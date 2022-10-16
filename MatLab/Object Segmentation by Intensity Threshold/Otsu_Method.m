I = imread('rice.jpg');
imshow(I, [])

% Otsu method
mask = imbinarize(I);
imshow(mask)

% mask = imfill(mask, 'holes')
% fill a holes (regions of false surrounded by trues) in a mask
mask = imfill(mask, 'holes')
imshow(mask)

% otsu method
% work well if the histogram has a bimodal distribution

% demonstration of infill
B = imread('holes.png');
% image create by paint is rgb. Remember to convert to gray first
mask1 = imbinarize(rgb2gray(B));
% white is true/ black is false
mask1 = ~(mask1);
% fill gap inside white object
% This is why this method do not work with rice.jbg. black hole inside 
% rice particle is not enclose
mask1 = imfill(mask1, 'holes');
% imshow
imshow(mask1, [])