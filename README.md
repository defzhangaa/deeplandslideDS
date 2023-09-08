# deeplandslideDS
This is the source codebase for: A Deep Evidence-theoretic Remote Sensing Landslide Image Classification Frame with a New Belief Divergence, Multi-scale Visual Saliency and an Improved Three-branched Fusion Model. 


<img width="889" alt="fig000_1" src="https://github.com/defzhangaa/deeplandslideDS/assets/128769580/7e266e86-0a20-4524-aaf1-0cc3acecbfb5">


**IMPORTANT**: The experiments of this paper can be repeated on your platform with the following steps: 

1. Download the Bijie landslide image dataset, which is avaliable in [1] at http://gpcv.whu.edu.cn/data/Bijie_pages.html . 

2. Use the code multiscale_saliency_grad.m to obtain multi-scale visual saliency. Then the remote sensing images after channel-wise fusion can be avaliable.  

3. Train the deep neural networks using fused images with the source code (in the folder Awesome-Backbones-main, which is from repo https://github.com/Fafa-DL/Awesome-Backbones) and initial weights in OpenMMLab's Image Classification Toolbox and Benchmark, which is avaliable at https://github.com/open-mmlab/mmclassification. 

4. Fuse the decisions from deep neural networks with the proposed three-branched fusion model (network_fusion.py). 

[1] Ji, S., Yu, D., Shen, C., Li, W., & Xu, Q. Landslide detection from an open satellite imagery and digital elevation model dataset using attention boosted convolutional neural networks. Landslides, 1-16, 2020. 
