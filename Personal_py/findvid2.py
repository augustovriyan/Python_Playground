#Here's an updated version of the function with loading progress added:

import os

def find_video_files(search_dirs, video_title):
    video_extensions = [".mkv", ".mp4", ".ts", ".webm"]
    num_files_searched = 0
    num_files_matched = 0
    for start_dir in search_dirs:
        for root, dirs, files in os.walk(start_dir):
            for file in files:
                num_files_searched += 1
                if os.path.splitext(file)[1] in video_extensions:
                    if video_title.lower() in file.lower():
                        num_files_matched += 1
                        print(os.path.join(root, file))
        print(f"Finished searching {start_dir}. {num_files_matched} files matched out of {num_files_searched} searched.")

search_dirs = ["E:\\", "F:\\", "G:\\"]  # Enter the drive letters or paths to search
title_to_search = input("Enter the title of the video to search for: ")
find_video_files(search_dirs, title_to_search)

#The function now keeps track of the total number of files searched and the number of files that match the video title. After searching each directory, it prints out an update on the number of files matched and the total number of files searched so far. This gives an idea of the progress of the search.
