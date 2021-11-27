from pytube import YouTube, StreamQuery

link = input("Enter link:")
yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"No. of views: {yt.views}")
print(f"Length of video: {yt.length}")
print(f"Rating: {yt.rating}")

video_streams_li = yt.streams.filter(type="video")
audio_streams_li = yt.streams.filter(type="audio")

print("Video streams:")
for stream in video_streams_li:
    print(stream)

print("Audio streams:")
for stream in audio_streams_li:
    print(stream)




def download(streams: StreamQuery, itag: int = None, type: str = None):
    try:
        if streams is None:
            raise Exception("No streams available")
        if type == "audio":
            ys = streams.filter(type="audio").get_by_itag(itag)
        else:
            ys = streams.filter(type="video").get_by_itag(itag)

        ys.download()
    except Exception as e:
        print(e)

download(yt.streams, 140, "audio")