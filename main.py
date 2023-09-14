import random


class Pixel:
    possibleColors = ['B', 'W', 'G']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(Pixel.possibleColors)
    
    def toString(self):
        return self.color

    def isAdjacentTo(self, other):
        return abs(self.x - other.x) == 1 or abs(self.y - other.y) == 1

class Image:
    def __init__(self, size):
        self.size = size
        self.pixels = []
        for y in range(size):
            for x in range(size):
                self.pixels.append(Pixel(x, y))
    
    def getPixel(self, x, y):
        for pixel in self.pixels:
            if pixel.x == x and pixel.y == y:
                 return pixel
        
    def toString(self):
        toReturn = ""
        for y in range(self.size):
            for x in range(self.size):
                pixel = self.getPixel(x, y)
                toReturn += pixel.toString() + " "
            toReturn += "\n"
        return toReturn
        
    def setAdjacentPixelsToColor(self, targetPixel, originalColor, targetColor):
        adjacentPixels = []
        for pixel in self.pixels:
            if pixel.color == originalColor:
                if pixel.isAdjacentTo(targetPixel):
                    adjacentPixels.append(pixel)
                    pixel.color = targetColor
                    # print("Changed color of adjacent pixel from " + originalColor + " to " + pixel.color)
        # print("Found " + str(len(adjacentPixels)) + " adjacent pixels.")
        return adjacentPixels

contiguousInterpretation = False

image = Image(5)
print("Before:\n" + image.toString())

# input
targetX = 2
targetY = 2

targetColor = 'P'

targetPixel = image.getPixel(targetX, targetY)
originalColor = targetPixel.color
targetPixel.color = targetColor
# print("Changed color of target pixel from " + originalColor + " to " + targetPixel.color)
adjacentPixels = image.setAdjacentPixelsToColor(targetPixel, originalColor, targetColor)

if contiguousInterpretation:
    for i in range(image.size):
        toAppend = []
        for ap in adjacentPixels:
            toAppend.append(image.setAdjacentPixelsToColor(ap, originalColor, targetColor))
        adjacentPixels.append(toAppend)


print("After:\n" + image.toString() + "\n")