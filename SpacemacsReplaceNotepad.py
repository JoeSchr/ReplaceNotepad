#!/usr/bin/python2
### CONFIG
## Open Regedit
## In "HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
## Add:
## Debugger (REG_SZ) : pyw "C:\Path\To\gVimReplaceNotepad\gVimReplaceNotepad.py" -Z

import subprocess,os,sys, getopt
bin_path = "C:/Program Files/emacs/bin/emacsclientw.exe"
def main(argv):
    inputfile = None
    vimargs = [os.path.normpath(bin_path), "-cna=runemacs"]
    try:
       opts, args = getopt.getopt(argv,"hZ:")
    except getopt.GetoptError:
        print 'ReplaceNotepad.py [-Z ignoredThis pathToFile] Arguments:', argv
        opts = []
    for opt, arg in opts:
        if opt == '-h':
           print 'ReplaceNotepad.py -Z ignoredThis pathToFile Arguments:', argv
           sys.exit()
        if opt == '-Z' and len(args) >= 1:
           inputfile = " ".join(args) # the rest it the pathtoopen with vim
           inputfile = os.path.normpath(inputfile)
           break

    #vimargs = [os.path.normpath(bin_path), "-cna=runemacs", inputfile]
    if not inputfile:
        inputfile = "new file"
    vimargs.append(inputfile)
    sys.exit(subprocess.call(vimargs,shell=True))
    # print 'Input file is "',inputfile
    # print 'Args is "',argv
    # raw_input("Press Enter to continue...")

if __name__ == "__main__":
    main(sys.argv[1:])
