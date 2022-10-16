% read image as gray
image = rgb2gray(imread("coin.png"));
imshow(image)

%convert to binary
% in this case foreground object already black, no need to inverse
% otherwise, comvert image to binary => inverse => distance transform
% => negate distrance transform => water shed
% shortcut: dd = -bwdist(~mask)
% in ourcase mask already a  ~mask
binary_image = imbinarize(image);
imshow(binary_image)

% distance transform
dd = -bwdist(binary_image);

%supress the local minimun
% otherword: cut the tip of the basin so that we have only one tip each
% basin
d2 = imhmin(dd, 2);
mesh(dd);

% apply watershed algortih
L = watershed(d2);

% change boudary to zero
binary_image = ~binary_image;
binary_image(L == 0) = false;
imshow(binary_image);

