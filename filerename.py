
import os.path
import time
import sys
import os
import glob
import operator
import shutil

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
fileHash = {}  

def move(src, dest):
    shutil.move(src, dest)

def NumToString(innum):
    calcvalue = innum / (26 * 26)
    firstLetter = alpha[calcvalue]
    innum -= calcvalue * (26 * 26) 

    calcvalue = innum / 26
    secondLetter = alpha[calcvalue]
    innum -= calcvalue * (26)

    thirdLetter = alpha[innum]
    return firstLetter+secondLetter+thirdLetter

def main(indir):

    print "list of all files"
    listOfFiles = glob.glob(indir+"/*.*")

    for f in listOfFiles:
        print f
        fileHash[f] = os.path.getmtime(f)

    sorted_x = sorted(fileHash.iteritems(), key=operator.itemgetter(1))

    filecount = 0
    for sorted_f in sorted_x:
        fileprefix = NumToString(filecount)
        (dirName, fileName) = os.path.split(sorted_f[0])
        newfilename = NumToString(filecount)+"_"+fileName
        print "copy/move " + "(" + sorted_f[0] +","+ dirName + "/" + newfilename+ ")"
        shutil.copyfile(sorted_f[0], dirName + "/" + newfilename)
        #shutil.move(sorted_f[0], dirName + "/" + newfilename)
        filecount += 1


#file = "filerename.py"
#print "mtime modified: %d" % os.path.getmtime(file)
#print "last modified: %s" % time.ctime(os.path.getmtime(file))
#print "created: %s" % time.ctime(os.path.getctime(file))
#
#import os, time
#(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
#print "last modified: %s" % time.ctime(mtime)



if __name__ == "__main__": 
    if (len(sys.argv) != 2):
        print "args wrong, try: "  + sys.argv[0] + " <dirname>"
        sys.exit(-1)
          
    main(sys.argv[1])
