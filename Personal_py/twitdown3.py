# ```
import requests

# URL Twitter video yang ingin diunduh
video_url = "https://twitter.com/i/status/1670163475421712384"

# Mendapatkan sumber halaman Twitter
response = requests.get(video_url)

# Mencari URL video dengan resolusi sederhana
start = response.text.find('https://video.twimg.com/')
end = response.text.find('.mp4', start) + 4
video_link = response.text[start:end]

# Unduh video ke direktori F:\
response = requests.get(video_link)
with open(r"F:\twitter_video.mp4", "wb") as outfile:
    outfile.write(response.content)

print("Video berhasil diunduh ke F:\twitter_video.mp4")
# ```

# Pastikan Anda mengganti URL video Twitter yang ingin diunduh di kode Anda. Juga pastikan bahwa F:\ direktori yang ada pada komputer Anda. Jika folder ini tidak ada, maka Anda harus menggantinya ke lokasi direktori yang benar pada komputer Anda.
