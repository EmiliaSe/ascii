from PIL import Image
import os, sys


def openImage():
    #Check if valid file
    filename = input('please enter full path to image file: ')
    if not os.path.isfile(filename):
        filename = input('please enter valid file: ')
    im = Image.open(filename)
    # print(im.format, im.size, im.mode)
    # w,h = im.size
    # print('width: '+str(w) )
    # print('height: ' +str(h))
    return im
   

def makePixelMatrix(im):
    w,h = im.size
    pixels = list(im.getdata())
    return [pixels[i:i+w] for i in range(0, w*h, w)]
    
def makeBrightnessMatrix(pixels, option): #option: 1 for average, 2 for lightness, 3 for luminosity
    matrix = []
    for row in pixels:
        newrow = []
        for pi in row:
            if (option == 1):
                newrow.append((pi[0]+pi[1]+pi[2])/3)
            elif (option ==2):
                newrow.append((max(pi)+min(pi))/2)
            else:
                newrow.append(0.21*pi[0]+0.72*pi[1]+0.07*pi[2])    
                
        matrix.append(newrow)   
    return matrix 

def toASCII(intensity_matrix):
    asciiChars ='"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"'
    asciiMatrix = []
    for row in intensity_matrix:
        asciiRow = []
        for pi in row:
            value = int(pi/255*len(asciiChars))-1
            asciiRow.append(asciiChars[value])
        asciiMatrix.append(asciiRow)
    return asciiMatrix    

def printFormatASCII(aMatrix):
    for row in aMatrix:
        for p in row:
            print(p,end='')
        print('\n')   

def saveToFile(filename, aMatrix):
    f = open(filename, 'w')
    for row in aMatrix:
        for p in row:
            f.write(p+p+p)
        f.write('\n')
    f.close()        


def main():
   im = openImage()
   pixels = makePixelMatrix(im)
   inten_matrix = makeBrightnessMatrix(pixels, 3)
   aMatrix = toASCII(inten_matrix)
   printFormatASCII(aMatrix)
   saveToFile('test2.txt', aMatrix)



if __name__ == "__main__":
    main()