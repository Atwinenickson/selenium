from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

inputboxes = driver.find_elements_by_class_name("text_field")

print(len(inputboxes))

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Nikson')