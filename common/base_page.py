#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: base_page.py
# @time: 2023/3/16 22:55
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from common.config_utils import local_config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def set_browser_max(self):
        self.driver.maximize_window()

    def set_browser_min(self):
        self.driver.minimize_window()

    def refresh(self):
        self.driver.refresh()

    def wait(self, wait_time=local_config.get_time_out):
        time.sleep(wait_time)

    def implicitly(self, wait_time=local_config.get_time_out):
        self.driver.implicitly_wait(wait_time)

    def get_title(self):
        value = self.driver.title
        return value

    # 封装元素操作
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        elif locator_type_name == 'css_selector':
            locator_type = By.CSS_SELECTOR
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        element = WebDriverWait(self.driver, locator_timeout).until(lambda x: x.find_element(locator_type,
                                                                                             locator_value_info))
        # element = WebDriverWait(self.driver, locator_timeout).until(EC.visibility_of_element_located(locator_type, locator_value_info))
        return element

    def switch_to_frame(self, **element_info):
        self.wait(2)
        if 'id' == element_info['locator_type']:
            self.driver.switch_to.frame(element_info['locator_value'])
        elif 'name' == element_info['locator_type']:
            self.driver.switch_to.frame(element_info['locator_value'])
        else:
            element = self.find_element(element_info)
            self.driver.switch_to.frame(element)

    def switch_to_alert(self, action='accept', time_out=local_config.get_time_out):
        alert = WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert_text = alert.text
        if action.lower() == 'accept':
            alert.accept()
        elif action.lower() == 'dismiss':
            alert.dismiss()
        return alert_text

    def get_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window_by_handle(self, window_handle):
        return self.driver.switch_to.window(window_handle)

    def switch_to_window_by_tittle(self, title):
        handles = self.driver.window_handles
        for window_handle in handles:
            if WebDriverWait(self.driver, local_config.get_time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    def switch_to_window_by_url(self, url):
        handles = self.driver.window_handles
        for window_handle in handles:
            if WebDriverWait(self.driver, local_config.get_time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()

    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)

    # 鼠标、键盘事件封装（建议先判断操作系统类型）
    def click_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).click(element).perform()

    def right_click_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).context_click(element).perform()

    def double_click_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).double_click(element).perform()

    def move_to_element_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    def ctrl_key_group(self, key, content):
        if key.upper() == 'CONTROL':
            key = Keys.CONTROL
        elif key.upper() == 'CONTROL':
            key = Keys.ALT
        elif key.upper() == 'SHIFT':
            key = Keys.SHIFT
        ActionChains(self.driver).key_down(key).send_keys(content).key_down(key).perform()

    def screentshot_as_file(self, *screentshot_path):
        if len(screentshot_path) == 0:
            screentshot_filepath = local_config.get_screentshot_path
        else:
            screentshot_filepath = screentshot_path[0]
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        screentshot_filepath = os.path.join(os.path.dirname(__file__), screentshot_filepath, 'UITtest_screentshot%s.png'%now)
        return self.driver.save_screenshot(screentshot_filepath)

    # selenium执行js脚本
    def execute_js_script(self, js_str, element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, None)


if __name__ == '__main__':
    pass
