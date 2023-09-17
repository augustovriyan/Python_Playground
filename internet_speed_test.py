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
    print("\nTesting upload speed...")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    print("Running Internet Speed Test...")
    test_internet_speed()
