from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given("a user with a valid username")
def given(context):
    context.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()


@when('he enters only his username')
def when(context):
    login_input = context.driver.find_element_by_id('login')
    login_input.send_keys('lucas.bertoldo@dellead.com')


@then('the Sign In button should remain disabled')
def then(context):
    WebDriverWait(context.driver, 20).until(expected_conditions.element_attribute_to_include((
        By.ID, 'btnLogin'), 'disabled'))
    context.driver.quit()