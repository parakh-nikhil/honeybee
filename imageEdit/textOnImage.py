import cv2


if __name__ == "__main__":
    imageName = "sunflower.jpg"
    imagePath = "./assets/baseImage/%s" %(imageName)
    image = cv2.imread(imagePath)
    window_name = imageName

    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()