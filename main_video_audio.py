import os
import ffmpeg
from pathlib import Path
from pytube import YouTube
from time import sleep

downloads = Path("./downloads")

index = 0
with open("data/001_js.txt") as file:
    line = file.readline()
    while line:
        index += 1

        yt = YouTube(line.strip())

        print(f"{yt.title}\nVideo download in process ...\n")
        video_file = yt.streams.get_highest_resolution().download(
            output_path=str(downloads),
            filename_prefix=f"{index:03}_video_"
        )

        # video_file = yt.streams.filter(
        #     file_extension='mp4',
        #     progressive=False,
        #     res="1080p"
        # ).first().download(output_path=downloads, filename_prefix=f"{index:03}_video_")

        # print(f"{yt.title}\nAudio download in process ...\n")
        # audio_file = yt.streams.get_audio_only().download(
        #     output_path=str(downloads),
        #     filename_prefix=f"{index:03}_audio_"
        # )

        # audio_file = yt.streams.filter(
        #     only_audio=True,
        #     progressive=False,
        #     abr="128kbps",
        # ).first().download(output_path=downloads, filename_prefix=f"{index:03}_audio_")

        # dir_list = sorted(os.listdir(downloads))
        #
        # for audio, video in zip(dir_list, dir_list[1:]):
        #     if audio[:3] == video[:3]:
        #
        #         input_video = ffmpeg.input(str(downloads / video))
        #         input_audio = ffmpeg.input(str(downloads / audio))
        #
        #         print(f"{video[10:]}\nFFmpeg in process ...\n")
        #         file_name = f"{downloads}/{index:03}_{video[10:]}"
        #
        #         ffmpeg.output(input_audio, input_video, file_name, format='mp4').run()
        #
        #         os.remove(str(downloads / audio))
        #         os.remove(str(downloads / video))

        line = file.readline()
