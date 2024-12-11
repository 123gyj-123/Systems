%% ���� TestCodeʶ��ͼ������

clc,clear
% ����ѵ���õ�ģ�Ͳ���
load('trainedNet.mat');

% ��ȡ��ʶ��ͼ��
[file,path] = uigetfile('*');
image = fullfile(path,file);
I = imresize(imread(image),[224,224]);

tic
% ʹ��ģ�ͷ���
[label,scores] = classify(net, I);
accuracy = "׼ȷ�ʣ�"+string(round(max(scores)*100))+"%"
toc

% ��ʾ������
[~,name] = xlsread('labelname.xlsx');
figure('Name','ʶ����','NumberTitle','off') ;
imshow(I); 
fruit = name(label,1);
disease = name(label,2);
level = name(label,3);
title(['\bf',fruit]), xlabel(disease), ylabel(['���س̶ȣ�',level]);

