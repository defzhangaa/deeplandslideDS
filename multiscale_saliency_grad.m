% 请修改数据集导入地址
file_path =  'F:\code\RoadCrackClassification\CRACK500-20220623T155714Z-001\CRACK500\test\';
file_list = dir(file_path);

for i = 3:length(file_list)
    name = file_list(i).name;
    pic = imread([file_path,name]);
    pic = imgaussfilt(pic,0.5);
    I = rgb2gray(pic);
    hx=[-1 -2 -1;0 0 0 ;1 2 1];%生产sobel垂直梯度模板
    hy=hx'; %生产sobel水平梯度模板
    gradx=filter2(hx,I,'same');
    gradx=abs(gradx); %计算图像的sobel垂直梯度
    grady=filter2(hy,I,'same');
    grady=abs(grady); %计算图像的sobel水平梯度
    grad=gradx+grady; %得到图像的sobel梯度
    grad = grad/max(max(grad));

    Img = im2double(rgb2gray(pic));
    [h,w,c] = size(Img);
%     1.对原尺度进行计算
    Img1 = Img;
%     傅立叶变换
    FFT = fft2(Img1);
%     对数幅度谱
    LogAmplitude = log(abs(FFT));
%     相位
    Phase = angle(FFT);
%     原幅度谱减去局部平滑后的幅度谱
    SpectralResidual = LogAmplitude - imfilter(LogAmplitude, fspecial('average', 3), 'replicate');
%     融合幅度与相位
    saliencyMap1 = abs(ifft2(exp(SpectralResidual+1i*Phase))).^2;
    saliencyMap1 = mat2gray(imfilter(saliencyMap1, fspecial('gaussian', [8, 8], 8)));

%     2.对2/3尺度进行计算
    Img2 = imresize(Img,[floor(h*2/3), floor(w*2/3)]);
%     傅立叶变换
    FFT = fft2(Img2);
%     对数幅度谱
    LogAmplitude = log(abs(FFT));
%     相位
    Phase = angle(FFT);
%     原幅度谱减去局部平滑后的幅度谱
    SpectralResidual = LogAmplitude - imfilter(LogAmplitude, fspecial('average', 3), 'replicate');
%     融合幅度与相位
    saliencyMap2 = abs(ifft2(exp(SpectralResidual+1i*Phase))).^2;
    saliencyMap2 = mat2gray(imfilter(saliencyMap2, fspecial('gaussian', [8, 8], 8)));
    saliencyMap2 = imresize(saliencyMap2,[h,w]);

%     3.对1/3尺度进行计算
    Img3 = imresize(Img,[floor(h/3), floor(w/3)]);
%     傅立叶变换
    FFT = fft2(Img3);
%     对数幅度谱
    LogAmplitude = log(abs(FFT));
%     相位
    Phase = angle(FFT);
%     原幅度谱减去局部平滑后的幅度谱
    SpectralResidual = LogAmplitude - imfilter(LogAmplitude, fspecial('average', 3), 'replicate');
%     融合幅度与相位
    saliencyMap3 = abs(ifft2(exp(SpectralResidual+1i*Phase))).^2;
    saliencyMap3 = mat2gray(imfilter(saliencyMap3, fspecial('gaussian', [8, 8], 8)));
    saliencyMap3 = imresize(saliencyMap3,[h,w]);

%     以entropy为权重融合multi-scale saliency
    en1 = entropy(saliencyMap1);
    en2 = entropy(saliencyMap2);
    en3 = entropy(saliencyMap3);
    sum = en1+en2+en3;
    en1 = en1/sum;
    en2 = en2/sum;
    en3 = en3/sum;
    
    saliencyMap = saliencyMap1*en1 + saliencyMap2*en2 + saliencyMap3*en3;
%     imshow(saliencyMap);

%     再加上之前求的grad得到最终的saliencyMap
     saliencyMap = saliencyMap + grad;
%     归一化
     saliencyMap = saliencyMap/max(max(saliencyMap));

    imwrite(saliencyMap,['F:\code\RoadCrackClassification\CRACK500-20220623T155714Z-001\CRACK500\srtest\',name])
end
