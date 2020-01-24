from seam_carve import seam_carve, resize
import cv2

SHOULD_DOWNSIZE = True
DOWNSIZE_WIDTH = 1000

def insta_carve(im, dy, dx):

    output = seam_carve(im, dy, dx)

    cv2.imwrite('Images/test_result.png', output)


def num_seams(im):
    '''
    Takes the image input as an openCV image object
    and calculates the number of seams to remove to
    make the image a square.
    '''
    h, w = im.shape[:2]

    dy = 0
    dx = 0
    
    if(h>w):
        dy = w-h
    elif(w>h):
        dx = h-w

    return  dy, dx


if __name__=='__main__':
    image_path = "Images/test2.jpg"
    im = cv2.imread(image_path)

    # downsize image for faster processing
    h, w = im.shape[:2]
    if SHOULD_DOWNSIZE and w > DOWNSIZE_WIDTH:
        im = resize(im, width=DOWNSIZE_WIDTH)

    dy, dx = num_seams(im)
    insta_carve(im, dy, dx)

    