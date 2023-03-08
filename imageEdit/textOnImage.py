import cv2
from Text import Text


BASEPATH = "./assets/baseImage/"
ALPHA = 0.7
FONT_SCALE_FACTOR = (5/720)
FONT_THICKNESS_FACTOR = (20/720)

def getImagePath(imageName):
    return BASEPATH+imageName

def downsize_to_youtube_thumbnail(imageToResize):
    oldDimensions = imageToResize.shape
    width = 1280
    height = 720
    minWidth = 640
   
    if(oldDimensions[0] < height):
        height = oldDimensions[0]

    if(oldDimensions[1] < width and oldDimensions[1]>minWidth):
        width = oldDimensions[1]

    dim = (width, height)
   
    downsizedImage = cv2.resize(imageToResize, dim, interpolation = cv2.INTER_AREA)
    return downsizedImage

if __name__ == "__main__":
    imageName = "sunflower.jpg"
    # imageName = "Little_Joys.jpeg"
    imagePath = getImagePath(imageName)
    image = cv2.imread(imagePath)
   
    window_name = imageName

    image = downsize_to_youtube_thumbnail(image)
    dimensions = image.shape
    imageHeight, imageWidth, _= dimensions
    print(imageHeight)
    print(imageWidth)
    
    # #------------image2--------------
    # imageName2 = "Little_Joys.jpeg"
    # image2 = cv2.imread(getImagePath(imageName2))
    # image2Dimensions = image2.shape
    # print("image2 size: ", image2Dimensions[0])
    #  #---------------------------------


    #Title Val
    val = "HELLO"
    # font = cv2.FONT_HERSHEY_SIMPLEX
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    fontScale = FONT_SCALE_FACTOR * imageHeight
    color_white = (255, 255, 255)
    color_black = (0,0,0)
    thickness = int(FONT_THICKNESS_FACTOR * imageHeight * ALPHA)
    org= (int(imageWidth*ALPHA/2),int(imageHeight/2))
    lineType = cv2.LINE_AA
    title_white = Text(val, font, fontScale, org, color_white, thickness, lineType)

    imageWithText = cv2.putText(image, title_white.getVal(), title_white.getOrg(), title_white.getFont(), title_white.getFontScale(), title_white.getColor(), title_white.getThickness(), title_white.getLineType())


    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()