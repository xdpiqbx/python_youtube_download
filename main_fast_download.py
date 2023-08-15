import os

from pathlib import Path
from pytube import YouTube

data = Path("./data")
done = Path("./done")
downloads = Path("./downloads")

dir_list = sorted(os.listdir(data))

for data_file in dir_list:
    print(data_file)  # some_file.txt
    index = 0
    with open(data.joinpath(data_file)) as file:
        line = file.readline()
        while line:
            index += 1
            print(f"{index}: {line.strip()}")  # 1: https://www.youtube.com/watch?v=dkfjgh

            yt = YouTube(line.strip())

            print(f"{yt.title}\nVideo download in process ...")
            video_file = yt.streams.get_highest_resolution().download(
                output_path=str(downloads.joinpath(data_file[:-4])),
                filename_prefix=f"{index:03}_"
            )

            line = file.readline()

    os.replace(data.joinpath(data_file), done.joinpath(data_file))
