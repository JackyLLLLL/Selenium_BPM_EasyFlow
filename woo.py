import selenium
import time
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions

url = r"https://wootalk.today/"
secret_mes = r"成人模式"
chrome_path = r"C:\Users\jacky-lin\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"


opt = webdriver.ChromeOptions()
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome(chrome_path, options=opt)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

  

driver.get(url)


actions = ActionChains(driver)
menu = driver.find_element("css selector","""div[id=open-left]""")
actions.move_to_element(menu)
sleep(1)
actions.move_to_element(menu).click(menu)
sleep(1)
actions.perform()
sleep(1)

##menu = driver.find_element("css selector","""div[id=open-left]""")
##menu.click()
##sleep(1) 
secret = driver.find_element("link text","""使用密語""")
secret.click()
sleep(1) 

send_secret = driver.find_element("xpath","""//*[@id="keyInput"]""")
sleep(2)
send_secret.send_keys(secret_mes)

start_chat = driver.find_element("id","""startButton""")
sleep(0.5)
start_chat.click()

print("ok")


