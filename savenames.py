#!/usr/bin/python
from main import *
a = Playlists()
a.call_refresh()
ini = open("../../playlists.ini", 'wt')
index = 0
ini.write("[names]\n")
for s in a.playlistNames:
   ini.write(str(index) + " = \"" + s + "\"\n")
   index += 1

index = 0
ini.write("[URI]\n")
for s in a.playlistURI:
    ini.write(str(index) + " = \"" + s + "\"\n")
    index += 1
