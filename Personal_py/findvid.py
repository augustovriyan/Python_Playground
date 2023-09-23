import os

def find_video_files(search_dirs, video_title):
    video_extensions = [".mkv", ".mp4", ".ts", ".webm"]
    for start_dir in search_dirs:
        for root, dirs, files in os.walk(start_dir):
            for file in files:
                if os.path.splitext(file)[1] in video_extensions:
                    if video_title.lower() in file.lower():
                        video_path = os.path.join(root, file)
                        print("Found:", video_path)

search_dirs = ["E:\\", "F:\\", "G:\\"]  # Enter the drive letters or paths to search
title_to_search = input("Enter the title of the video to search for: ")
find_video_files(search_dirs, title_to_search)
