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
from common.log_utils import local_logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        local_logger.info('打开url:{}'.format(url))

    def set_browser_max(self):
        self.driver.maximize_window()
        local_logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        local_logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        local_logger.info('刷新浏览器')

    def close_table(self):
        self.driver.close()
        local_logger.info('关闭table页')

    def exit_driver(self):
        self.driver.quit()
        local_logger.info('关闭浏览器')

    def wait(self, wait_time=local_config.get_time_out):
        time.sleep(wait_time)
        local_logger.info('等待时间：{}秒'.format(wait_time))

    def implicitly(self, wait_time=local_config.get_time_out):
        self.driver.implicitly_wait(wait_time)
        local_logger.info('显示等待时间：{}秒'.format(wait_time))

    def get_title(self):
        value = self.driver.title
        local_logger.info('获取浏览器title：{}'.format(value))
        return value

    # 封装元素操作
    def find_element(self, element_info):
        """
        根据提供的元素信息查找元素
        :param element_info:元素信息，字典类型{...}
        :return:element对象
        """
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
        elif locator_type_name == 'link_text':
            locator_type = By.LINK_TEXT
        element = WebDriverWait(self.driver, locator_timeout).until(lambda x: x.find_element(locator_type,
                                                                                             locator_value_info))
        # element = WebDriverWait(self.driver, locator_timeout).until(EC.visibility_of_element_located(locator_type, locator_value_info))
        local_logger.info('查找元素信息element：{}'.format(element_info))
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
        local_logger.info('切换frame')

    def switch_to_alert(self, action='accept', time_out=local_config.get_time_out):
        alert = WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert_text = alert.text
        if action.lower() == 'accept':
            alert.accept()
        elif action.lower() == 'dismiss':
            alert.dismiss()
        local_logger.info('切换至弹窗，返回弹窗文本：{}'.format(alert_text))
        return alert_text

    def get_window_handle(self):
        local_logger.info('获取当前窗口句柄：{}'.format(self.driver.current_window_handle))
        return self.driver.current_window_handle

    def switch_to_window_by_handle(self, window_handle):
        local_logger.info('切换浏览器句柄：{}'.format(window_handle))
        return self.driver.switch_to.window(window_handle)

    def switch_to_window_by_tittle(self, title):
        handles = self.driver.window_handles
        for window_handle in handles:
            if WebDriverWait(self.driver, local_config.get_time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break
        local_logger.info('根据title切换浏览器句柄，title:{},浏览器句柄:{}'.format(title, window_handle))

    def switch_to_window_by_url(self, url):
        handles = self.driver.window_handles
        for window_handle in handles:
            if WebDriverWait(self.driver, local_config.get_time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break
        local_logger.info('根据url切换浏览器句柄，title:{},浏览器句柄:{}'.format(url, window_handle))

    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        local_logger.info('点击元素element:{}'.format(element_info))

    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        local_logger.info('element:{} 输入框输入:{}'.format(element_info, content))

    # 鼠标、键盘事件封装（建议先判断操作系统类型）
    def click_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).click(element).perform()
        local_logger.info('鼠标左击元素element:{}'.format(element_info))

    def right_click_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).context_click(element).perform()
        local_logger.info('鼠标右击元素element:{}'.format(element_info))

    def double_click_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).double_click(element).perform()
        local_logger.info('鼠标双击元素element:{}'.format(element_info))

    def move_to_element_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()
        local_logger.info('鼠标移动至元素element:{}'.format(element_info))

    def ctrl_key_group(self, key, content):
        if key.upper() == 'CONTROL':
            key = Keys.CONTROL
        elif key.upper() == 'CONTROL':
            key = Keys.ALT
        elif key.upper() == 'SHIFT':
            key = Keys.SHIFT
        ActionChains(self.driver).key_down(key).send_keys(content).key_down(key).perform()
        local_logger.info('键盘组合按键:{} + {}'.format(key, content))

    def screentshot_as_file(self, *screentshot_path):
        if len(screentshot_path) == 0:
            screentshot_filepath = local_config.get_screentshot_path
        else:
            screentshot_filepath = screentshot_path[0]
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        screentshot_filepath = os.path.join(os.path.dirname(__file__), screentshot_filepath, f'UITtest_screentshot_{now}.png')
        local_logger.info('截图路径:{}'.format(screentshot_filepath))
        return self.driver.save_screenshot(screentshot_filepath)

    # selenium执行js脚本
    def execute_js_script(self, js_str, element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, None)
        local_logger.info('js脚本执行 element：{},js脚本：{}'.format(element_info, js_str))


if __name__ == '__main__':
    pass
