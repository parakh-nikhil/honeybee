import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

from Text import Text

ASSETS_PATH = "./assets/"
IMAGES_BASEPATH = ASSETS_PATH+"baseImage/"
FONTS_BASEPATH = ASSETS_PATH+"fonts/"
ALPHA = 0.6
FONT_SCALE_FACTOR = (2/720)
CUSTOM_FONT_SCALE_FACTOR = (75/720)
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

def add_text_to_img_using_custom_font(textConfig, fontPath, image):
    font_bebas = ImageFont.truetype(fontPath, int(CUSTOM_FONT_SCALE_FACTOR * imageHeight))
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text(textConfig.getOrg(),  textConfig.getVal(), font = font_bebas,fill = textConfig.getColor())

    img = np.array(img_pil)
    return img

def add_text_to_img_using_custom_font_with_shadow(textConfig, fontPath, image, shadow_color):
    space = 0
    font_bebas = ImageFont.truetype(fontPath, int(CUSTOM_FONT_SCALE_FACTOR * imageHeight))
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text(textConfig.getOrg(),  textConfig.getVal(), font = font_bebas, stroke_width = 5, spacing = space, fill = shadow_color)
    draw.text(textConfig.getOrg(),  textConfig.getVal(), font = font_bebas, stroke_width = 1, spacing = space, fill = textConfig.getColor())

    img = np.array(img_pil)
    return img

if __name__ == "__main__":
    images = ["sunflower.jpg",  "Little_Joys.jpeg"]
    imageName = images[0]
    imagePath = getImagePath(imageName)
    image = cv2.imread(imagePath)
   
    window_name = imageName.split(".")[0] if "." in imageName else imageName

    image = downsize_to_youtube_thumbnail(image)
    dimensions = image.shape
    imageHeight,imageWidth,_= dimensions

   #--------------------------Title--------------------------------
    val = "You generated this thumbnail"
    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = FONT_SCALE_FACTOR * imageHeight
    color_white = (255, 255, 255)
    color_black = (0,0,0)
    thickness = int(FONT_THICKNESS_FACTOR * imageHeight * ALPHA)
    org= (int(imageWidth*ALPHA/4),int(imageHeight/2 * ALPHA))
    lineType = cv2.LINE_AA
    title_white = Text(val, font, fontScale, org, color_white, thickness, lineType)
    #---------------------------------------------------------------------



    #--------------------------Custom Font--------------------------------
    fontPath = getFontPath("bebas/Bebas-Regular.ttf")
    # img = add_text_to_img_using_custom_font(title_white, fontPath, image)
    img = add_text_to_img_using_custom_font_with_shadow(title_white, fontPath, image, (0,0,0))
    #---------------------------------------------------------------------

    cv2.imshow(window_name, img)
    cv2.waitKey(10000) #waits 10 seconds before closing
    cv2.destroyAllWindows()