%% ���ݵ���
clear;clc;
DatasetPath = 'E:\ģʽʶ��\235442-�����-��ĩ����ҵ\�������溦ʶ��\ģ�ʹ���\ѵ����'; %���ݼ�·��
imds = imageDatastore(DatasetPath, 'IncludeSubfolders',true, 'LabelSource','foldernames');

%% ����ѵ��������֤��
[imgTrain,imgValid] = splitEachLabel(imds,0.8,'randomize'); %��������� ImageDatastore ��ǩ,��80%ѵ����20%��֤��

% ����ͼ���С��ƥ����������㡣
imdsTrain = augmentedImageDatastore([224 224 3],imgTrain);
imdsValid = augmentedImageDatastore([224 224 3],imgValid);

%% VGG19 ����
% Ԥѵ������
params = load("params_2020_12_31__21_04_38.mat");

% ������
layers = [
    imageInputLayer([224 224 3],"Name","input","AverageImage",params.input.AverageImage)
    convolution2dLayer([3 3],64,"Name","conv1_1","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv1_1.Bias,"Weights",params.conv1_1.Weights)
    reluLayer("Name","relu1_1")
    convolution2dLayer([3 3],64,"Name","conv1_2","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv1_2.Bias,"Weights",params.conv1_2.Weights)
    reluLayer("Name","relu1_2")
    maxPooling2dLayer([2 2],"Name","pool1","Stride",[2 2])
    convolution2dLayer([3 3],128,"Name","conv2_1","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv2_1.Bias,"Weights",params.conv2_1.Weights)
    reluLayer("Name","relu2_1")
    convolution2dLayer([3 3],128,"Name","conv2_2","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv2_2.Bias,"Weights",params.conv2_2.Weights)
    reluLayer("Name","relu2_2")
    maxPooling2dLayer([2 2],"Name","pool2","Stride",[2 2])
    convolution2dLayer([3 3],256,"Name","conv3_1","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv3_1.Bias,"Weights",params.conv3_1.Weights)
    reluLayer("Name","relu3_1")
    convolution2dLayer([3 3],256,"Name","conv3_2","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv3_2.Bias,"Weights",params.conv3_2.Weights)
    reluLayer("Name","relu3_2")
    convolution2dLayer([3 3],256,"Name","conv3_3","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv3_3.Bias,"Weights",params.conv3_3.Weights)
    reluLayer("Name","relu3_3")
    convolution2dLayer([3 3],256,"Name","conv3_4","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv3_4.Bias,"Weights",params.conv3_4.Weights)
    reluLayer("Name","relu3_4")
    maxPooling2dLayer([2 2],"Name","pool3","Stride",[2 2])
    convolution2dLayer([3 3],512,"Name","conv4_1","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv4_1.Bias,"Weights",params.conv4_1.Weights)
    reluLayer("Name","relu4_1")
    convolution2dLayer([3 3],512,"Name","conv4_2","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv4_2.Bias,"Weights",params.conv4_2.Weights)
    reluLayer("Name","relu4_2")
    convolution2dLayer([3 3],512,"Name","conv4_3","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv4_3.Bias,"Weights",params.conv4_3.Weights)
    reluLayer("Name","relu4_3")
    convolution2dLayer([3 3],512,"Name","conv4_4","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv4_4.Bias,"Weights",params.conv4_4.Weights)
    reluLayer("Name","relu4_4")
    maxPooling2dLayer([2 2],"Name","pool4","Stride",[2 2])
    convolution2dLayer([3 3],512,"Name","conv5_1","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv5_1.Bias,"Weights",params.conv5_1.Weights)
    reluLayer("Name","relu5_1")
    convolution2dLayer([3 3],512,"Name","conv5_2","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv5_2.Bias,"Weights",params.conv5_2.Weights)
    reluLayer("Name","relu5_2")
    convolution2dLayer([3 3],512,"Name","conv5_3","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv5_3.Bias,"Weights",params.conv5_3.Weights)
    reluLayer("Name","relu5_3")
    convolution2dLayer([3 3],512,"Name","conv5_4","Padding",[1 1 1 1],"WeightL2Factor",0,"Bias",params.conv5_4.Bias,"Weights",params.conv5_4.Weights)
    reluLayer("Name","relu5_4")
    maxPooling2dLayer([2 2],"Name","pool5","Stride",[2 2])
    fullyConnectedLayer(4096,"Name","fc6","WeightL2Factor",0,"Bias",params.fc6.Bias,"Weights",params.fc6.Weights)
    reluLayer("Name","relu6")
    dropoutLayer(0.5,"Name","drop6")
    fullyConnectedLayer(4096,"Name","fc7","WeightL2Factor",0,"Bias",params.fc7.Bias,"Weights",params.fc7.Weights)
    reluLayer("Name","relu7")
    dropoutLayer(0.5,"Name","drop7")
    fullyConnectedLayer(9,"Name","fc8","WeightL2Factor",0)
    softmaxLayer("Name","softmax")
    classificationLayer("Name","classoutput")];

%% ����ѵ������
 options = trainingOptions('sgdm', ...
    'MiniBatchSize',4, ...
    'InitialLearnRate',0.0001, ...
    'Shuffle','every-epoch', ...
    'ValidationData',imdsValid,...
    'ValidationFrequency',50,...
    'ExecutionEnvironment','auto',...
    'Verbose',false, ...
    'Plots','training-progress');
%% ѵ��������
 [net,traininfo]= trainNetwork(imdsTrain,layers,options);

%% ����ѵ���ò���
save('trainedNet.mat','net');%����ѵ���õ������絽���أ��ļ���ΪtrainedNet.mat
save('trainedInfo.mat','traininfo');%����ѵ����Ϣ
















