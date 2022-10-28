

img = imread('trafficSign.jpg');
hsv = rgb2hsv(img);
imshow(img);
h = imfreehand;
M = h.createMask;

hMin = 1;
hMax = 0;
sMin = 1;
sMax = 0;
vMin = 1;
vMax = 0;


for row = 1:size(M,1)
    for col = 1:size(M,2) 
        if M(row,col) == 1 && hsv(row,col,1) ~= 0  && hsv(row,col,2) ~= 0  && hsv(row,col,2) ~= 0
            % h extreme
            if hsv(row,col,1) < hMin
                hMin = hsv(row,col,1);
            end
            if hsv(row,col,1) > hMax
                hMax = hsv(row,col,1);
            end
            % s extreme
            if hsv(row,col,2) < sMin
                sMin = hsv(row,col,2);
            end
            if hsv(row,col,2) > sMax
                sMax = hsv(row,col,2);
            end
            % v extreme
            if hsv(row,col,1) < vMin
                vMin = hsv(row,col,1);
            end
            if hsv(row,col,3) > vMax
                vMax = hsv(row,col,1);
            end

        end
    end
end
fprintf("h:%.2f - %.2f\n",hMin*180,hMax*180);
fprintf("s:%.2f - %.2f\n",sMin*255,sMax*255);
fprintf("v:%.2f - %.2f\n",vMin*255,vMax*255);
