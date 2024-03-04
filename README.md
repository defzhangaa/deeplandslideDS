# deeplandslideDS
This is the source codebase for: **Deep Evidential Remote Sensing Landslide Image Classification With a New Divergence, Multi-Scale Saliency and an Improved Three-Branched Fusion.** This work has been accepted by IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing (IEEE JSTARS) in Jan 12 2024, and published online in IEEE Xplore: https://doi.org/10.1109/JSTARS.2024.3354455 . We sincerely thank the timely help of Prof. Lianmeng Jiao from Northwestern Polytechnical University (NPU) for improving the paper's quality. 


**Video:** https://www.bilibili.com/video/BV1nC4y1673W/?spm_id_from=333.999.0.0&vd_source=99d771014e44a2063a6907c1ea2fa567 .

**Graphical abstract:**

<img width="1200" alt="fig000_1" src="https://github.com/defzhangaa/deeplandslideDS/assets/128769580/7e266e86-0a20-4524-aaf1-0cc3acecbfb5">

**Post:**

<img width="1240" alt="海报jstars" src="https://github.com/defzhangaa/deeplandslideDS/assets/128769580/970f58cd-e102-4b05-8502-711f93310092">


**HOW TO USE THIS REPO**: The experiments of this paper can be repeated on your platform with the following steps: 

1. Download the Bijie landslide image dataset, which is avaliable at http://gpcv.whu.edu.cn/data/Bijie_pages.html *. 

2. Use the code multiscale_saliency_grad.m to obtain multi-scale visual saliency. Then the remote sensing images after channel-wise fusion can be avaliable.  

3. Train the deep neural networks using fused images with the source code (in the folder Awesome-Backbones-main, which is from repo https://github.com/Fafa-DL/Awesome-Backbones) and initial weights in OpenMMLab's Image Classification Toolbox and Benchmark, which is avaliable at https://github.com/open-mmlab/mmclassification. 

4. Fuse the decisions from deep neural networks with the proposed three-branched fusion model (network_fusion.py). 


**Please cite this paper** if this code contributes to your research:   
@article{zhang2024deep,   
title={Deep Evidential Remote Sensing Landslide Image Classification With a New Divergence, Multi-Scale Saliency and an Improved Three-Branched Fusion},   
author={Zhang, Jiaxu and Cui, Qi and Ma, Xiaojian},   
journal={IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing},   
volume={69},   
pages={3799-3820},   
year={2024},   
month={Jan.},   
publisher={IEEE}   
}

