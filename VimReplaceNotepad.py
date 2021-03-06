#!/usr/bin/python
### CONFIG
## In "HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
## Debugger :
#
#pythonw "C:\Path\To\gVimReplaceNotepad\gVimReplaceNotepad.py" -Z
import subprocess,os,sys, getopt
bin_path = "C:/Program Files (x86)/Vim/vim74/gvim.exe"
# bin_path = "C:/Program Files/emacs/bin/emacsclientw.exe"
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
           # old for gvim
           vimargs = [os.path.normpath(bin_path), "--remote-tab-silent",os.path.normpath(inputfile)]
           # vimargs = [os.path.normpath(bin_path), "-cna=runemacs",os.path.normpath(inputfile)]
           # full logging
           # vimargs = [os.path.normpath("C:/Program Files (x86)/Vim/vim74/gvim.exe"),os.path.normpath(inputfile),"--startuptime", "e:\\vim.log"]
           sys.exit(subprocess.call(vimargs,shell=True))
    # print 'Input file is "',inputfile
    # print 'Args is "',argv
    # raw_input("Press Enter to continue...")

if __name__ == "__main__":
    main(sys.argv[1:])
