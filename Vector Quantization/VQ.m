clear all; close all; clc;

img = imread('lena.bmp');
img = imresize(img,[512 512]);
figure,imshow(img);

codebookSize = 1024;
blockSize = 4;
codebook = zeros(blockSize^2,codebookSize); 

%% codebook
tic;
pool = im2col(img,[blockSize blockSize],'sliding');
pool = double(pool);
[poolHeight,poolWidth] = size(pool);

randIndex = randperm(poolWidth);
codebook(:) = pool(:,randIndex(1:codebookSize));

trainTime = 30;
for t=1 : trainTime
    index = zeros(1,poolWidth);
    for i=1 : poolWidth
        temp = repmat(pool(:,i),1,codebookSize);
        [val,ind] = min(sum((temp-codebook).^2));
        index(i) = ind;
    end

    order = 1:poolWidth;
    for i = 1 : codebookSize
        codebook(:,i) = round(mean(pool(:,order(index==i))')');
    end
end
toc
save codebook codebook


%% encoder
tic;
load codebook

pool = im2col(img,[blockSize blockSize],'distinct');
pool = double(pool);
[imgHeight,imgWidth] = size(img);
index = zeros(imgHeight/blockSize,imgWidth/blockSize);

for i=1 : numel(index)
    temp = repmat(pool(:,i),1,codebookSize);
    [val,ind] = min(sum((temp-codebook).^2));
    index(i) = ind;
end
toc

%% decoder
tic;
pool = codebook(:,index(:));
VQResult = uint8(col2im(pool,[blockSize blockSize],[imgHeight imgWidth],'distinct'));
figure,imshow(VQResult);
toc