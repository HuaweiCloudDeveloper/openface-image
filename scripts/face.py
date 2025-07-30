import logging
import sys
import os
import time
import pickle
import numpy as np
import streamlit as st
from PIL import Image
import face_recognition

# 配置日志
logger = logging.getLogger('FaceRecognition')
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

# 获取人脸特征向量（支持多人脸）
def getRep(imgPath, verbose=True, multiple=True):
    logger.info("处理图像: {}".format(imgPath))
    start = time.time()
    try:
        image = face_recognition.load_image_file(imgPath)
        face_locations = face_recognition.face_locations(image, model='cnn')  # 使用 CNN 模型提高准确性
        encodings = face_recognition.face_encodings(image, face_locations, num_jitters=1)  # 降低 num_jitters
        if not encodings:
            raise Exception("无法检测到人脸")
        if verbose:
            logger.info("特征提取耗时 {} 秒.".format(time.time() - start))
            logger.info("检测到的人脸数量: {}".format(len(encodings)))
            logger.info("特征向量维度: {}".format(len(encodings[0])))
        reps = []
        for i, encoding in enumerate(encodings):
            reps.append((i, encoding))  # 使用编号表示人脸顺序
        return reps
    except Exception as e:
        raise Exception(f"处理图像失败: {e}")

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
        logger.info(f"加载的标签: {labels}")
    except Exception as e:
        st.error(f"加载模型或标签失败: {e}")
        logger.error(f"加载模型或标签失败: {e}")
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
        st.image(uploaded_file, caption="上传的图片", use_container_width=True)

        # 进行人脸识别
        try:
            reps = getRep(test_image_path, verbose=True, multiple=True)
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
                st.write(f"预测结果: {person_name} (脸部编号={bbx}), 置信度: {confidence:.2f}")
                st.write(f"预测耗时: {time.time() - start:.2f} 秒")
                logger.info(f"预测结果: {person_name} (脸部编号={bbx}), 置信度: {confidence:.2f}")
        except Exception as e:
            st.error(f"人脸识别失败: {e}")
            logger.error(f"人脸识别失败: {e}")

if __name__ == "__main__":
    main()
