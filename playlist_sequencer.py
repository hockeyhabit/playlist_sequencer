#! /usr/bin/env python

import os.path
import time
import sys
import os
import glob
import operator
import shutil
import re, string

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
fileHash = {}  

def move(src, dest):
    shutil.move(src, dest)

# creates a three letter string based on the number provided
# example: innum = 7, returns: aag
def CountNumToAlphaString(innum):
    calcvalue = innum / (26 * 26)
    firstLetter = alpha[calcvalue]

    innum -= calcvalue * (26 * 26) 
    calcvalue = innum / 26
    secondLetter = alpha[calcvalue]

    innum -= calcvalue * (26)
    thirdLetter = alpha[innum]

    return firstLetter+secondLetter+thirdLetter

# this function will touch a file
def TouchFile(fname):
    try:
        os.utime(fname, None)
    except:
        open(fname, 'a').close()

def FilePathExt(fullfilepath):
    path, filename = os.path.split(fullfilepath)
    filebase, fileext = os.path.splitext(filename)
    if (len(path) > 0):
        path += "/"
    return path, filename, filebase, fileext

# this function will get all numbers from a string and return it as an array, else it returns 0
# it is expected that this function return either one or two values for one or two values in the filename
def GetNumbersFromString(str):
    try:
        path, filename, filebase, fileext = FilePathExt(str)
        numberArray = [int(x.group()) for x in re.finditer(r'\d+', filebase)]
        return numberArray
    except:
        return [0]

# this function will get a number from a string, right now it only handles the first number in the string
# this function assumes that there will be a number in the string, else it returns 0
def GetNumberFromString(str):
    try:
        stringNumber = re.search(r'\d+', str).group()
        return int(stringNumber)
    except:
        return 0

# given an array of filenames, this function will return the smallest and largest values of the integers in the filenames
def GetMinMaxArray(listOfFiles):
    min1 = -1
    max1 = -1
    min2 = -1
    max2 = -1
    for f in listOfFiles:
        numberArray = GetNumbersFromString(f)
        if (len(numberArray) >= 1):
            number = numberArray[0]
            if (min1 == -1):
                min1 = number
                max1 = number
            if (number < min1):
                min1 = number
            if (number > max1):
                max1 = number
        if (len(numberArray) >= 2):
            number = numberArray[1]
            if (min2 == -1):
                min2 = number
                max2 = number
            if (number < min2):
                min2 = number
            if (number > max2):
                max2 = number
    return (min1,max1,min2,max2)

# given an array of filenames, this function will return the smallest and largest value of the integers in the filenames
def GetMinMax(listOfFiles):
    min = -1
    max = -1
    for f in listOfFiles:
        number = GetNumberFromString(f)
        if (min == -1):
            min = number
            max = number

        if (number < min):
            min = number
        if (number > max):
            max = number

    return (min,max)

# this function will replace in a string any integer with %d
# this will replace EACH int character with '%d', '1' is one int char, '11' is two int chars
def IntToPctd(s, chars):
    return re.sub('[%s]' % chars, '%d', s)
      

# this function will replace in a string any integer with %d
# this will replace an int with %d
def IntToPctd2(fullfilepath):
    pattern = "(\d+)"
    path, filename, filebase, fileext = FilePathExt(fullfilepath)
    updatedFileBase = re.sub(pattern, '%d', filebase)
    return path + updatedFileBase + fileext

def main(indir):

    print "processing..."
    listOfFiles = glob.glob(indir+"/*.*")

    minMaxArray = GetMinMaxArray(listOfFiles)
    generic_filename = IntToPctd2(listOfFiles[0])

    # iterate through the range of files and touch each file so that they are in order
    count = 0
    min1 = minMaxArray[0]
    max1 = minMaxArray[1]
    min2 = minMaxArray[2]
    max2 = minMaxArray[3]
    for x in range(min1, max1+1):
        for y in range(min2, max2+1):  # for single int filenames, this will be range (-1, -1+1) which is a range of one...so... it becomes a "pass"
            if (min2 == -1):
                numbered_filename = generic_filename % x
            else:
                numbered_filename = generic_filename % (x, y)
            try:
                if numbered_filename in listOfFiles:
                    fileHash[numbered_filename] = count
                    count += 1
            except ValueError:
                pass # or scream: thing not in listOfFiles!
            except AttributeError:
                pass # call security, listOfFiles not quacking like a list!

    # make fileHash based on filedate/time
    #for f in listOfFiles:
    #    fileHash[f] = os.path.getmtime(f)

    # create sorted list based on hash key
    sortedFilelist = sorted(fileHash.iteritems(), key=operator.itemgetter(1))

    filecount = 0
    for sortedFile in sortedFilelist:
        path, filename, filebase, fileext = FilePathExt(sortedFile[0])
        newfilename = path + CountNumToAlphaString(filecount)+"_"+filename
        #print "copy/move " + "(" + sortedFile[0] + "," + newfilename
        #shutil.copyfile(sortedFile[0], newfilename)
        shutil.move(sortedFile[0], newfilename)
        filecount += 1

    print "Renamed " + str(filecount) + " files"


if __name__ == "__main__": 
    if (len(sys.argv) != 2):
        print "args wrong, try: "  + sys.argv[0] + " <dirname>"
        sys.exit(-1)
          
    main(sys.argv[1])
