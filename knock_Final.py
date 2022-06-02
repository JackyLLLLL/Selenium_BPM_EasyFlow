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
            start_chat = driver.find_element("css selector","""span.MuiButton-label""")
            actions = ActionChains(driver)
            
            if start_chat is not None:
                sleep(0.3)
                actions.move_to_element(start_chat).click(start_chat)
                actions.perform()
                print("點擊開始聊天")
                break
        except Exception as e:
            pass

def choose_famale():
    while True:
        try:
            choose = driver.find_element("css selector","""button[class='MuiButtonBase-root MuiToggleButton-root MuiToggleButtonGroup-grouped jss21 MuiToggleButtonGroup-groupedHorizontal jss19 MuiToggleButton-sizeSmall']""")
            if choose:
                choose.click()
                print("找異性")
                sleep(0.5)
            female = driver.find_element("css selector","""button[value='female']""")
            if female:
                female.click()
                print("找女性")
                break
        except Exception as e:
            pass
        
    
def messager(mes):
    while True:
        try:
            driver.find_element("css selector","""textarea.MuiInputBase-input.MuiInputBase-inputMultiline""").send_keys(mes)        
            break
        except:
            pass
            
    send_mes = driver.find_element("css selector",""".MuiButtonBase-root.MuiIconButton-root[aria-label='send']""") #送出訊息
    actions = ActionChains(driver)
    if send_mes:
        try:
            actions.move_to_element(send_mes).click(send_mes)
            actions.perform()
        except:
            pass
    print("送出訊息")

def re_pair():
    count = 15
    while True:
        try:
            re_pair = driver.find_element("css selector","""span.MuiButton-label""")
            respond = driver.find_element("css selector","""div[class='message user other']""")
            print(count)
            if re_pair is not None:
                re_pair.click()   
                print("對方已離開，點擊重新配對..")        
                break

            elif respond is not None:
                print("對方有回應")
                break
 
            
            elif count == 0:
                driver.find_element("css selector","""svg[class='MuiSvgIcon-root'][focusable='false']""").click()
                sleep(0.5)
                driver.find_element("css selector","""button[type='button'][data-test='ok']""").click()
                count = 15
                break
            count -= 1
           
                
        except Exception as e:
            pass


def left():
     while True:
        try:
            driver.find_element("css selector","""div[style='position: relative; grid-area: date / date / date / date; display: flex; align-items: flex-end; align-self: stretch;']""").click()
            sleep(0.5)
            driver.find_element("css selector","""svg[class='MuiSvgIcon-root'][focusable='false']""").click()
            driver.find_element("css selector","""button[type='button'][data-test='ok']""").click()
            print("自動離開對話..")
            
            break
        except Exception as e:
            pass
    

url = r"https://knock.tw/"
mes = "台南182 找約or電愛"
##mes = "Hi 女 等我一下"
chrome_path = r"C:\Users\jacky-lin\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
##chrome_path = r"C:\Users\user\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe"
user_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
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
    
##    countdown = 0
##    x = 0
##    y = 1
##    while True:
##
##        print("Program Start")
##        if flag == True:
##            start_chat()
##        messager(mes)
##        while True:
##            try:
##                re_pair = driver.find_element("css selector","""span.MuiButton-label""")
##                if re_pair:
##                    re_pair.click()
##                    print("點擊重新配對")
##                    flag = False
##                    countdown = 0
##                    y += 1
##                    break
##            except:
##                pass
##
##
##                if x == 0:
##                    countdown += 1
##                    print(f"累積配對人數:第{y}人,等待了: {countdown} 秒")
##                    sleep(1)


    while True:
        print("Start")
        if flag == True:
            start_chat()
            
        messager(mes)

        while True:
            try:
                respond = driver.find_element("css selector","""div[style='']""")
                respond = driver.find_element("xpath","""""")
                
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
                re_pair = driver.find_element("css selector","""span.MuiButton-label""") #新的
                if re_pair is not None:
                    re_pair.click()   
                    print("對方已離開，點擊重新配對..")
                    count = 15
                    flag = False
                    break
            except:
                pass

   




            

        
