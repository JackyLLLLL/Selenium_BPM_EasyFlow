import selenium
import time
import random
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service



url = r"https://wootalk.today/"
##chrome_path = r"C:\Users\User\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe" #家裡的driver路徑
chrome_path = r"C:\Users\jacky-lin\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
mes = r""

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
print("get URL")

x = random.uniform(7.0, 9.0)
y = random.uniform(1.3, 2.4)
sleep(x)

actions = ActionChains(driver)


##menuButton = driver.find_element("id","""menuButton""")
##actions.move_to_element(menuButton).click(menuButton)
##print("menu Button")
##sleep(y)
##actions.perform()
##
##secret = driver.find_element("xpath","""/html/body/div[5]/div/ul[1]/li[1]/a""")
##actions.move_to_element(secret).click(secret)
##sleep(2)
##actions.perform()
##print("secret")
##
##adult_mode = driver.find_element("css selector","""input.keyword[value='成人模式']""")
##actions.move_to_element(adult_mode)
##sleep(y)
##adult_mode.click()
##actions.perform()
##print("choose mode")
##driver.find_element("css selector","""input#startButton""").click()
##sleep(y)
##driver.find_element("id","""[messageInput]""").send_keys(mes)

#<input type="text" id="messageInput" placeholder="輸入訊息" autocomplete="off">

start_chat = driver.find_element("css selector","""input#startButton""")
actions.move_to_element(start_chat).click(start_chat)
actions.perform()
print("Start chat")

print("OK")
