

<h1 align="center">OpenFace open-source facial recognition tool</h1>
<p align="center">
    <strong>English</strong> | <a href="README_ZH.md">简体中文</a>
</p>




## Table of Contents

- [Repository Introduction](#project-introduction)
- [Prerequisites](#prerequisites)
- [Image Description](#image-description)
- [Get Help](#get-help)
- [How to Contribute](#how-to-contribute)

## Project Introduction



[OpenFace](https://github.com/cmusatyalab/openface)  is an open-source facial recognition tool based on neural networks, which utilizes deep neural networks to generate 128 dimensional facial feature vectors and supports LFW or custom dataset training for identity recognition. This product provides an out-of-the-box OpenFace based on the Huawei Cloud EulerOS 2.0 64-bit system of Kunpeng servers.

## Core Features

- **End to end visualization interaction system:** Integrate Streamlit to build a web interface that supports image upload, real-time result display, and confidence display. The operation is intuitive and suitable for non-technical users
- **Lightweight localized deployment:** All calculations are completed locally, without the need for networking or calling third-party APIs, ensuring user privacy and security. It is also compatible with CPU environments and reduces deployment barriers
- **Modular Model Management and Scalability:** Feature extraction and classification models are stored separately (`. pkl `), supporting flexible replacement of classifiers (such as SVM, k-NN) for easy integration of new samples and incremental training in the future

The open-source image product [OpenFace open-source facial recognition tool](https://marketplace.huaweicloud.com/intl/hidden/contents/fbc9139b-e9b3-48b7-896c-8f6f44e9cf7b) provided by this project has pre-installed the the 0.2.2 version of OpenFace and its related runtime environment, and provides deployment templates. Come and refer to the usage guide to easily start an efficient "out-of-the-box" experience!

> **System requirements are as follows:**
>
> - CPU: 2vCPUs or higher
> - RAM: 4GB or larger
> - Disk: At least 40GB

## Prerequisites



[Register a Huawei account and activate Huawei Cloud](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## Image Description



| Image Specification                                          | Feature Description                                          | Remarks |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------- |
| [OpenFace-0.2.2-kunpeng](https://github.com/HuaweiCloudDeveloper/openface-image/tree/OpenFace-0.2.2-kunpeng) | Installed and deployed based on Kunpeng servers + Huawei Cloud EulerOS 2.0 64-bit |         |

## Get Help

- For more questions, you can contact us through [issues](https://github.com/HuaweiCloudDeveloper/openface-image/issues) or the service support of the specified product in the Huawei Cloud Marketplace.
- For other open-source images, please refer to [open-source-image-repos](https://github.com/HuaweiCloudDeveloper/open-source-image-repos).

## How to Contribute

- Fork this repository and submit a merge request.
- Synchronously update README.md based on your open-source image information.
