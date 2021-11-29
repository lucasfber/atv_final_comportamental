from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


@given("a user is logged and is on the Create Company page d5")
def given(context):
    context.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()

    login_input = context.driver.find_element_by_id('login')
    login_input.send_keys('lucas.bertoldo@dellead.com')

    password_input = context.driver.find_element_by_id('inputPassword')
    password_input.send_keys('123')

    login_button = context.driver.find_element_by_id('btnLogin')
    login_button.click()

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="sidebar"]/div/div[1]/div/div[1]/img')))

    context.driver.get('https://test.jasgme.com/en/administrator/list-companies/create-company')


@when('he does not provide any data to the new company')
def when(context):
    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="body"]/div/form/div[1]/div[1]/input')))


@then('the Save button should remain disabled d5')
def then(context):
    WebDriverWait(context.driver, 20).until(expected_conditions.element_attribute_to_include((
        By.ID, 'change'), 'disabled'))
    context.driver.quit()