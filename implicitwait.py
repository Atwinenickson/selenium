from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

textbox_username_id="Email"
textbox_password_id="Password"
button_login_xpath="//body/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/input[1]"
link_logout_linktext="Logout"


driver.implicitly_wait(10  )
driver.find_element_by_id(textbox_username_id).clear()
el = driver.find_element_by_id(textbox_username_id).send_keys("username")
driver.find_element_by_id(textbox_password_id).clear()
ep = driver.find_element_by_id(textbox_password_id).send_keys("password")
driver.find_element_by_xpath(button_login_xpath).click()
# assert "Customers" in driver.find_element_by_xpath("//body/div[3]/div[2]/div[1]/ul[1]/li[4]/a[1]/span[1]")

# el = driver.find_element_by_xpath("//body/div[3]/div[2]/div[1]/ul[1]/li[4]/a[1]/span[1]").send_keys("sybyl")
# print(el)

if el:
    print("el")
    print(el)
else:
    print('nothing')

driver.close()