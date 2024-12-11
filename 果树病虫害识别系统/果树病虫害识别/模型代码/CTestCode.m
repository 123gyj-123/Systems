%% 三、 TestCode识别图像类型

clc,clear
% 加载训练好的模型参数
load('trainedNet.mat');

% 读取待识别图像
[file,path] = uigetfile('*');
image = fullfile(path,file);
I = imresize(imread(image),[224,224]);

tic
% 使用模型分类
[label,scores] = classify(net, I);
accuracy = "准确率："+string(round(max(scores)*100))+"%"
toc

% 显示分类结果
[~,name] = xlsread('labelname.xlsx');
figure('Name','识别结果','NumberTitle','off') ;
imshow(I); 
fruit = name(label,1);
disease = name(label,2);
level = name(label,3);
title(['\bf',fruit]), xlabel(disease), ylabel(['严重程度：',level]);

