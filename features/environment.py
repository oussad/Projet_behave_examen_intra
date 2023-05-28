import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
def before_scenario(context,driver):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshotfield',attachment_type=allure.attachment_type.PNG)
    else:
        if step.status=="passed":
            allure.attach(context.driver.get_screenshot_as_png(), name='screenshotpassed',attachment_type=allure.attachment_type.PNG)
