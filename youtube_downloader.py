youtube_downloader.py
from pytube import YouTube

link = input("Link = ")
yt_1 = YouTube(link)

print(yt_1.title)
print(yt_1.thumbnail_url)
videos = yt_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("Enter: "))
videos[strm].download()
print("Successfully") 
