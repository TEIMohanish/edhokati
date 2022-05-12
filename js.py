import requests, json
import os, sys
import argparse
import subprocess
import pathlib
import shutil
import time

FILE_DIRECTORY=str(pathlib.Path(__file__).parent.absolute())
TEMPORARY_PATH = FILE_DIRECTORY+"/cache"
OUTPUT_PATH = FILE_DIRECTORY+"/output"
ENCODES = FILE_DIRECTORY+"/encodes"
ACCOUNT = FILE_DIRECTORY+"/accounts"


# define paths
currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)
ytdl_path = "yt-dlp"
filedir=str(pathlib.Path(__file__).parent.absolute())
 
def divider():
	print ('-' * shutil.get_terminal_size().columns)

Request_URL = "https://prod.media.jio.com/apis/common/v3/playbackrights/get/"
Meta_URL = "https://prod.media.jio.com/apis/common/v3/metamore/get/"
First = "https://jiobeats.cdn.jio.com/vod/_definst_/smil:"
Second = ".smil/chunklist.m3u8"
arguments = argparse.ArgumentParser()
arguments.add_argument("-id", "--id", dest="id", help="content id ")
arguments.add_argument("-q", "--quality", dest="res", help="quality") 
arguments.add_argument("-o", "--output", dest="output", help="file")
args = arguments.parse_args()
VideoID = args.id
fileName = args.res


def get_metadata(VideoID):
    url = Meta_URL + VideoID
    print(url) 
    test = input ('Enter thumb: ')
    m3u8 = First + test + Second
    outputpath = OUTPUT_PATH + '/' + f"{fileName}"
    print(f'link: {m3u8}') 
    print ("Shakthi Hero Ikkada")
    os.system('yt-dlp --external-downloader aria2c --no-warnings --allow-unplayable-formats --no-check-certificate -F "%s"'%m3u8)
    divider()
    VIDEO_ID = input("ENTER VIDEO_ID (Press Enter for Best): ")
    if VIDEO_ID == "":
           AUDIO_ID = "ba"
    divider()
    os.system(f'yt-dlp --no-warnings --external-downloader aria2c --allow-unplayable-formats --user-agent "JioOnDemand/1.5.2.1 (Linux;Android 4.4.2)" -f {VIDEO_ID} "{m3u8}" -o thelidhu.mp4')
    os.rename(f'thelidhu.mp4', outputpath)
    #print ("\nSuccessfully downloaded the stream!") 

def subtitles():
    test = input ('Enter thumb: ')
    m3u8 = First + test + Second
    print("Downloading Subtitles")
    os.system(f'yt-dlp --write-subs --convert-sub srt --skip-download --external-downloader aria2c --verbose --allow-u "%s" -o %s/decrypted_subs'%(m3u8,OUTPUT_PATH))

def merge_content():
	divider()
	accounts = ACCOUNT + '/' + f"{fileName}"
	outputpath = OUTPUT_PATH + '/' + f"{fileName}"
	print("Merging Files and Processing..")
	time.sleep(2)
	os.system('ffmpeg -i %s -i %s/decrypted_subs.eng.srt -preset ultrafast -hide_banner -c:v copy -c:a copy -c:s copy %s'%(outputpath,OUTPUT_PATH,outputpath))



def trackname():
        outputpath = OUTPUT_PATH + '/' + f"{fileName}"
        encodespath = ENCODES + '/' + f"{fileName}"
        divider()
        os.system('ffmpeg -i %s -hide_banner -map 0:v -map 0:a -metadata title="TroopOriginals" -metadata:s:v title="TroopOriginals" -metadata:s:a title="TroopOriginals" -codec copy %s/thelidhu.mp4 && mv %s/thelidhu.mp4 %s'%(outputpath,OUTPUT_PATH,OUTPUT_PATH,encodespath))


def rclone():
    print("Aagu Ra Nakka Pumka")
    encodespath =  ENCODES + '/' + f"{fileName}"
    subprocess.run(['rclone','move', encodespath,'wanda:troopdrive/jiosun'])
    print("SHAKTHI HERO THELUSA THAMMUDU NEEKU") 


get_metadata(VideoID)
divider()
trackname()
rclone()
