from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


@given("a user is logged and is on the Create Company page d1")
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
        By.ID, 'create')))

    context.driver.find_element_by_id('create').click()
    # context.driver.get('https://test.jasgme.com/en/administrator/list-companies/create-company')


@when('he enters a name and selects an edition with an educational institution both valid')
def when(context):
    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="body"]/div/form/div[1]/div[1]/input')))

    company_name_input = context.driver.find_element_by_xpath('//*[@id="body"]/div/form/div[1]/div[1]/input')
    company_name_input.send_keys('Company XYZ')

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="body"]/div/form/div[1]/div[2]/select')))

    select_elem = context.driver.find_element_by_xpath('//*[@id="body"]/div/form/div[1]/div[2]/select')
    select_edition = Select(select_elem)
    select_elem.click()
    select_edition.select_by_visible_text('A Diego Edition')

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="body"]/div/form/div[1]/div[3]/select')))

    select_elem_inst = context.driver.find_element_by_xpath('//*[@id="body"]/div/form/div[1]/div[3]/select')
    select_institution = Select(select_elem_inst)
    select_elem_inst.click()
    select_institution.select_by_visible_text('A Diego Institute')

    save_button = context.driver.find_element_by_id('change')
    save_button.click()


@then('the platform should show him a success message d1')
def then(context):
    WebDriverWait(context.driver, 50).until(expected_conditions.url_matches('https://test.jasgme.com/en/administrator/list-companies'))
    #
    # body = context.driver.find_element_by_id('body')
    # print(body.get_attribute('class'))
    # assert 'high-contrast' not in body.get_attribute('class').split()
    context.driver.quit()
