import os
import shutil

names = os.listdir('./bach/midiclassics/')
names.remove('.DS_Store')

for name in names:
    p = './bach/midiclassics/' + name
    subs = os.listdir(p)
    for sub in subs:
        if os.path.isdir(p + '/' + sub):
            files = os.listdir(p + '/' + sub)
            for f in files:
                shutil.move(p + '/' + sub + '/' + f,  p)
            shutil.rmtree(p + '/' + sub)