import cv2
from Text import Text


BASEPATH = "./assets/baseImage/"


def getImagePath(imageName):
    return BASEPATH+imageName

if __name__ == "__main__":
    imageName = "sunflower.jpg"
    # imageName = "Little_Joys.jpeg"
    imagePath = getImagePath(imageName)
    image = cv2.imread(imagePath)
   
    window_name = imageName

    dimensions = image.shape
    imageHeight, imageWidth, _= dimensions
    print("image1 size: ", imageHeight)
    
    # #------------image2--------------
    # imageName2 = "Little_Joys.jpeg"
    # image2 = cv2.imread(getImagePath(imageName2))
    # image2Dimensions = image2.shape
    # print("image2 size: ", image2Dimensions[0])
    #  #---------------------------------
  


    #Title Val
    val = "HELLO"
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 5 if imageHeight < 1000 else 50
    org = (int(imageHeight/2), int(imageWidth/2))
    color_white = (255, 255, 255)
    color_black = (0,0,0)
    thickness = 20 if imageHeight < 1000 else 75
    lineType = cv2.LINE_AA
    title_white = Text(val, font, fontScale, org, color_white, thickness, lineType)

    imageWithText = cv2.putText(image, title_white.getVal(), title_white.getOrg(), title_white.getFont(), title_white.getFontScale(), title_white.getColor(), title_white.getThickness(), title_white.getLineType())


    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()