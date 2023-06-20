#If you want to search for a specific title of a video, you can modify the code to include a parameter that takes the title as input and then matches it against the filenames of the video files. Here's an example:

#```python
import os

def find_video_files(search_dirs, video_title):
    video_extensions = [".mkv", ".mp4", ".ts", ".webm"]
    for start_dir in search_dirs:
        for root, dirs, files in os.walk(start_dir):
            for file in files:
                if os.path.splitext(file)[1] in video_extensions:
                    if video_title.lower() in file.lower():
                        print(os.path.join(root, file))

search_dirs = ["E:\\", "F:\\", "G:\\"]  # Enter the drive letters or paths to search
title_to_search = input("Enter the title of the video to search for: ")
find_video_files(search_dirs, title_to_search)
#```

#In this updated code, we added a new parameter called `video_title` to the `find_video_files` function, which takes the input from the user for the title to search for.

#Then, we added an extra `if` statement inside the `for file in files` loop to check whether the `video_title` parameter is present in the filename in lowercase (using `lower()`), and only prints the file path if it matches.

#To use the script, just run it with Python as before, and enter the title of the video you want to search for when prompted.
