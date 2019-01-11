"""
pytube module written by nficano
credit: https://github.com/nficano/pytube
combined with youtube API

Download all the videos in the the playlist. Initially, download
resolution is 720p (or highest available), later more option
should be added to download resolution of choice
"""

import os
import logging
import sys
import urllib

from pytube import Playlist
from pytube.__main__ import YouTube

logger = logging.getLogger(__name__)

videos_urls = ['https://www.youtube.com/watch?v=-Xn6IDytVGw']
playlists_pydata = {
    'PyData Seattle 2017': 'https://www.youtube.com/playlist?list=PLGVZCDnMOq0rxoq9Nx0B4tqtr891vaCn7',
    'Pandas': 'https://www.youtube.com/playlist?list=PLGVZCDnMOq0oywykwgVAcGvsGzagyMbwS',
    'Probabilistic Programming and Bayesian': 'https://www.youtube.com/playlist?list=PLGVZCDnMOq0rLLb519Ah3EntCUAAHPnfU',
    'Jupyter': 'https://www.youtube.com/playlist?list=PLGVZCDnMOq0reyEnGXyF5OX1KIquMIiXt',
    'Text_Language Processing': 'https://www.youtube.com/playlist?list=PLGVZCDnMOq0rjkF7p_F4qtaVJQnjK1oKT',
    'Data Visualisation': 'https://www.youtube.com/playlist?list=PLGVZCDnMOq0pV4lOIE-1EE0ZJiGtr0-Ha',
    'AI': 'https://www.youtube.com/playlist?list=PLGVZCDnMOq0rR4Zf7_8rDKlKeD1UCKdxD',
    'Data Mining': 'https://www.youtube.com/playlist?list=PLGVZCDnMOq0ogEIvRHZyXMNJwkEPHi6Bl',
    'Machine Learning': 'https://www.youtube.com/watch?v=wZnTOOU3K1Y&list=PLGVZCDnMOq0rVk5kyQVl8Sjt_Pcrf6XqA'}

playlists_sentdex = {
    'Level Python Intermediate 30': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_',
    '3D CNN for Kaggle 5': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDd5meH8cStO9cMi98tPT12_',
    'Quadcopter 5': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDfp4GmCdhbPhPwWt4O_TBmB',
    'Open_CV': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq',
    'Raspberry Pi 5': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDcG4wbhhCv_XTnexvWfjlBy',
    'Flask intro10': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB',
    'NLTK 30': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL',
    'Raspberry Pi I/O 4': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDdnpgDr1YZF9dI_4G334od6',
    'Open GL 16': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDdfGpqjkEJSeWKGCP31__wD',
    'Pandas Sentiment Analysis 12': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDdktuSQRsofoGxC2PTSdsi7',
    'Bitcoin Satoshi': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDcq2QME4pfeh0cE71mkb_qz',
    'Monte Carlo Simulation': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDdhOnp-FnVStDsALpYk2hk0',
    'Machine Learning Stock Analysis': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO',
    'Machine Learning Big Data Stock Trading': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDcR-u9O8LyLR7URiKuW-XZq',
    'ML, Parsing, NLTK, Big Data': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDfRO5bQFLcVgvIOIhNUZpZf',
    'GUIs': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDc4SQhfpm6XHO0l-1Ybtur2',
    'LEVEL_Intermediate Python': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G',
    'Big Data intro': 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDdGp4ppcRbVIkFf6gwzdEuz'}


class MyPlaylist(Playlist):
    def download_all(self, download_path=None):
        self.populate_video_urls()
        length = len(self.video_urls)
        print('Total videos found: ', length)
        print('Starting download')
        print('Complete:')

        for i, link in enumerate(self.video_urls):
            print_progress(i, length)
            yt = YouTube(link)
            dl_stream = yt.streams.filter(
                progressive=True, subtype='mp4',
            ).order_by('resolution').desc().first()
            logger.debug('download path: %s', download_path)
            dl_stream.download(download_path)
            logger.debug('download complete')
            print_progress(i + 1, length)


def print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def dl_user_playlist():
    try:
        playlist = input(
            """Please specify the link to the playlist e.g. 'https://www.youtube.com/playlist?list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3' """)
        destination = input(
            """Please give the path to destination directory e.g. 'C:/Users/Michu/Videos/Python_Videos/SQL_Lite' """)
        pl = MyPlaylist(playlist)
        try:
            os.stat(destination)
        except:
            os.mkdir(destination)
        pl.download_all(destination)
    except:
        print("An error has ocurred.")
    print("Downloading complete")


def dl_videos_from_list(video_list):
    download_path = os.path.dirname(os.path.realpath(__file__))
    length = len(video_list)
    print('Total videos found: ', length)
    print('Starting download')
    print('Complete:')
    for i, link in enumerate(video_list):
        print_progress(i, length)
        yt = YouTube(link)
        dl_stream = yt.streams.filter(
            progressive=True, subtype='mp4',
        ).order_by('resolution').desc().first()
        logger.debug('download path: %s', download_path)
        dl_stream.download(download_path)
        logger.debug('download complete')
        print_progress(i + 1, length)


def dl_dict_videos(directory, playlists):
    i = 1
    for name in playlists:
        destination = directory + name
        playlist = playlists[name]
        print("\nNow downloading {}, {}/{} of all playlists".format(name, i, len(playlists)))
        pl = MyPlaylist(playlist)
        try:
            os.stat(destination)
        except FileNotFoundError:
            os.mkdir(destination)
        pl.download_all(destination)
        i = i + 1
    print("\nDownloading complete")


if __name__ == '__main__':
    try:
        dl_videos_from_list(uc_British_col_machine_learning)
    except urllib.error.URLError:
        sys.stdout.write("You have no Internet Connection.")
        exit()
