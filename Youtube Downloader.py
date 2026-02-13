from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: yt.title")

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download() # Enter your folder location where in which you want the downloaded file to save in