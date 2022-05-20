import selenium
import time
from selenium import webdriver
from time import sleep



def start_chat():
    while True:
        try:
            start_chat = driver.find_element("xpath","""//*[@id="app"]/div/button""") #點擊開始聊天
            if start_chat is not None:
                start_chat.click()
                print("點擊開始聊天")
                break
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


url = r"https://knock.tw/"
mes = input("請輸入第一句話:")
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
                respond = driver.find_element("css selector","""div[style='background-color: rgb(40, 162, 223);']""")
                if respond:
                    print("對方有回應")
                    count = 15
                    break
            except:
                pass                

                if count == 0:
                    print("計時歸零離開")
                    left()
                    count = 15
                    break  
                else:
                    count -= 1
                    print(count)
                    sleep(1)

            try:
                re_pair = driver.find_element("css selector","""button.message-content""")
                if re_pair is not None:
                    re_pair.click()   
                    print("對方已離開，點擊重新配對..")
                    count = 15
                    break
            except:
                pass
                


            

        
