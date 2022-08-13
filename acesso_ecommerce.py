from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

campoUsername = driver.find_element(By.ID, 'user-name').send_keys("standard_user")
campoPassword = driver.find_element(By.ID, 'password').send_keys("secret_sauce")
btnLogin = driver.find_element(By.ID, 'login-button').click()
time.sleep(2)

btnOrdenarPreco = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]').click()
btnAddCart = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
btnAddCart2 = driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()
time.sleep(2)
btnCarrinho = driver.find_element(By.ID, 'shopping_cart_container').click()
btnCheckout = driver.find_element(By.ID, 'checkout').click()

campoFirstName = driver.find_element(By.ID, 'first-name').send_keys("Wallison")
campoLastName = driver.find_element(By.ID, 'last-name').send_keys("Alves Dantas")
campoPostalCode = driver.find_element(By.ID, 'postal-code').send_keys("58400515")
time.sleep(2)

btnContinue = driver.find_element(By.ID, 'continue').click()
btnFinish = driver.find_element(By.ID, 'finish').click()
