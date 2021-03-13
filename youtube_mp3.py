# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:50:42 2021

@author: ASUS
"""

from pytube import Playlist as pt
from tqdm import tqdm
from pytube import YouTube as yt
import os,glob
import pytube.exceptions as ex
var1 = pt("https://www.youtube.com/playlist?list=PL2Iefjpn3w-Mg_QIF6Eivl_Fl1XshaSSQ")


    


#where to save 
SAVE_PATH = r"C:\Users\ASUS\music" #to_do 
os.chdir(SAVE_PATH)

for i in tqdm(var1): 
    try: 
        x = yt(i)
    except ex.VideoUnavailable:
        print("cant download")
    else:
        print("downloading : {i} ")
        audio = x.streams.get_audio_only()
        audio.download(r"C:\Users\ASUS\music")
for fi in glob.glob("*.mp4"):
   os.rename(fi, fi[:-3] + "mp3")
        
print("completed")



