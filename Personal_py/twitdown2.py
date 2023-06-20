# ```python
import re
import urllib.request
import sys

# from setuptools.config._validate_pyproject.formats import url


def download_twitter_video(url, filename): (
    'https://twitter.com/MasterAlecsDOM/status/1670163475421712384', 'test_vid1.mp4')


# set the maximum resolution for the downloaded video (720p)
max_resolution = 720

# download the HTML source code of the tweet's page
# with urllib.request.urlopen(url) as response:
#    html = response.read().decode('utf-8')

# extract the video URL from the HTML source code
pattern = re.compile(
    r'content="https://video.twimg.com/ext_tw_video/\d+/pu/vid/\d+x(\d+)')
# match = pattern.search(html)
# if not match:
print('Error: could not find video URL in tweet.')
return
video_url = re.sub(r'\d+x(\d+)', f'{max_resolution}x\\1', match.group(0)[9:])

# display a download progress bar
print('Downloading...', end='')


def report_hook(count, block_size, total_size):
    progress = count * block_size * 100 / total_size
    progress_bar_width = 50
    progress_bar = ('=' * int(progress / 2)).ljust(progress_bar_width)
    sys.stdout.write('\r[%s] %.1f%%' % (progress_bar, progress))
    sys.stdout.flush()


# download the video
# urllib.request.urlretrieve(video_url, filename, report_hook)
print('\nDownload complete.')

# example usage: download a Twitter video and save it as "my_video.mp4"
# download_twitter_video('https://twitter.com/twitter/status/1397992930550578177', 'my_video.mp4')
# ```

# Let me know if you have any other questions or need further assistance!
