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
        basepath = '/home/hunter/PycharmProjects/VideoAutomation/TwitchGithub/downloads/'
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
    video.write_videofile('CompiledClips.mp4')
    print('Uploading edited video to YouTube')
    from selenium import webdriver
    if __name__ == "__main__":
        if os.path.isdir("/home/ubuntu/"):
            from pyvirtualdisplay import Display
            display = Display(visible=0,size=(800, 600))
        import time
    driver = webdriver.Chrome()    
    driver.get('https://studio.youtube.com')
    time.sleep(2)
    from datetime import date
    today = "Top "+top_game_name+  " Highlights of November 27th"
    driver.find_element_by_xpath("//input[@type='email']").send_keys('automate6969@gmail.com')
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='password']").send_keys('cooldogmaui123')
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()
    time.sleep(2)
    driver.get('https://www.youtube.com/upload')
    time.sleep(2)
    elem = driver.find_element_by_xpath("//input[@type='file']")
    elem.send_keys("/home/hunter/PycharmProjects/VideoAutomation/downloads/CompiledClips.mp4")
    time.sleep(5)
    driver.find_element_by_xpath("//div[@id='textbox']").send_keys("Name of Video")
    time.sleep(5)
    driver.find_element_by_xpath("//paper-radio-button[@name='NOT_MADE_FOR_KIDS']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//ytcp-button[@id='next-button']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//ytcp-button[@id='next-button']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//paper-radio-button[@name='PUBLIC']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//ytcp-button[@id='done-button']").click()
    time.sleep(2)
    print('closing selenium webbrowser')
    driver.close()

    #+ str(date.today())
    #print('Waiting for video to finish processing before deleting video...')
    #time.sleep(400)
    #driver.close()
    print('Deleting video and clips now.')
    import os
    os.remove("CompiledClips.mp4")
    import shutil
    #shutil.rmtree("/home/hunter/PycharmProjects/VideoAutomation/downloads")
    #print(top_game_video)
    #if not os.path.exists('downloads'):
        #os.makedirs('downloads')
    for file in os.scandir('/home/hunter/PycharmProjects/VideoAutomation/TwitchGithub/downloads'):
        if file.name.endswith(".mp4"):
            os.unlink(file.path)
    os.chdir('/home/hunter/PycharmProjects/VideoAutomation/TwitchGithub')
    #print('Waiting for video to finish processing before deleting video...')
    #time.sleep(100)
    