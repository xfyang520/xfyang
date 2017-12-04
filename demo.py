#coding=utf-8
__author__ = 'Findlay'

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '58e0ca9b0903'
desired_caps['appPackage'] = 'com.cignacmb.hmsapp'
desired_caps['appActivity'] = '.ui.StartActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(4)

driver.find_element_by_id("ll_tab_sport").click()

time.sleep(2)

driver.swipe(1000,800,0,800)
#driver.find_element_by_id("tv_change_sport").click()

time.sleep(2)

#driver.shake()

print(driver.find_element_by_id("step_count").text)

print(driver.current_activity)

print(driver.get_window_size())

time.sleep(10)
driver.quit()