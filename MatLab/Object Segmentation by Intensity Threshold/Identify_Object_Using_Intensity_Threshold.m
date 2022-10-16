I = imread('rice.jpg');
imshow(I, [])

% cell by cell comprasion, that is why matlab is built for image processing
% Toll/data tips to inspect image pixel by pixel, intesity is threshold
mask = I > 115;
imshow(mask, [])

% use improfile to inspect image intensity ( find threshold)
% imshow image first, don't forget [] parameter
% improfile
% click start point, then click end point (can be a zigzag)
% press enter when done
imshow(I, [])
improfile

%BW = bwperim(L)
% return a matrix containing the perimeter of true region in the input mask
% L should be a logical/binary matrix/image
% other words: return the boudary (Canny in openCV)
BW = bwperim(mask);
imshow(BW)

%imshowpair(A, B)
%display a merger image. A: is display as green, B: is display as magenta
imshowpair(I, BW)

% summary: foreground pixels intensities should distinguishable from the
% backgound, which is not the case of rice.jpg 
% rule of thumb: intesities should be 2x difference