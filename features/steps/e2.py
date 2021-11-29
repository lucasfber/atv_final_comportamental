from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


@given("a user is logged and is on the Create Education Institution page e2")
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

    context.driver.get('https://test.jasgme.com/en/administrator/institutions/create-institution')


@when('he does not provide the Education Institution name and clicks on the Save button')
def when(context):
    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="body"]/div/form/div[1]/div[1]/input')))


    # name_input = context.driver.find_element_by_xpath('//*[@id="body"]/div/form/div[1]/div[1]/input')
    # name_input.send_keys('Instituion XYZ')

    cep_input = context.driver.find_element_by_xpath('//*[@id="body"]/div/form/div[2]/div[1]/input')
    cep_input.send_keys('62748012')

    address_input = context.driver.find_element_by_xpath('//*[@id="body"]/div/form/div[2]/div['
                                                      '2]/input')
    address_input.send_keys('Address XYZ')

    number_input = context.driver.find_element_by_xpath('//*[@id="body"]/div/form/div[3]/div['
                                                      '1]/input')
    number_input.send_keys('101')

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.ID, 'country')))

    sel_country_elem = context.driver.find_element_by_id('country')
    select_country = Select(sel_country_elem)
    sel_country_elem.click()
    select_country.select_by_visible_text('Brasil')

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.ID, 'state')))

    sel_state_elem = context.driver.find_element_by_id('state')
    select_state = Select(sel_state_elem)
    sel_state_elem.click()
    select_state.select_by_visible_text('Alagoas')

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.ID, 'city')))

    sel_city_elem = context.driver.find_element_by_id('city')
    select_city = Select(sel_city_elem)
    sel_city_elem.click()
    select_city.select_by_visible_text('Maceió')

    context.driver.execute_script('''
       document.getElementsByTagName('app-chat')[0].remove()
    ''')

    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="change"]')))

    btn = context.driver.find_element_by_xpath('//*[@id="change"]')
    btn.click()


@then('the platform should show him an error message e2')
def then(context):
    WebDriverWait(context.driver, 20).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="body"]/div/form/div[1]/div[1]/app-errors/div')))
    context.driver.quit()