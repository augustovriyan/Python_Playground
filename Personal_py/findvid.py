import os

def find_video_files(search_directories, target_title):
    """Search for video files with a specific title within given directories."""
    
    # List of video file extensions to consider
    video_extensions = [".mkv", ".mp4", ".ts", ".webm"]
    
    # Iterate over each start directory provided for the search
    for start_directory in search_directories:
        # Walk through the directory tree starting from the given directory
        for current_root, _, files in os.walk(start_directory):
            for file_name in files:
                # Check if the file has a video extension and matches the target title
                if os.path.splitext(file_name)[1].lower() in video_extensions and target_title.lower() in file_name.lower():
                    video_path = os.path.join(current_root, file_name)
                    print("Found:", video_path)

def main():
    """Main function to initiate the search for video files."""
    
    # Directories to search for video files (add or modify paths as needed)
    search_directories = ["E:\\", "F:\\", "G:\\"]
    
    # Prompt user to enter the title of the video to search for
    title_to_search = input("Enter the title of the video to search for: ")
    
    # Call the function to find video files with the specified title in the directories
    find_video_files(search_directories, title_to_search)

if __name__ == "__main__":
    main()
