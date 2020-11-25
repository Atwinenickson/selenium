from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

el = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(el)

#select by visible text
# drp.select_by_visible_text("Morning")

#select by index
drp.select_by_index(2)

#select by value
# drp.select_by_value("Radio-2")