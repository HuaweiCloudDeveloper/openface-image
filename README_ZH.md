<h1 align="center">OpenFace开源人脸识别工具</h1>
<p align="center">
  <a href="README.md"><strong>English</strong></a> | <strong>简体中文</strong>
</p>



## 目录

- [仓库简介](#项目介绍)
- [前置条件](#前置条件)
- [镜像说明](#镜像说明)
- [获取帮助](#获取帮助)
- [如何贡献](#如何贡献)

## 项目介绍

[OpenFace](https://github.com/cmusatyalab/openface) 是一款基于神经网络的开源人脸识别工具，利用深度神经网络，生成128维人脸特征向量，支持lfw或自定义数据集训练进行身份识别。本商品基于鲲鹏服务器的Huawei Cloud EulerOS 2.0 64bit系统，提供开箱即用的OpenFace。

## 核心特性

- **端到端可视化交互系统：** 集成 Streamlit 构建 Web 界面，支持图片上传、实时结果显示与置信度展示，操作直观，适合非技术用户使用
- **轻量本地化部署：** 所有计算在本地完成，无需联网或调用第三方 API，保障用户隐私安全，同时兼容 CPU 环境运行，降低部署门槛
- **模块化模型管理与可扩展性：** 特征提取与分类模型分离存储（`.pkl`），支持灵活更换分类器（如 SVM、k-NN），便于后续集成新样本与增量训练

本项目提供的开源镜像商品 [OpenFace开源人脸识别工具](https://marketplace.huaweicloud.com/hidden/contents/9d0d496c-0205-4fc0-99ae-e05cf4d5fa19#productid=OFFI1151327957189582848) 已预先安装0.2.2版本的OpenFace及其相关运行环境，并提供部署模板。快来参照使用指南，轻松开启“开箱即用”的高效体验吧。

> **系统要求如下：**
>
> - CPU: 2vCPUs 或更高
> - RAM: 4GB 或更大
> - Disk: 至少 40GB

## 前置条件

[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## 镜像说明

| 镜像规格                                                     | 特性说明                                                 | 备注 |
| ------------------------------------------------------------ | -------------------------------------------------------- | ---- |
| [OpenFace-0.2.2-kunpeng](https://github.com/HuaweiCloudDeveloper/openface-image/tree/OpenFace-0.2.2-kunpeng) | 基于鲲鹏服务器 + Huawei Cloud EulerOS 2.0 64bit 安装部署 |      |

## 获取帮助

- 更多问题可通过 [issue](https://github.com/HuaweiCloudDeveloper/openface-image/issues) 或 华为云云商店指定商品的服务支持 与我们取得联系
- 其他开源镜像可看 [open-source-image-repos](https://github.com/HuaweiCloudDeveloper/open-source-image-repos)

## 如何贡献

- Fork 此存储库并提交合并请求
- 基于您的开源镜像信息同步更新 README.md
