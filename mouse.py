from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input').send_keys("Admin")
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input').send_keys("admin123")
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input').click()

admin = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/a/b')
user_mgt = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a')
users = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a')

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_mgt).move_to_element(users).click().perform()



