clearvars
% file location
path = "/Users/cara/Desktop/OneDrive - UBC/PhD/Experiments/2022_06_24" + ...
    "/SideCam/";
filename = path + 'plume.MP4';

%read in video and open test frame
v = VideoReader(filename);

% get the cropping zone
t1 = 4*60;
i = read(v,t1+10000);
b = read(v,t1);

%close

%% preprocess and save files

tic

for k = 1:v.NumFrames
    i = read(v,k); %read frame
    i = imcrop(i,rectout); %crop using defined above
    i = im2double(i);
    i = rgb2gray(i);
    i_filt = imboxfilt(i,17); %sliding box filter
    i_hp = i - i_filt; %highpass
    T = graythresh(i_hp);
    i_lp = i_hp > T;
    i_final = imgaussfilt(im2uint8(i_lp),'FilterDomain','frequency','Filtersize',5);
    rgb = cat(3, i_final, i_final, i_final);
    framename = path + "push3/push3_orig_" + num2str(k,'%04.f')+ ".png";
    imwrite(i, framename)
end

toc

%% write
tic

vidname = path + 'push3/push3gauss';
writerObj = VideoWriter(vidname);
writerObj.FrameRate = 30;
open(writerObj);

for k = 1:v.NumFrames
    framename = path + "push3/push3_gauss_" + num2str(k,'%04.f')+ ".png";
    I = imread(framename);
    %I = double(I);
    writeVideo(writerObj, I);
end

close(writerObj)

toc