# deeplandslideDS
**Video:** https://www.bilibili.com/video/BV1nC4y1673W/?spm_id_from=333.999.0.0&vd_source=99d771014e44a2063a6907c1ea2fa567 .

**Feb 02 2024:** This work has been published online in IEEE Xplore: https://doi.org/10.1109/JSTARS.2024.3354455 . 

We sincerely thank the timely help of Prof. Lianmeng Jiao from Northwestern Polytechnical University (NPU) for improving the paper's quality. 

**Jan 12 2024:** **CONGRATULATIONS!** The present study has been accepted by IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing (IEEE JSTARS) in Jan 12 2024.
The published version will be uploaded in this repo as long as available. 


**This is the source codebase for: Deep Evidential Remote Sensing Landslide Image Classification With a New Divergence, Multi-Scale Saliency and an Improved Three-Branched Fusion.** 


**IMPORTANT**: The experiments of this paper can be repeated on your platform with the following steps: 

1. Download the Bijie landslide image dataset, which is avaliable in [1] at http://gpcv.whu.edu.cn/data/Bijie_pages.html *. 

2. Use the code multiscale_saliency_grad.m to obtain multi-scale visual saliency. Then the remote sensing images after channel-wise fusion can be avaliable.  

3. Train the deep neural networks using fused images with the source code (in the folder Awesome-Backbones-main, which is from repo https://github.com/Fafa-DL/Awesome-Backbones) and initial weights in OpenMMLab's Image Classification Toolbox and Benchmark, which is avaliable at https://github.com/open-mmlab/mmclassification. 

4. Fuse the decisions from deep neural networks with the proposed three-branched fusion model (network_fusion.py). 

Reference: 

[1] Ji, S., Yu, D., Shen, C., Li, W., & Xu, Q. Landslide detection from an open satellite imagery and digital elevation model dataset using attention boosted convolutional neural networks. Landslides, 1-16, 2020. 

* In Sep 2023, the website of Bijie dataset seems unaccesible. You may contact the authors for this dataset at zhangjx283(at)mail2.sysu.edu.cn

<img width="889" alt="fig000_1" src="https://github.com/defzhangaa/deeplandslideDS/assets/128769580/7e266e86-0a20-4524-aaf1-0cc3acecbfb5">


<img width="1440" alt="海报jstars" src="https://github.com/defzhangaa/deeplandslideDS/assets/128769580/970f58cd-e102-4b05-8502-711f93310092">
