from pytube import Playlist as pt
from tqdm import tqdm
from pytube import YouTube as yt
import os,glob
import pytube.exceptions as ex

import threading

    


#where to save 
SAVE_PATH = r"C:\Users\ASUS\music" #to_do 
os.chdir(SAVE_PATH)


def download_playlist(var1):
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
    return "Done"


if __name__ == "__main__":
    var1 = pt('https://www.youtube.com/watch?v=2sAzb3kraoQ&list=PL-oM5qTjmK2vxdTsj2Xghu5fjxhtuMaxo')
    t1 = threading.Thread(target=download_playlist, args=(var1,)) 
    t1.start()
    t1.join()from pytube import Playlist as pt
from tqdm import tqdm
from pytube import YouTube as yt
import os,glob
import pytube.exceptions as ex

import threading

    


#where to save 
SAVE_PATH = r"C:\Users\ASUS\music" #to_do 
os.chdir(SAVE_PATH)


def download_playlist(var1):
    for i in tqdm(var1): 
        try: 
            x = yt(i)
        except ex.VideoUnavailable:
            print("cant download")
        else:
            #print("downloading : {i} ")
            audio = x.streams.get_audio_only()
            audio.download(r"C:\Users\ASUS\music")
    for fi in glob.glob("*.mp4"):
       os.rename(fi, fi[:-3] + "mp3")
    return "Done"


if __name__ == "__main__":
    var1 = pt('https://www.youtube.com/watch?v=2sAzb3kraoQ&list=PL-oM5qTjmK2vxdTsj2Xghu5fjxhtuMaxo')
    t1 = threading.Thread(target=download_playlist, args=(var1,)) 
    t1.start()
    t1.join()
