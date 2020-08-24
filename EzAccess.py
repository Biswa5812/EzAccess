# importing libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import date
import pyautogui

# loading system date
t = time.localtime()
c=0
today = date.today()
today = str(today)
today = int(today[8::])
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()

# activating browser
browser.get('https://login.gitam.edu/Login.aspx')

# fetching credentials
browser.find_element_by_name('txtusername').send_keys('ENTER YOUR ROLL NUMBER')
browser.find_element_by_name('password').send_keys('ENTER G_LEARN PASSWORD')

browser.find_element_by_xpath("//input[@id='Submit']").click()

# Opening g-learn
browser.find_element_by_xpath("//*[@id='MainContent_studentg']/div[11]/a/h5").click()

# changing driver window
browser.switch_to.window(browser.window_handles[1])

# launching zoom
rows = browser.find_elements_by_xpath("//*[@id='ContentPlaceHolder1_GridViewonline']/tbody/tr")
for i in range(len(rows)):
    x_path = "//*[@id='ContentPlaceHolder1_GridViewonline']/tbody/tr[{}]/td/a/div/h6".format(i+1)
    row_content = browser.find_element_by_xpath(x_path).text
    print(row_content)
    test = row_content
    test_1 = list(test.split())
    date = list(test_1[2].split("-"))[0]
    date = int(date)
    start = test_1[4]
    end = test_1[6]
    t_com =  list(start.split(":"))[1:3]
   
    for j in list(end.split(":")):
        t_com.append(j)
    s_time = int(t_com[0]+t_com[1][0:2])
    if t.tm_hour>12:
        c_hr = t.tm_hour - 12
    else:
        c_hr = t.tm_hour
    if t.tm_min<10:
        c_min = '0' + str(t.tm_min)
    else:
        c_min = t.tm_min
    c_time = int(str(c_hr)+str(c_min))  
    if ((((s_time-c_time)-40)<45) and s_time-c_time>-15 ) and today==date:
        zoom_link = '//*[@id="ContentPlaceHolder1_GridViewonline"]/tbody/tr[{}]/td/a/div'.format(i+1)
        browser.find_element_by_xpath(zoom_link).click()
        time.sleep(5)
        pyautogui.click(1050, 290)
        time.sleep(1)
        # browser.quit()
        c +=1
        break
if(c==0):
    print("NO SESSION FOUND")
    browser.quit()
        
