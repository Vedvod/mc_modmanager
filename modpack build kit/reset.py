import os, shutil, sys

for root, dirs, files in os.walk('mods/'):
    for f in files:
        if f.endswith("toml"): os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))
for root, dirs, files in os.walk('resourcepacks/'):
    for f in files:
        if f.endswith("toml"): os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))
(index := open("index.toml", "w")).write('''hash-format = "sha256"''')
index.close()
#input("Press Enter to exit. . .")