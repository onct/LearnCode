
# -*- coding: utf-8 -*-import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
import time


def writewj(name, phone):
    driver = webdriver.Edge(r"C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedgedriver.exe")
    # 'https://www.wenjuan.com/s/6VVJZfT/'
    driver.get('https://www.wenjuan.top/s/NJ3EvuS')
    # 定位所有的问卷问题
    questions = driver.find_elements_by_css_selector('.matrix')
    for answers in questions:
        # 定位所有问卷问题选项
        answer = answers.find_elements_by_css_selector('.icheckbox_div')
        # 定位需要填写文字的选项，并填入相关内容
        if  answer:
            choose_ans = random.choice(answer)
            choose_ans.click()
        else:
            break
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda1").click()
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda1").clear()
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda1").send_keys(u"李yan")
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda2").clear()
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda2").send_keys("15838319693")
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda3").click()
    Select(driver.find_element_by_id("5e61c0bd92beb526e8c0cda3")
        ).select_by_visible_text(u"河南省")
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda3").click()
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda4").click()
    Select(driver.find_element_by_id("5e61c0bd92beb526e8c0cda4")
        ).select_by_visible_text(u"焦作市")
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda4").click()
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda5").click()
    Select(driver.find_element_by_id("5e61c0bd92beb526e8c0cda5")
        ).select_by_visible_text(u"孟州市")
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda5").click()
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda6").click()
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda6").clear()
    driver.find_element_by_id("5e61c0bd92beb526e8c0cda6").send_keys(u"谷旦镇")

    driver.find_element_by_xpath(
        "//div[@id='question_5e61c0bc92beb526e8c0cd5f']/div[2]/div[2]").click()
    driver.find_element_by_id("next_button").click()
    # 延迟问卷结果提交时间，以免间隔时间太短而无法提交
    time.sleep(2)
    driver.quit()
if __name__ == "__main__":
    namelist = u'[[李yan,李现]]'
    phonelist = ['15838319691', '15838329692']
    t=2
    for i in range(t):
        writewj(name=namelist[i],phone=phonelist[i]) 
        print('已经成功提交了{}次问卷'.format(int(i)+int(1)))