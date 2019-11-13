from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from config import user,pwd
name= "HARI K BATCHU"
subcode = "ADMIN TASK"

code_lookup = "HADOOP DISTRIBUTED FILE SYSTEM (HDFS)"
#summery = "[HADOOP] CREATE NEW ACCOUNTS UNDER RDIP HADOOP_M"
#summery = "Updating RDIP Platform Bookmark page"
summery = "DEVMCC agent log directory free space waring on"
#description = "This ticket is created to track all the AD principals done from team and also to track the time effort for it."

#description = 'Need to update below service links to the RDIP Platform Bookmark page'
cluster = ""
group = "TECH-RD-INFO-PLATFORM"
n = 1

driver = webdriver.Chrome()
driver.get("https://stvus029.corpnet2.com/arsys_en/shared/login.jsp")
#username and password
elem = driver.find_element_by_id("username-id")
elem.send_keys(user)
elem = driver.find_element_by_id("pwd-id")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

try:
    elem = driver.switch_to.alert
    elem.accept()
except:
    print("nothing")    

try:
    elem = driver.find_element_by_xpath('//*[@id="ardivcl"]')
    elem.click() 
except:
    print("0")
j=1

wait = WebDriverWait(driver, 10 )
for i in range(0,n):
    try:
#set 1st window as active window
        driver.switch_to.window(driver.window_handles[0])
        elem = driver.find_element_by_id("WIN_0_300000000")
        elem.send_keys(Keys.RETURN)
    except:
            print("00")

#set 2nd window as active window
    driver.switch_to.window(driver.window_handles[j])

#login name
    elem = driver.find_element_by_id("arid_WIN_0_240000005")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)

#summery
    elem = driver.find_element_by_id("arid_WIN_0_8")
    elem.send_keys(summery)

#casetype
    elem.find_element_by_xpath('//*[@id="arid_WIN_0_260000130"]').click()

#misc
    elem.find_element_by_xpath('/html/body/div[3]/div[2]/table/tbody/tr[2]/td[1]').click()

#code lookup
    elem = driver.find_element_by_id("arid_WIN_0_536871047")
    elem.send_keys(code_lookup)
    elem.send_keys(Keys.RETURN)

    try:
#subcode
        elem =driver.find_element_by_xpath('//*[@id="arid_WIN_0_200000005"]')
#ADMIN TASK
        elem = elem.send_keys(subcode)
    except:
            print("subcode")
#casetype
    try:
        elem =driver.find_element_by_xpath('//*[@id="arid_WIN_0_260000130"]')
        elem.click()
    except:
        print("casetype")

#misc
    elem.find_element_by_xpath('/html/body/div[3]/div[2]/table/tbody/tr[2]/td[1]').click()

#keyword
    elem = driver.find_element_by_xpath('//*[@id="arid_WIN_0_700072007"]')
    elem.send_keys(cluster)

#group
    elem = driver.find_element_by_xpath('//*[@id="arid_WIN_0_240000006"]')
    elem.send_keys(group)

#individual
    elem = driver.find_element_by_xpath('//*[@id="arid_WIN_0_240000015"]')
    elem.send_keys(name)
#description
    elem = driver.find_element_by_xpath('//*[@id="arid_WIN_0_240000007"]')
    elem.send_keys(description)
    j=j+1
    
    
