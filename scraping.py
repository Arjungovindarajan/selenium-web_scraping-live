import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import smtplib, ssl
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

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

def send_email(video_df):
    try:
        subject = "Top Youtube Trending Videos"
        body = "This is now trending today in Youtube, an email with attachment sent from Python. Kindly see this attachment."

        sender_email = "arjunviki44@gmail.com"
        receiver_email = "arjunviki44@gmail.com"
        password = 'nufb bcug sari fvgd'

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email

        message.attach(MIMEText(body, 'plain'))

        filename = "video_data.csv"
pip3.11 install -t selenium/python/lib/python3.11/site-packages selenium==4.16.0
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",)
            message.attach(part)

        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            print('Mail sent successfully')
            server.close()

    except Exception as e:
        print(f'Something went wrong: {e}')








        # server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server_ssl.ehlo()

        # sender_email = 'arjunviki44@gmail.com'
        # Receiver_email = 'arjunviki44@gmail.com'  
        # sender_pass = 'nufb bcug sari fvgd'
        
        # for key, value in os.environ.items():
        #     print(f'{key}: {value}')
        # Use environment variable to retrieve the password
        # sender_pass = os.environ.get('Gmail_pass')
        # print(sender_pass)

        # if sender_pass is None:
        #     raise ValueError("Gmail_pass environment variable is not set.")
    
        # subject = 'Top Youtube Trending Videos'

        # email_text = f"""\
        # From: {sender_email}
        # To: {Receiver_email}
        # Subject: {subject}

        # {body}
        # """
        # video_df.to_csv('video_data.csv', index=None)
        # attachment = open("video_data.csv", "rb") 
  
        # p = MIMEBase('application', 'octet-stream') 
 
        # p.set_payload((attachment).read()) 
 
        # encoders.encode_base64(p) 
        
        # p.add_header('Content-Disposition', "attachment; filename= %s" % 'video_data.csv') 
 
        # server_ssl.attach(p)

        # print('Login', sender_email, sender_pass)
        # server_ssl.login(sender_email, sender_pass)
        # print('Login successful')
        # server_ssl.sendmail(sender_email, Receiver_email, email_text, attachment)
        # server_ssl.close()
        # print('Mail sent successfully')

if __name__ == "__main__":
    print('Creating driver')
    driver = get_driver()

    print('Fetching trending videos')
    videos = get_video(driver)

    print('title video:', driver.title)

    print("parsing the firt video")

    print("top 10 video data")
    video_data = [parse_video(video) for video in videos[:10]]

    video_df = pd.DataFrame(video_data)
    # video_df.to_csv('video_data.csv', index=None)
    # df = pd.read_csv('video_data.csv')
    # print(df)

    print('Send the result over email')
    body = json.dumps(video_data, indent=2)
    send_email(video_df)
    print('finish')
"""
# responce = requests.get(TRENDING_YOUTUBE_URL)

# print("status code:", responce.status_code)
# print("status code:", responce.text[:2000])

# with open('trend.html','w') as f:
#     f.write(responce.text)

# doc = BeautifulSoup(responce.text, 'html.parser')

# print('Page title:', doc.title)
# # print(len(doc))

# # find all video counts

# vid_div = doc.find_all('div', class_ = "style-scope ytd-shelf-renderer")
# print(f'total {len(vid_div)} videos')
"""