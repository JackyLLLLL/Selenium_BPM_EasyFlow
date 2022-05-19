import selenium
import time
import threading
from selenium import webdriver
from time import sleep
from datetime import datetime


def start_chat():
    try:
        start_chat = driver.find_element("xpath","""//*[@id="app"]/div/button""") #點擊開始聊天
        if start_chat is not None:
            start_chat.click()
            print("點擊開始聊天")
    except Exception as e:
        pass
    
def messager(mes):
    while True:
        try:
            driver.find_element("css selector","""textarea.main-input""").send_keys(mes)#輸入訊息
            break
        except:
            pass
            

    driver.find_element("css selector","""button.send""").click() #送出訊息
    print("送出訊息")

def re_pair():
    count = 15
    while True:
        try:
            re_pair = driver.find_element("css selector","""button.message-content""")
            respond = driver.find_element("xpath","""//*[@id="app"]/div/div[1]/div[3]/div/div[2]/div/span[1]""")
            respond_2 = driver.find_element("css selector","""div.message.user.other""")
            respond_3 = driver.find_element("xpath","""//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div""")
            respond_4 = driver.find_element("xpath","""//*[@id="app"]/div/div[1]/div[4]/div""")
            respond_5 = driver.find_element("css selector","""div[class=message-content][style=background-color: rgb(40, 162, 223)]""")
            print(count)
            if re_pair is not None:
                re_pair.click()   
                print("對方已離開，點擊重新配對..")        
                break

            elif respond or respond_2  or respond_3 or respond_5 is not None:
                print("對方有回應")
                break
 
            
            elif count == 0:
                driver.find_element("css selector","""i.tool-button.leave-chat""").click()
                driver.find_element("css selector","""button.modal-default-button.confirm""").click()
                print("自動離開對話..")
                count = 15
                break
            count -= 1
           
                
        except Exception as e:
            pass

def left():
    while True:
        try:
            driver.find_element("css selector","""i.tool-button.normal-tool-button.show-command""").click()
            driver.find_element("css selector","""i.tool-button.leave-chat""").click()
            driver.find_element("css selector","""button.modal-default-button.confirm""").click()
            print("自動離開對話..")
            break
        except Exception as e:
            pass

def countdown(num_of_secs):
    global min_sec_format

    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        time.sleep(1)
        num_of_secs -= 1

def user_other():
     while True:
        try:
            user_other = driver.find_element("css selector","""div.message.user.other""")
            
            print("對方回應")
            break
        except Exception as e:
            print("無回應")
            sleep(1)
            pass    


url = r"https://knock.tw/"
mes = r"女"
count = 15

if __name__ == "__main__":
    
    driver = webdriver.Chrome()
    driver.get(url)
    

    while True:
        
        print("Start")
        start_chat()
        messager(mes)
        while True:
            try:
                driver.find_element("css selector","""div.[class=message-content][style=background-color:rgb(40, 162, 223)]""")
                print("1")
                sleep(1)
            except:
                print("2")
                pass

        
