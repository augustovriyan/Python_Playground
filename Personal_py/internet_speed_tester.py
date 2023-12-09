import speedtest

def test_internet_speed():
    # Create a Speedtest client
    st = speedtest.Speedtest()

    # Function to convert bytes to megabits per second
    def convert_to_mbps(bytes_per_second):
        return bytes_per_second / 1_000_000

    # Function to display speed results
    def display_speed(test_type, speed):
        print(f"Testing {test_type} speed...")
        speed_mbps = convert_to_mbps(speed)
        print(f"{test_type.capitalize()} speed: {speed_mbps:.2f} Mbps")

    # Test download speed
    download_speed = st.download()
    display_speed("download", download_speed)

    # Test upload speed
    upload_speed = st.upload()
    display_speed("upload", upload_speed)

    # Get the best server for accurate results
    server = st.get_best_server()

    # Display the best server's information
    print(f"Best server: {server['host']} ({server['country']})")

if __name__ == "__main__":
    print("Internet Speed Test")
    test_internet_speed()
