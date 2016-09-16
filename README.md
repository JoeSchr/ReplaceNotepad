ReplaceNotepad
==================

quick n dirty script to help me replacing notepad with gvim. it uses the debug switch -Z so it ignores the first argument (which would be "pathto/notepad.exe") and the opens gvim with what ever comes after it. 
regedit needed for it 
In "HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe"
ADD => Debugger : pythonw "C:\pathto\gVimReplaceNotepad.py" -Z

search "notepad2 replace notepad" or go to http://www.flos-freeware.ch/doc/notepad2-Replacement.html to unterstand more
