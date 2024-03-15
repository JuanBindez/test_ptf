from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Playlist
from pytubefix.cli import on_progress
from pytubefix import YouTube
from pytubefix import Channel


def download_mp4():
    try:
        url = "https://www.youtube.com/watch?v=tAGnKpE4NCI"
        
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        
        ys = yt.streams.get_highest_resolution()
        ys.download()
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)


def download_mp3():
    try:
        url = "https://www.youtube.com/watch?v=tAGnKpE4NCI"
        
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        
        ys = yt.streams.get_audio_only()
        ys.download(mp3=True)
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)


def download_playlist():
    try:
        url = "https://www.youtube.com/watch?v=8IZR7_9uyos&list=PLJvQXRgtxlum8BrBk16tRspIza8q8gjpR"

        pl = Playlist(url)

        for video in pl.videos:
            ys = video.streams.get_audio_only()
            ys.download(mp3=True) # pass the parameter mp3=True to save in .mp3
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)


def subtitles_test():
    try:
        yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
        subtitles = yt.captions

        print(subtitles)
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)


def subtitle_tracks():
    try:
        yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

        caption = yt.captions.get_by_language_code('en')
        print(caption.generate_srt_captions())
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)

def save_captions():
    try:
        yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

        caption = yt.captions.get_by_language_code('en')
        caption.save_captions("captions.txt")
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)

def channels_names():
    try:
        c = Channel("https://www.youtube.com/@ProgrammingKnowledge/featured")

        print(f'Channel name: {c.channel_name}')
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)

def downloads_channel():
    try:
        c = Channel("https://www.youtube.com/@juanbindez2033")

        print(f'Downloading videos by: {c.channel_name}')

        for video in c.videos:
            download = video.streams.get_highest_resolution().download()
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)


def chapters():
    try:
        url = 'https://www.youtube.com/watch?v=kRzgCylePjk'

        yt = YouTube(url)
        print(yt.chapters)
    except Exception as error:
        print("Algo deu errado: \n\n\n", error)


if __name__ == "__main__":
    download_mp4()
    download_mp3()
    download_playlist()
    subtitles_test()
    subtitle_tracks()
    save_captions()
    channels_names()
    downloads_channel()
    chapters()


