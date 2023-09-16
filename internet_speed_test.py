import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    
    # Get the best server
    st.get_best_server()
    
    # Perform download and upload speed tests
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    print("Testing download speed...")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    
    print("\nTesting upload speed...")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    print("Running Internet Speed Test...")
    test_internet_speed()
