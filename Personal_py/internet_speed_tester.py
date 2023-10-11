import speedtest

def test_internet_speed():
    # Create a Speedtest client
    st = speedtest.Speedtest()

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    print(f"Download speed: {download_speed:.2f} Mbps")

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload speed: {upload_speed:.2f} Mbps")

    server = st.get_best_server()
    print(f"Best server: {server['host']} ({server['country']})")

if __name__ == "__main__":
    print("Internet Speed Test")
    test_internet_speed()
