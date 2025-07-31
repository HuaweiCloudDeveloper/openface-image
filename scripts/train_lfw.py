import logging
import sys
import os
import cv2
import time
import openface
import pickle
import numpy as np
import streamlit as st
from PIL import Image

# 配置日志
logger = logging.getLogger('FaceRecognition')
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

# dlib 和 openface 模型配置
imgDim = 96
dlib_model_dir = '/home/openface/models/dlib'
openface_model_dir = '/home/openface/models/openface'
align = openface.AlignDlib(os.path.join(dlib_model_dir, "shape_predictor_68_face_landmarks.dat"))
net = openface.TorchNeuralNet(os.path.join(openface_model_dir, 'nn4.small2.v1.t7'), imgDim)

# 获取人脸特征向量（支持多人脸）
def getRep(imgPath, verbose=False, multiple=False):
    logger.info("处理图像: {}.".format(imgPath))
    bgrImg = cv2.imread(imgPath)
    if bgrImg is None:
        raise Exception("无法加载图像: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
    if verbose:
        logger.info("原始图像尺寸: {}".format(rgbImg.shape))

    start = time.time()
    if multiple:
        faceBoundingBoxs = align.getAllFaceBoundingBoxes(rgbImg)
    else:
        faceBoundingBox = align.getLargestFaceBoundingBox(rgbImg)
        faceBoundingBoxs = [faceBoundingBox]
    if len(faceBoundingBoxs) == 0 or (not multiple and faceBoundingBox is None):
        raise Exception("无法检测到人脸: {}".format(imgPath))
    if verbose:
        logger.info("人脸检测耗时 {} 秒.".format(time.time() - start))

    reps = []
    for bb in faceBoundingBoxs:
        start = time.time()
        alignedFace = align.align(imgDim, rgbImg, bb, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        if alignedFace is None:
            raise Exception("无法对齐图像: {}".format(imgPath))
        if verbose:
            logger.info("人脸对齐耗时 {} 秒.".format(time.time() - start))
            logger.info("边界框中心位于 {}, {}".format(bb.center().x, bb.center().y))

        start = time.time()
        rep = net.forward(alignedFace)
        if verbose:
            logger.info("OpenFace 前向传播耗时 {} 秒.".format(time.time() - start))
        reps.append((bb.center().x, rep))

    sreps = sorted(reps, key=lambda x: x[0])
    return sreps

# Streamlit 应用
def main():
    st.title("人脸识别系统")
    st.write("上传一张图片进行人脸识别分类")

    pwd = os.getcwd()
    clf_name = 'classifier_linear_svm.pkl'
    labels_name = 'labels.pkl'

    # 检查模型和标签文件是否存在
    if not os.path.exists(os.path.join(pwd, clf_name)) or not os.path.exists(os.path.join(pwd, labels_name)):
        st.error(f"模型文件 {clf_name} 或标签文件 {labels_name} 不存在，请先运行 train_lfw.py 进行训练！")
        return

    # 加载模型和标签
    try:
        clf = pickle.load(open(os.path.join(pwd, clf_name), 'rb'))
        labels = pickle.load(open(os.path.join(pwd, labels_name), 'rb'))
        st.success("已加载模型和标签！")
    except Exception as e:
        st.error(f"加载模型或标签失败: {e}")
        return

    # 上传图像
    uploaded_file = st.file_uploader("选择一张图片", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # 保存上传的图片
        test_image_path = os.path.join(pwd, 'test_images', uploaded_file.name)
        if not os.path.exists(os.path.join(pwd, 'test_images')):
            os.makedirs(os.path.join(pwd, 'test_images'))
        with open(test_image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="上传的图片", use_column_width=True)

        # 进行人脸识别
        try:
            reps = getRep(test_image_path, multiple=True)
            if len(reps) > 1:
                st.write("图像中检测到多个人脸，从左到右列出：")
            for r in reps:
                rep = r[1].reshape(1, -1)
                bbx = r[0]
                start = time.time()
                pred = clf.predict_proba(rep).ravel()
                max_prob_index = np.argmax(pred)
                person_name = labels[max_prob_index]
                confidence = pred[max_prob_index]
                st.write(f"预测结果: {person_name.decode('utf-8')} @ x={bbx:.2f}, 置信度: {confidence:.2f}")
                st.write(f"预测耗时: {time.time() - start:.2f} 秒")
                for name, prob in zip(labels, pred):
                    st.write(f"{name.decode('utf-8')} 的概率: {prob:.2f}")
        except Exception as e:
            st.error(f"人脸识别失败: {e}")

if __name__ == "__main__":
    main()
