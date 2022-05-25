import selenium
import time
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions

url = r"https://wootalk.today/"
secret_mes = r"成人模式"
##chrome_path = r"C:\Users\User\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
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


driver.find_element("id","""menuButton""").click()
sleep(1)
driver.find_element("xpath","""/html/body/div[5]/div/ul[1]/li[1]/a""").click()
sleep(1)
driver.find_element("css selector","""input.keyword[value='成人模式']""").click()
sleep(2)
driver.find_element("css selector","""input#startButton""").click()

