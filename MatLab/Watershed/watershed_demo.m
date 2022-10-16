% Step for performing watershed transform
% 1. Segment objects of interest
% 2. Convert the mask into an intensity profile using the distance
% transform
% 3. Run the watershed algorith
% 4. Update the original mask

I = rgb2gray(imread('coin.png'));
M = imbinarize(I);
imshow(M);  

% distance transform dd = bwdist(M)
% dd is distance transform (double)
% computes the distance between each pixel and the nearest non zero pixel
% distance = sket a straight line ( pythagorean if neccessary)
% therefore, value of white pixel is 0, black pixel is the distance to white
% we want a center of an object to be a basin => it must be black
% black dd is a positive value ( distance to white) => negate it
% we have a graph of basin
dd = bwdist(M);
mesh(dd)

% However, we don't need a hill but a basin
% Therefore, we -dd (negative, not inverve cause dd is double matrix)
% (do not inverve M before compute distance)
dd = -dd;
dd = imhmin(dd, 2);
mesh(dd);

% becuase we already have the all the need basin, watershed algorith 
% will compute the local minima between each object
% becuase object is black (0), background is white(1)
% distance between black pixel to white will be largest at the center
% smallest at the edge or boundary(where white pixel is its neighbor)
% these local minimun number will become zero in L
% However, we need only one local nimimun between each region
L = watershed(dd);
imshow(L, []);

% logical index demo
% A = [1 2 3 4 5]
% I = [false true true false false]
% >> A(I) = 2   3
% aslo I = A > 3
% A(I) = 4   5
% A(A > 3)  GIVE THE SAME RESULT

% watershed
M = ~M;
M(L == 0) = false;
imshow(M)







