I = imread('rice.jpg')
imshow(I)

% mask = imbinarize(I)
% otsu method do not work well in this situatiob
% use other refining method

% manual theshold
mask = I > 120;
imshow(mask, [])

% bwareopen(BW, P) = removes true region in BW with ares less than P
M = bwareaopen(mask, 100);
imshow(M)

% fill in the gap
M = imfill(M, 'holes');
imshow(M)

% smooth the boudary using opening
SE = strel('square', 3);
M = imopen(M, SE);
imshow(M, [])

% beautiful but they still stick to each other
%SE = [false true false; true true true; false true false];
%M = imerode(M, SE);
%imshow(M, [])

% kind of
% M = imclearborder(BW) = removes true regions which intersect with the 
% image border
%M = imclearborder(M)
%imshow(M, [])

dd = -bwdist(~M);
d2 = imhmin(dd, 2);
mesh(d2);

L = watershed(d2);
M (L == 0) = false;
imshow(M)
