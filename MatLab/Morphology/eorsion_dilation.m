% erode: imagine we invade object from the outside in. If the is no
% back-up of behind(constraint to the structuring element) pixel 
% with the value of true. The current processing pixel is swipe out

% dilation: same concept, but instead of being erode, false pixed that
% located next to the true pixel(of course in the same SE) will become a 
% new true pixel

% SE play a significant role here. A cross SE in dilation can not 
% turn the edge pixed of rectangle object to true. But the square SE CAN

I = imread('2cell.jpg');
imshow(I, [])

% M = imerode(BW, SE)
% BW = logical array(mask)
% SE = structuring elements
% Structuring Element can be created by: SE = strel('quare', w)
    %SE = strel(nhood)
    %SE = strel("diamond",r)
    %SE = strel("disk",r)
    %SE = strel("disk",r,n)
    %SE = strel("octagon",r)
    %SE = strel("line",len,deg)
    %SE = strel("rectangle",[m n])
    %SE = strel("square",w)
    %SE = strel("cube",w)
    %SE = strel("cuboid",[m n p])
    %SE = strel("sphere",r) This is a 3d array ( ignore for now)
 
% in this case, create a 3x3 matrix of true
SE = strel('square', 10)

% other way: SE = true(3)
% manual cross SE: SE = [false true false; true true true; false true false];
Mout = imerode(I, SE);
imshow(Mout, [])

% clearvars -except M

Mout = imdilate(I, SE);
imshow(Mout, [])

