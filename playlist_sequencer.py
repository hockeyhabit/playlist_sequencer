#! /usr/bin/env python

import os.path
import time
import sys
import os
import glob
import operator
import shutil
import re, string


def move(src, dest):
    try:
        shutil.move(src, dest)
    except:
        print "Error moving file, check file perms"

# provides full access to path/filename/filebase/ext of entered filepath string
# it even corrects for empty path 
def FilePathExt(fullfilepath):
    path, filename = os.path.split(fullfilepath)
    filebase, fileext = os.path.splitext(filename)
    if (len(path) > 0):
        path += "/"
    return path, filename, filebase, fileext

# creates a three letter string based on the number provided
# example: innum = 7, returns: aag
def CountNumToAlphaString(innum):
    # list of alpha characters
    alpha = list(string.ascii_lowercase)

    calcvalue = innum / (26 * 26)
    firstLetter = alpha[calcvalue]

    innum -= calcvalue * (26 * 26)
    calcvalue = innum / 26
    secondLetter = alpha[calcvalue]

    innum -= calcvalue * (26)
    thirdLetter = alpha[innum]

    return firstLetter+secondLetter+thirdLetter

# this sort was inspired by this blog:
# http://nedbatchelder.com/blog/200712/human_sorting.html#comments
def nsort(l):
    return sorted(l, key=lambda a:zip(re.split("(\\d+)", a)[0::2], map(int, re.split("(\\d+)", a)[1::2])))

def main(indir):

    print "processing..."

    # get list of files to process
    listOfFiles = glob.glob(indir+"/*.*")

    # create sorted list of files
    sortedFilelist = nsort(listOfFiles)

    filecount = 0
    for sortedFile in sortedFilelist:
        path, filename, filebase, fileext = FilePathExt(sortedFile)
        newfilename = path + CountNumToAlphaString(filecount)+"_"+filename
        move(sortedFile, newfilename)
        filecount += 1

    print "Renamed " + str(filecount) + " files"


if __name__ == "__main__": 
    if (len(sys.argv) != 2):
        print "args wrong, use: "  + sys.argv[0] + " <dirname>"
        sys.exit(-1)
          
    main(sys.argv[1])
