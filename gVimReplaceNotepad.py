#!/usr/bin/python

import subprocess,os,sys, getopt

def main(argv):
    inputfile = ''
    try:
       opts, args = getopt.getopt(argv,"hZ:")
    except getopt.GetoptError:
        print 'gVimReplaceNotepad.py -Z ignoredThis pathToFile Arguments:', argv
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
           print 'gVimReplaceNotepad.py -Z ignoredThis pathToFile Arguments:', argv
           sys.exit()
        elif opt == '-Z' and len(args) >= 1: 
           inputfile = " ".join(args) # the rest it the pathtoopen with vim 
           vimargs = [os.path.normpath("C:/Program Files (x86)/Vim/vim74/gvim.exe"),os.path.normpath(inputfile)]
           sys.exit(subprocess.call(vimargs,shell=True))
    # print 'Input file is "',inputfile
    # print 'Args is "',argv
    # raw_input("Press Enter to continue...")

if __name__ == "__main__":
    main(sys.argv[1:])
