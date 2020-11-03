# Brendan McGlynn
# CSEC 472 - Lab 3
# Group 2
# Method 4

import skimage

import numpy as np # computations in the mse command
from PIL import Image, ImageChops, ImageStat  # Image Library

import glob # Import file paths
import mahotas
import pylab
import random # shuffle array
import math

test = []
train = []
imageDetails_list = []
finalTestCheck = []



def difference(imageA, imageB):
    h = ImageChops.difference(imageA, imageB).histogram()
    val = math.sqrt(sum(h*(i**2) for i, h in enumerate(h)) / (float(imageA.size[0]) * imageB.size[1]))
    return val/100

def main():
    # Add images to testing
    for finger in glob.glob(
            'C:/Users/brend/Desktop/RIT/Senior Year/Fall Semester/Auth/mod 4/lab/groupStuff/jake/test/*'):
        if finger.endswith('.txt'):
            imageDetails_list.append(finger[-12:])
        else:
            im = Image.open(finger)
            finalTestCheck.append(finger[-12:])
            test.append(im)

    # Add images to training
    for finger2 in glob.glob(
            'C:/Users/brend/Desktop/RIT/Senior Year/Fall Semester/Auth/mod 4/lab/groupStuff/jake/train/*'):
            im2 = Image.open(finger2)
            train.append(im2)

    trainlength = len(train)
    print("Number of train images:", trainlength)

    testlength = len(test)
    print("Number of test images:", testlength)

    #print(test[0])

    #Image._show(train[0])
    #Image._show(train[1])
    #Image._show(train[2])

    # img = Image._show(image_list[0])
    # img.show()

    # print(imageDetails_list[0])
    # print(imageDetails_list[1])

    for everyFinger in train:
        test.append(everyFinger)
        #print()

   # print("new test Length - ", newLength)

    trainNum = 0
    random.shuffle(test)
    newLength = len(test)

    while trainNum < len(train): # go thru each train item
        testNum = 0
        while testNum < len(test): # go thru each test item
            image1 = train[trainNum]
            image2 = test[testNum]
            valid = difference(image1,image2)
            #print("counter - ", testNum)
            if valid < 0.40: # 0 is more similar
                #Image._show(test[testNum])
                test.pop(testNum)
                print("train num: ", trainNum)
                print("test num:  ", testNum)
                testNum=0
                trainNum+=1
                if trainNum >= len(train):
                    break
            else:
                #do next iteration
                testNum += 1
                if(testNum >= len(test)):
                    testNum = 0
                    trainNum += 1
                    break


    print("final length of test - ", len(test))
    numCorrect = 0
    for item in test:
        print("File Name:", item.filename[-12:])
        fingerPrintNum = int(item.filename[-11:-7])
        print("Finger Print Number:", fingerPrintNum)
        if(fingerPrintNum > 1500):
            numCorrect += 1
    print("Number of correct fingerprints: " + str(numCorrect) + "/500")

if __name__ == '__main__':
   main()