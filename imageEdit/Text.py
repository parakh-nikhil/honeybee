import cv2
class Text:
    def __init__(self, val, font = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 5, org = (0,0), color = (0,0,0), thickness = 2, lineType = cv2.LINE_AA):
        self.__val = val
        self.__font = font
        self.__fontScale = fontScale
        self.__org = org
        self.__color = color
        self.__thickness = thickness
        self.__lineType = lineType;

    def getVal(self):
        return self.__val
    
    def setVal(self, newVal):
        self.__val= newVal

    def getFont(self):
        return self.__font
    
    def setFont(self, newFont):
        self.__font = newFont

    def getFontScale(self):
        return self.__fontScale
    
    def setFontScale(self, newFontScale):
        self.__fontScale = newFontScale

    def getOrg(self):
        return self.__org
    
    def setOrg(self, newOrg):
        self.__org= newOrg

    def getColor(self):
        return self.__color
    
    def setColor(self, newColor):
        self.__color = newColor

    def getThickness(self):
        return self.__thickness
    
    def setThickness(self, newThickness):
        self.__thickness = newThickness

    def getLineType(self):
        return self.__lineType
    
    def setLineType(self, newlineType):
        self.__lineType = newlineType

    def __str__(self) -> str:
        return self.__val