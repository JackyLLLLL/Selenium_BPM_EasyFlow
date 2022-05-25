import selenium
import time
import random
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains


url = r"https://wootalk.today/"
chrome_path = r"C:\Users\User\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe" #家裡的driver路徑
##chrome_path = r"C:\Users\jacky-lin\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"

mes = r"台南182 電愛不約"


opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome(chrome_path, options=opt)

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

x = random.uniform(6.8, 9.0)
y = random.uniform(0.5, 2.0)
sleep(x)

driver.find_element("id","""menuButton""").click()
sleep(y)
driver.find_element("xpath","""/html/body/div[5]/div/ul[1]/li[1]/a""").click()
sleep(y)
driver.find_element("css selector","""input.keyword[value='成人模式']""").click()
sleep(y)
driver.find_element("css selector","""input#startButton""").click()
sleep(y)
driver.find_element("id","""[messageInput]""").send_keys(mes)

#<input type="text" id="messageInput" placeholder="輸入訊息" autocomplete="off">

##start_chat = driver.find_element("css selector","""input#startButton""")
##actions = ActionChains(driver)
##sleep(1)
##actions.move_to_element(start_chat).click(start_chat)
##sleep(0.5)
##actions.perform()
