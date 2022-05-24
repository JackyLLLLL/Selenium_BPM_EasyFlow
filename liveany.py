import selenium
import time
from selenium import webdriver
from time import sleep
    

def send_messagner(mes):
    messagner = driver.find_element("id","""inputText""")
    messagner.send_keys(mes)
    print("輸入訊息中..")
    send_mes = driver.find_element("id","""sendMessageButton""")
    send_mes.click()
    print("點擊送出訊息..")

def left():
    try:
        driver.find_element("css selector","""h4[陌生人離開~~]""")
    except:
        pass

def new_conncet():
    
    new_connect = driver.find_element("id","""reConnectButton""") #點擊新連線
    new_connect.click()


def respond():

    respond = driver.find_element("css selector","""div[class='bubble left yellow']""")


url = r"https://www.liveany.com/web.html"
mes = r"182男"
count = 15


if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.get(url)

    flag = False  

    while True:
        
         print("Start")
         if flag == True:
            new_conncet()
         send_messagner(mes)

         while True:
            try:
              respond = driver.find_element("css selector","""div[class='bubble left yellow']""")
              if respond:
                  print("對方有回應")
                  count = 15
                  flag = True
                  break
            except:
              pass

              if count == 0:
                  print("計時歸零離開")
                  count = 15
                  flag = True
                  break
              else:
                  count -= 1
                  print(count)
                  sleep(1)

            try:
                re_pair = driver.find_element("css selector","""h4[陌生人離開~~]""")
                if re_pair:   
                    print("對方已離開，點擊重新配對..")
                    count = 15
                    flag = True
                    break
            except:
                pass
             
         

                    
        


