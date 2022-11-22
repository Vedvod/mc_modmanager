import os, sys, time
print(sys.argv); time.sleep(3)
if len(sys.argv) > 1:
  modlist="".join(["https://modrinth.com/mod/fabric-api\n", "https://modrinth.com/mod/modmenu\n"] + open(sys.argv[1]).readlines())
else: modlist="""https://modrinth.com/mod/fabric-api
Server Only
    QoL/client Features
        Server Optimisation
            https://modrinth.com/mod/lithium
            https://modrinth.com/mod/ferrite-core
            https://modrinth.com/mod/notenoughcrashes
            https://modrinth.com/mod/tabtps
            https://modrinth.com/mod/mixin-conflict-helper
            https://modrinth.com/mod/clean-logs
            https://modrinth.com/mod/styledplayerlist
            https://modrinth.com/mod/no-chat-reports
            https://modrinth.com/mod/automodpack
            https://www.curseforge.com/minecraft/mc-mods/distant-horizons
            https://www.curseforge.com/minecraft/mc-mods/attributefix
    Player Interactions
            https://modrinth.com/mod/server-chat-history
            https://modrinth.com/mod/simple-voice-chat
            https://modrinth.com/mod/sound-physics-remastered
            https://modrinth.com/mod/voice-chat-interaction
            https://modrinth.com/mod/sleep-warp
            https://modrinth.com/mod/deathlog
            https://modrinth.com/mod/enchantment-lore"""
print(modlist)

from_both = lambda modlist: [x.replace("https://modrinth.com/mod/", "").replace("https://www.curseforge.com/minecraft/mc-mods/", "")
                             for x in modlist.replace(" ", "").split("\n") if x.startswith("https")]
from_mr = lambda modlist: [x.replace("https://modrinth.com/mod/", "") 
                           for x in modlist.replace(" ", "").split("\n") if x.startswith("https://modrinth")]
from_cf = lambda modlist: {x.replace("https://www.curseforge.com/minecraft/mc-mods/", ""): x 
                           for x in modlist.replace(" ", "").split("\n") if x.startswith("https://www.curseforge")}

def mod_install(list_of_mods): # function to install mods given modlist
  for i in (["pack.toml"]): # can be extended to other (?)
    print(f"Now searching for {i}:\n{list_of_mods}")
    print(f"cf: {[x for x in from_cf(list_of_mods)]}") # display curseforge mods
    print(f"mr: {from_mr(list_of_mods)}") # display modrinth mods
    for n, mod in enumerate(cf_mods := from_cf(list_of_mods)): # curseforge mod loading
      l = len(cf_mods)
      print(f"{n}/{l}:", end = " ")
      sys.stdout.flush()
      if os.system(rf'''packwiz cf install {cf_mods[mod]} --pack-file {i}''') == 0: # calling packwiz on mod
        list_of_mods = list_of_mods.replace(f"https://www.curseforge.com/minecraft/mc-mods/{mod}", "") # removing mod from to load
    for n, mod in enumerate(mr_mods := from_mr(list_of_mods)): # modrinth mod loading
      l = len(mr_mods)
      print(f"{n}/{l}:", end = " ")
      if os.system(rf'''packwiz mr install {mod} --pack-file {i}''') == 0: # calling packwiz on mod
        list_of_mods = list_of_mods.replace(f"https://modrinth.com/mod/{mod}", "") # removing mod from to load
  print(list_of_mods) # output should be empty of URLs, otherwise highlights problematic mods

mod_install(modlist)
#input("Press Enter to exit. . .")

