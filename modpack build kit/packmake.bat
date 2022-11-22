@ECHO off
echo %CD%
set/p again="(re)install mods? "
    if /i "%again%" == "yes" py reset.py & py install.py modlist.txt
    if /i "%again%" == "y" py reset.py & py install.py modlist.txt
packwiz mr export

timeout /t -1