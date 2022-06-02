import selenium
import time
import random
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

def start_chat():
    while True:
        try:
            start_chat = driver.find_element("id","""startButton""")
            actions = ActionChains(driver)
            
            if start_chat is not None:
                sleep(0.3)
                actions.move_to_element(start_chat).click(start_chat)
                actions.perform()
                print("點擊開始聊天")
                break
        except Exception as e:
            pass

def messager(mes):
    while True:
        try:
            driver.find_element("css selector","""input#messageInput""").send_keys(mes)         
            break
        except:
            pass
    sleep(1)
    send_button = driver.find_element("css selector","""div#sendButton""")
    actions = ActionChains(driver)
    if send_button:
        try:
            actions.move_to_element(send_button).click(send_button)
            actions.perform()       
    
        except:
            pass
    print("送出訊息")
        
            

#######################################################################################################################
    
url = r"https://wootalk.today/key/成人模式"

##chrome_path = r"C:\Users\User\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe" #家裡的driver路徑
chrome_path = r"C:\Users\jacky-lin\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
mes = r""

if __name__ == "__main__":
    
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

    flag = True
    y = random.uniform(0.2,0.9)

    sleep(y)
    
    while True:
        try:
            print("Program Start")
            if flag == True:
                start_chat()
                sleep(y)
            messager(mes)
            break
        finally:
            pass



