import cv2
from Text import Text

if __name__ == "__main__":
    imageName = "sunflower.jpg"
    imagePath = "./assets/baseImage/%s" %(imageName)
    image = cv2.imread(imagePath)
    window_name = imageName

    #Title Val
    val = "HELLO"
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 5
    org = (2000, 2000)
    color_white = (255, 255, 255)
    color_black = (0,0,0)
    thickness = 20
    lineType = cv2.FILLED
    title_white = Text(val, font, fontScale, org, color_white, thickness, lineType)

    imageWithTextBG = cv2.putText(image, title_white.getVal(), title_white.getOrg(), title_white.getFont(), title_white.getFontScale(), title_white.getColor(), title_white.getThickness(), title_white.getLineType())


    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()