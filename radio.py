from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

driver.find_element_by_xpath("//label[contains(text(),'Sunday')]").click()
driver.find_element_by_xpath("//label[contains(text(),'Wednesday')]").click()
driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[2]/div[17]/table[1]/tbody[1]/tr[7]/td[1]/label[1]").click()