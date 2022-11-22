ok so first things first, 
REQUIREMENTS: 
    https://go.dev/doc/install
    https://multimc.org/#Download (or whichever installer you want)
    https://www.python.org/downloads/ python momento

STEP 1: install all dependencies, place go installer download in THIS folder
STEP 2: run RUNME.bat
this should install packwiz, you should install the other things as well

THEN in modpack build kit folder:
    Look through modlist.txt, this is the file from which mods are pulled
        if you want to prevent the packer packing a mod, add some character to the start of the line
            eg (https://modrinth.com/mod/) --> (#https://modrinth.com/mod/)
            or you could just remove the mod entry entirely I guess
        to add a mod just chuck its modrinth URL somewhere in the file
    If you want to add your options and servers files from a current install, just copy them into the folder
        same applies to resource and shaderpacks and mod configs (and even mods)
    Then, run packmake.bat and answer yes to the question
        answer no for future repacks if you have not changed the files
    finally, through your chosen launcher install the produced mrpack 