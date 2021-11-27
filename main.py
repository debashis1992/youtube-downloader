from pytube import YouTube, StreamQuery

link = input("Enter link: ")
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
            ys = streams.filter(type="video", progressive=True).get_by_itag(itag)

        ys.download(output_path="./downloads/")
    except Exception as e:
        print(e)


audio_codec = input("Enter only audio (Y/N): ") == "Y"
format_type = None
if audio_codec:
    format_type = "audio"
    itag = audio_streams_li.filter(abr = "128kbps")[0].itag
else:
    format_type = "video"
    available_formats = video_streams_li.filter(progressive=True)
    print(f"Available resolutions: {available_formats}")
    res_dict = {index:format for index,format in enumerate(available_formats)}
    print(res_dict)
    res_index = int(input("Enter resolution index: "))
    res = res_dict[res_index]
    itag = res.itag

download(yt.streams, itag, format_type)
