import selenium
import time
import random
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service

url = r"https://wootalk.today/"
secret_mes = r"成人模式"
##chrome_path = r"C:\Users\jacky-lin\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
chrome_path = r"C:\Users\user\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"


s = Service(chrome_path)

opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome(service = s)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
driver.execute_script(script)
driver.get(url)

y = random.uniform(1.3, 2.4)
mes = r"台南182 找約or電愛"

########################## 點擊目錄###################
actions = ActionChains(driver)
menu = driver.find_element("css selector","""div[id=open-left]""")
actions.move_to_element(menu)
sleep(y)
actions.move_to_element(menu).click(menu)
sleep(y)
actions.perform()
sleep(y)
#############################################

########################## 點擊密語###################
secret = driver.find_element("link text","""使用密語""")
secret.click()
sleep(y) 
#############################################

########################## 輸入密語###################
send_secret = driver.find_element("xpath","""//*[@id="keyInput"]""")
sleep(y)
send_secret.send_keys(secret_mes)
#############################################

##########################點擊開始聊天###################
start_chat = driver.find_element("id","""startButton""")
sleep(y)
start_chat.click()
sleep(y)
############################################

##########################輸入訊息###################
driver.find_element("css selector","""input#messageInput""").send_keys(mes)
sleep(y)
sleep(5)
try:
    send_button = driver.find_element("css selector","""div#sendButton""")
    if send_button:
        send_button.click()
except:
    pass
##<input type="button" value="回報" onclick="sendMessage(); return false;">
##<input type="text" id="messageInput" placeholder="輸入訊息" autocomplete="off">
##<input type="button" value="回報" onclick="sendMessage(); return false;">

print("ok")


