# coding = utf-8
from selenium import webdriver
import time

dr = webdriver.Chrome(executable_path="D:\Tools\PythonTools\chromedriver.exe")
try:
    dr.get("https://www.douyu.com/t/lpl")
    dr.maximize_window()
    dr.implicitly_wait(15)
    print(dr.title)
    time.sleep(5)
    #点击X号去掉广告，如果没有广告要注释这行代码
    dr.find_element_by_xpath("/html/body/div[7]/div/div/div[2]").click()
    dr.find_element_by_link_text("登录").click()
    time.sleep(3)
    #切换到密码登录frame
    dr.switch_to.frame("login-passport-frame")
    time.sleep(5)
    #点击密码登录
    dr.find_element_by_xpath("//*[@id='loginbox']/div[2]/div[2]/div[3]/div/span[2]").click()
    # dr.find_element_by_link_text("密码登录").click()  还是不要用字符串定位元素好
    time.sleep(3)
    #点击QQ图标
    dr.find_element_by_xpath("//*[@id='loginbox']/div[3]/div[2]/div[2]/div[2]/a[1]").click()
    time.sleep(3)

    # 获取当前窗口句柄（窗口A）
    handle = dr.current_window_handle
    print(handle)
    # 获取当前所有窗口句柄（窗口A、B）
    handles = dr.window_handles
    # 对窗口进行遍历
    for newhandle in handles:
        # 筛选新打开的窗口B
        if newhandle != handle:
            # 切换到新打开的窗口B
            dr.switch_to_window(newhandle)
            # 在新打开的窗口B中操作

            dr.switch_to.frame("ptlogin_iframe")
            time.sleep(3)
            ele = dr.find_element_by_id("switcher_plogin").click()
    dr.find_element_by_xpath("//*[@id='u']").send_keys("你的QQ帐号")
    dr.find_element_by_xpath("//*[@id='p']").send_keys("你的QQ密码")
    dr.find_element_by_xpath("//*[@id='login_button']").click()

    print("登录成功")
    # dr.get("https://www.douyu.com/t/lpl")
    # dr.implicitly_wait(15)
    # print(dr.title)
    while(1):
        dr.find_element_by_xpath("//*[@id='js-send-msg']/textarea").send_keys("厂长加油")
        time.sleep(3)
        dr.find_element_by_xpath("//*[@id='js-send-msg']/div[1]").click()
        #清空缓冲
        dr.find_element_by_xpath("//*[@id='js-send-msg']/textarea").clear()
        print("厂长加油")
        time.sleep(3)
        dr.find_element_by_xpath("//*[@id='js-send-msg']/textarea").send_keys("您配吗")
        time.sleep(3)
        dr.find_element_by_xpath("//*[@id='js-send-msg']/div[1]").click()
        # 清空缓冲
        dr.find_element_by_xpath("//*[@id='js-send-msg']/textarea").clear()
        print("您配吗")
        time.sleep(3)
    dr.quit()
except Exception as e:
    print(e)
#
