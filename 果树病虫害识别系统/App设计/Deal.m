function [fruit,disease,level,accuracy,time,I] = Deal()
%调用模型识别病虫害

% 加载训练好的模型参数
load('trainedNet.mat');

% 读取待识别图像
[file,path] = uigetfile('*');
image = fullfile(path,file);
I = imresize(imread(image),[224,224]);

tic
% 使用模型分类
[label,scores] = classify(net, I);
time = string(round(toc,2))+"s";

% 显示分类结果
accuracy = string(round(max(scores)*100))+"%"
[~,name] = xlsread('labelname.xlsx');
fruit = name(label,1);
disease = name(label,2);
level = name(label,3);
end