% opening: erode followed by dilate
% closing: dilate followed by erode

% is dilate the same as imfill?
I = imread('2cell.jpg');
SE = strel("square", 2);

% M = imopen(BW, SE)
% usefull for smoothing the edges of segmented objects
% remove white object and keep the rest
% removing object with a specific shape from the image
% https://www.youtube.com/watch?v=E_vU1Wd7Ks8&list=PLuBO7Twg9avCvnO-O-t3O_-6F2XQ3ViFG&index=9
open = imopen(I, SE);
imshow(open, [])

% M = imclose(BW, SE)
% fill hole in object, preserving the shape and size of other 
close = imopen(I, SE);
imshow(close, [])
