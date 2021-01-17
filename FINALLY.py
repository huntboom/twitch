import os
import sys
import requests
import urllib.request
from datetime import date
from datetime import datetime,timezone
from datetime import timedelta
from datetime import datetime, timedelta

client_id = 'ghl21u9bh2sahlgxgwfuv2o86zbujz'
client_secret='i7u0ksokaz5zag8cor31qxg1kgo8ft'
bearer_token = requests.post(f"https://id.twitch.tv/oauth2/token"
                                         f"?client_id={client_id}"
                                         f"&client_secret={client_secret}"
                                         "&grant_type=client_credentials").json()['access_token']
print(bearer_token)
authorizationtoken = 'Bearer '+bearer_token
if not os.path.exists('downloads'):
    os.mkdir('downloads')
top_game = requests.get("https://api.twitch.tv/helix/games/top",headers={"Client-ID": client_id,'Authorization': authorizationtoken},params={'first':5}).json()
for item in top_game['data']:
    top_gameID = item['id']
    top_game_name = item['name']
    print(top_game_name)
    local_time = datetime.now(timezone.utc).astimezone()
    yesterdate = (local_time-timedelta(7)).isoformat()
    top_clip = requests.get('https://api.twitch.tv/helix/clips',headers={"Client-ID": client_id,'Authorization': authorizationtoken},params={'game_id':top_gameID,'started_at':yesterdate,'first':2}).json()
    print('Now downloading Twitch Clips')
    print(top_clip)
    for item in top_clip['data']:
        slug = item['id'] 
        clipnumber= str(item)
        out_filename = slug + ".mp4"
        print(slug)
        # top_clip_url=top_clip['url']headers={"Client-ID": client_id,'Authorization': 'Bearer gwct88d9osd6cx4fwultixvcamt3wk'}
        # print(top_clip)
        headers = {"Client-ID": client_id, 'Authorization': authorizationtoken}
        #client_id = 'hqc99l0g1pv0qhy797w90t5jv04nrd'
        basepath = '/home/hunter/PycharmProjects/VideoAutomation/downloads/'
        # slug = clip.rpartition('/')[-1]

        clip_info = requests.get("https://api.twitch.tv/helix/clips?id=" + slug, headers={"Client-ID": client_id,'Authorization':authorizationtoken}).json()

        print(clip_info)
        thumb_url = clip_info['data'][0]['thumbnail_url']
        
        mp4_url = thumb_url.split("-preview", 1)[0] + ".mp4"

        output_path = (basepath + out_filename)


        def dl_progress(count, block_size, total_size):
            percent = int(count * block_size * 100 / total_size)
            sys.stdout.write("\r...%d%%" % percent)
            sys.stdout.flush()


        # create the basepath directory
        if not os.path.exists(basepath):
            os.makedirs(basepath)

        urllib.request.urlretrieve(mp4_url, output_path, reporthook=dl_progress)
    print(os.listdir())
    if not os.path.exists('downloads'):
            os.makedirs('downloads')
    os.chdir('downloads')
  
    #arr= os.listdir()
    print('Compiling twitch clips into one video....')
    from moviepy.editor import VideoFileClip, concatenate_videoclips
    from moviepy.editor import *

    clips = []

    for filename in os.listdir('.'):
        if filename.endswith(".mp4"):
            clips.append(VideoFileClip(filename))

    video = concatenate_videoclips(clips, method='compose')
    video.write_videofile('CurrentVideo.mp4')
    print('Uploading edited video to YouTube')
    from selenium import webdriver
    if __name__ == "__main__":
        import time

        driver = webdriver.Chrome()
        driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.find_element_by_xpath("//input[@type='email']").click()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("automate6969@gmail.com")
        driver.find_element_by_xpath("//div[@id='identifierNext']").click()
        time.sleep(4)
    import pyautogui
    pyautogui.write("cooldogmaui123")
    time.sleep(4)
    pyautogui.click(677,522)
    time.sleep(4)
    driver.get("https://studio.youtube.com/channel/UCR2MUX5Xzq552N9PArz7qxg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D")
    time.sleep(4)
    pyautogui.click(921,206)
    time.sleep(4)
    pyautogui.click(891,245)
    time.sleep(2)
    pyautogui.click(533,580)
    time.sleep(4)
    pyautogui.write("/home/hunter/PycharmProjects/VideoAutomation/downloads/CurrentVideo.mp4")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    from datetime import date
    today = "Top "+top_game_name+  " Highlights "+ str(date.today())
    pyautogui.write(today)
    pyautogui.click(953,688)
    time.sleep(3)
    pyautogui.click(114,554)
    time.sleep(2)
    pyautogui.click(953,688)
    time.sleep(2)
    pyautogui.click(953,688)
    time.sleep(2)
    pyautogui.click(166,600)
    time.sleep(2)
    pyautogui.click(951,691)
    print('Waiting for video to finish processing before deleting video...')
    time.sleep(100)
    print('Deleting video and clips now.')
    import os
    os.remove("CurrentVideo.mp4")
    import shutil
    #shutil.rmtree("/home/hunter/PycharmProjects/VideoAutomation/downloads")
    #print(top_game_video)
    #if not os.path.exists('downloads'):
        #os.makedirs('downloads')
    for file in os.scandir('/home/hunter/PycharmProjects/VideoAutomation/downloads'):
        if file.name.endswith(".mp4"):
            os.unlink(file.path)
    os.chdir('/home/hunter/PycharmProjects/VideoAutomation')