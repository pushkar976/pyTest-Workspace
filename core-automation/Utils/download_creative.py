import os
import subprocess

import requests
from bs4 import BeautifulSoup
import random

class CreativeDownload:

    def __init__(self,VIDEO_COLLECTION_PAGE="",SPECIFIC_VIDEO_URL=""):
        # URL for entire page which has collection of videos
        self.PAGE_URL = VIDEO_COLLECTION_PAGE

        # URL of specific video present in that page
        self.VIDEO_URL = SPECIFIC_VIDEO_URL
    
    def get_video_links(self):
        # create response object
        if not self.PAGE_URL:
            r = requests.get(self.VIDEO_URL)
            soup = BeautifulSoup(r.content, 'html5lib')
            links = soup.findAll('a')
        else:
            company = input("Enter which company ad you want to download : ")
            r = requests.get(self.PAGE_URL+company)

            # create beautiful-soup object
            soup = BeautifulSoup(r.content, 'html5lib')
            # print(soup)

            # find all links on web-page
            links = soup.findAll('a')
            ad_link_list = []
            for l in links:
                # print("-----------",l)
                if '<a href="/ad' in str(l):
                    tmp_path = str(l).split('>')
                    path = tmp_path[0].split('=')
                    actual_ad_link = 'https://www.ispot.tv'+path[1].split('"')[1]
                    ad_link_list.append(actual_ad_link)

            ad_link = random.choice(ad_link_list)
            r = requests.get(ad_link)
            soup = BeautifulSoup(r.content, 'html5lib')
            links = soup.findAll('a')

            # filter the link sending with .mp4
        video_links = [link['href'] for link in links if link['href'].endswith('mp4')]

        return video_links
    
    
    def download_video_series(self,video_links):
        file_name = ''
        if len(video_links) != 0:
            for link in video_links:
                '''iterate through all links in video_links
                and download them one by one'''
    
                # obtain filename by splitting self.PAGE_URL and getting
                # last string
                file_name = link.split('/')[-1]
                print("Downloading file:%s" % file_name)
    
                # create response object
                r = requests.get(link, stream=True)
    
                # download started
                with open(file_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            f.write(chunk)
    
                print("%s downloaded!\n" % file_name)
    
            print("Videos downloaded!")
        else:
            pass
        return file_name

    def move_creative_file(self,filepath):
        creative_dir = os.path.dirname(__file__)+'/creatives'
        download_dir = filepath
        move_ad = subprocess.Popen(
            ['cp', download_dir, creative_dir], shell=False, text=True, stdout=subprocess.PIPE,
        )
        move_ad.wait()
        delete_ad_from_current_dir = subprocess.Popen(
            ['rm', download_dir], shell=False, text=True, stdout=subprocess.PIPE,
        )
        delete_ad_from_current_dir.wait()

    def download_youtube_video(self,video_url):

        import pytube
        from pytube import YouTube
        # video_url = self.VIDEO_URL
        if not video_url:
            print("Empty SPECIFIC VIDEO URL! Provide a valid URL and Try Again.")
        else:
            try:
                yt_obj = YouTube(video_url)

                filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

                # download the highest quality video
                filters.get_highest_resolution().download()
                print('Video Downloaded Successfully')
            except Exception as e:
                print(e)


