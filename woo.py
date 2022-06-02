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
                sleep(0.4)
                actions.move_to_element(start_chat).click(start_chat)
                actions.perform()
                print("點擊開始聊天")
                break
        except Exception as e:
            pass

def messager(mes):
    while True:
        try:
            paired_successfully = driver.find_element("xpath","""//*[@id="messages"]/div[4]""")
            if paired_successfully:
                driver.find_element("css selector","""input#messageInput""").send_keys(mes)         
                break
        except:
            pass
    send_button = driver.find_element("css selector","""div#sendButton""")
    actions = ActionChains(driver)
    if send_button:
        try:
            actions.move_to_element(send_button).click(send_button)
            actions.perform()       
    
        except:
            pass
    print("送出訊息")



##def re_pair():
##    count = 15
##    while True:
##        try:
##            re_pair = driver.find_element("xpath","""//*[@id="messages"]/div[11]/text()[1]""")
##            print(count)
##            if re_pair is not None:
##                driver.find_element("css selector","""div#changeButton""").click()   
##                print("對方已離開，點擊重新配對..")        
##                break
## 
##            
##            elif count == 0:
##                driver.find_element("css selector","""div#changeButton""").click()
##                sleep(0.5)
##                driver.find_element("css selector","""button#popup-yes.right""").click()
##                count = 15
##                break
##            count -= 1
##           
##                
##        except Exception as e:
##            pass

def left():
     while True:
        try:

            driver.find_element("css selector","""div[id='changeButton']""").click()
            sleep(0.8)
            driver.find_element("css selector","""button#popup-yes.right""").click()
            sleep(1)
            print("自動離開對話..")
            
            break
        except Exception as e:
            pass
    

#######################################################################################################################
    
url = r"https://wootalk.today/key/成人模式"

chrome_path = r"C:\Users\jacky.lin\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe" #家裡的driver路徑
##chrome_path = r"C:\Users\jacky-lin\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
mes = r"台南182男 28y 找約or電愛"
##mes = r"Hi"
count = 15

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

    while True:
        print("Start")
        if flag == True:
            start_chat()
            
        messager(mes)

        while True:
            try:
                respond = driver.find_element("css selector","""div.stranger.text""")         
                if respond:
                    print("對方有回應")
                    count = 15
                    flag = True
                    break
            except:
                pass                

                if count == 0:
                    print("計時歸零離開")
                    left()
                    count = 15
                    flag = True
                    break  
                else:
                    count -= 1
                    print(count)
                    sleep(1)

            try:
                re_pair = driver.find_element("xpath","""//*[@id="messages"]/div[8]/a""")
                if re_pair is not None:
                    driver.find_element("css selector","""div#changeButton""").click()
                    print("對方已離開，點擊重新配對..")
                    count = 15
                    flag = True
                    break
            except:
                pass







