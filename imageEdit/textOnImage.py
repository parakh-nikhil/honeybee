import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

from Text import Text

ASSETS_PATH = "./assets/"
IMAGES_BASEPATH = ASSETS_PATH+"baseImage/"
FONTS_BASEPATH = ASSETS_PATH+"fonts/"
ALPHA = 0.6
FONT_SCALE_FACTOR = (2/720)
CUSTOM_FONT_SCALE_FACTOR = (100/720)
FONT_THICKNESS_FACTOR = (5/720)

def getImagePath(imageName):
    return IMAGES_BASEPATH+imageName

def getFontPath(pathToTtf):
    return FONTS_BASEPATH+pathToTtf

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
    images = ["sunflower.jpg",  "Little_Joys.jpeg"]
    imageName = images[1]
    imagePath = getImagePath(imageName)
    image = cv2.imread(imagePath)
   
    window_name = imageName

    image = downsize_to_youtube_thumbnail(image)
    dimensions = image.shape
    imageHeight,imageWidth,_= dimensions

    #Title
    val = "HELLO TO THIS WORLD"
    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = FONT_SCALE_FACTOR * imageHeight
    color_white = (255, 255, 255)
    color_black = (0,0,0)
    thickness = int(FONT_THICKNESS_FACTOR * imageHeight * ALPHA)
    org= (int(imageWidth*ALPHA/4),int(imageHeight/2 * ALPHA))
    lineType = cv2.LINE_AA
    title_white = Text(val, font, fontScale, org, color_white, thickness, lineType)
    
    # imageWithText = cv2.putText(image, title_white.getVal(), title_white.getOrg(), title_white.getFont(), title_white.getFontScale(), title_white.getColor(), title_white.getThickness(), title_white.getLineType())


    #--------------------------Custom Font--------------------------------
    fontPath = getFontPath("bebas/Bebas-Regular.ttf")
    font_bebas = ImageFont.truetype(fontPath, int(CUSTOM_FONT_SCALE_FACTOR * imageHeight))
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text(title_white.getOrg(),  title_white.getVal(), font = font_bebas, fill = title_white.getColor())
    img = np.array(img_pil)
    #---------------------------------------------------------------------


    cv2.imshow(window_name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()