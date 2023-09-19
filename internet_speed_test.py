import speedtest

def test_internet_speed():
    # Create a Speedtest object
    st = speedtest.Speedtest()
    
    # Find the best server for testing
    st.get_best_server()
    
    # Perform download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    # Print download speed results
    print("Testing download speed...")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    
    # Print upload speed results
    print("Testing upload speed...")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    
    # Save results to a text file (optional)
    save_results_to_file(download_speed, upload_speed)

def save_results_to_file(download_speed, upload_speed):
    with open("speedtest_results.txt", "a") as file:
        file.write(f"Download Speed: {download_speed:.2f} Mbps\n")
        file.write(f"Upload Speed: {upload_speed:.2f} Mbps\n\n")

if __name__ == "__main__":
    print("Running Internet Speed Test...")
    test_internet_speed()
