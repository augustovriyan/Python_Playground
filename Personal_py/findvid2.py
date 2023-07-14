import os
from tqdm import tqdm

def find_video_files(search_dirs, video_title):
    video_extensions = [".mkv", ".mp4", ".ts", ".webm"]
    num_files_searched = 0
    num_files_matched = 0
    
    for start_dir in search_dirs:
        for root, dirs, files in os.walk(start_dir):
            for file in tqdm(files, desc="Searching files", unit="file"):
                num_files_searched += 1
                if os.path.splitext(file)[1] in video_extensions:
                    if video_title.lower() in file.lower():
                        num_files_matched += 1
                        print(os.path.join(root, file))
    
    print(f"Finished searching. {num_files_matched} files matched out of {num_files_searched} searched.")

search_dirs = ["E:\\", "F:\\", "G:\\"]  # Enter the drive letters or paths to search
title_to_search = input("Enter the title of the video to search for: ")
find_video_files(search_dirs, title_to_search)
