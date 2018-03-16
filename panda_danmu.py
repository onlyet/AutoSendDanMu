# from selenium import webdriver
#
# browser = webdriver.Chrome("D:\Tools\PythonTools\chromedriver.exe")
# browser.get('http://www.baidu.com/')

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome("D:\Tools\PythonTools\chromedriver.exe")
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)


# coding = utf-8
from selenium import webdriver
import time

dr = webdriver.Chrome(executable_path="D:\Tools\PythonTools\chromedriver.exe")
try:
    dr.get("https://www.panda.tv/52222")
    dr.maximize_window()
    dr.implicitly_wait(15)
    print(dr.title)
    dr.find_element_by_link_text("登录").click()
    time.sleep(3)
    #点击QQ登录
    ele = dr.find_element_by_xpath("//*[@id='ruc-dialog-container']/div[1]/div[3]/div/div[7]/ul/li[1]/a").click()
    time.sleep(3)

    #点击帐号密码登录
    # ele = dr.find_element_by_xpath("//*[@id='bottom_qlogin']").click()
    # ele = dr.find_element_by_link_text("帐号密码登录").click()
    #切换到iframe
    dr.switch_to.frame("ptlogin_iframe")
    time.sleep(3)
    #点击帐号密码登录
    dr.find_element_by_id("switcher_plogin").click()
    ele = dr.find_element_by_xpath("//*[@id='u']").send_keys("QQ帐号")
    ele = dr.find_element_by_xpath("//*[@id='p']").send_keys("QQ密码")
    # ele = dr.find_element_by_xpath("//*[@id='ruc-dialog-container']/div[1]/div[3]/div/div[1]/div/input").send_keys("手机号")
    # ele = dr.find_element_by_xpath("//*[@id='ruc-dialog-container']/div[1]/div[3]/div/div[2]/input").send_keys("手机密码")
    # time.sleep(3)
    dr.find_element_by_xpath("//*[@id='login_button']").click()
    print("登录成功")
    # dr.switch_to.default_content()
    dr.switch_to.parent_frame()
    while(1):
        dr.find_element_by_xpath("//*[@id='main-container']/div[2]/div[4]/div[2]/div[1]/textarea").send_keys("还有谁")
        time.sleep(5)
        dr.find_element_by_xpath("//*[@id='main-container']/div[2]/div[4]/div[2]/div[2]").click()
    dr.quit()
except Exception as e:
    print(e)

