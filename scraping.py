import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


TRENDING_YOUTUBE_URL = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'



def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_video(driver):
    video_div_tag = 'ytd-video-renderer'
    driver.get(TRENDING_YOUTUBE_URL)
    videos = driver.find_elements(By.TAG_NAME, video_div_tag)
    return videos

def parse_video(videos):
    title_tag = videos.find_element(By.ID, 'video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')
    thumbnail_tag = videos.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')
    channel_div = videos.find_element(By.CLASS_NAME, 'ytd-channel-name')
    chanel_name = channel_div.text
    description  = videos.find_element(By.ID, 'description-text').text

    return {
        'title' : title,
        'url' : url,
        'thumbnail_url': thumbnail_url,
        'chanel' : chanel_name,
        'description' : description
    }

if __name__ == "__main__":
    # print('Creating driver')
    driver = get_driver()

    # print('Fetching trending videos')
    videos = get_video(driver)

    # print('title video:', driver.title)

    # print("parsing the firt video")

    print("top 10 video data")
    video_data = [parse_video(video) for video in videos[:10]]

    video_df = pd.DataFrame(video_data)
    video_df.to_csv('video_data.csv', index=None)
    df = pd.read_csv('video_data.csv')

    print(df)

"""
responce = requests.get(TRENDING_YOUTUBE_URL)

# print("status code:", responce.status_code)
# print("status code:", responce.text[:2000])

with open('trend.html','w') as f:
    f.write(responce.text)

doc = BeautifulSoup(responce.text, 'html.parser')

print('Page title:', doc.title)
# print(len(doc))

# find all video counts

vid_div = doc.find_all('div', class_ = "style-scope ytd-shelf-renderer")
print(f'total {len(vid_div)} videos')
"""