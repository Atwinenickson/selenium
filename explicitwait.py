from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

action = ActionChains(driver)

driver.find_element(By.LINK_TEXT,"Flights").click()
# driver.find_element(By.CLASS_NAME, 'uitk-faux-input').send_keys("Kigali")


# time.sleep(5) 
# wait = WebDriverWait(driver, 10)
# el = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]")))
# el.click()
# print("here")
# print(el)
# print("pop")
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@class="zsg-button_primary contact-submit-button track-ga-event"]')))
# action.send_keys(Keys.COMMAND+Keys.ALT+'i')
# action.perform()
# driver.find_element_by_css_selector("body.uitk-no-outline:nth-child(2) div.app-layer-base--active div.uitk-grid.pageWhiteBackground:nth-child(1) div.uitk-cell.Storefront-Homepage div.uitk-cell:nth-child(1) div.StorefrontWizardRegionBEX.all-b-margin-six:nth-child(3) figure.uitk-image.bexHeroImageFigure div.wizardCard.all-t-padding-twelve.all-x-padding-six.SimpleContainer div.uitk-card-aloha.uitk-card-aloha-roundcorner-all.all-b-padding-six.all-cell-1-1.elevation-4 div.uitk-tabs-container div.uitk-tabs-content div.uitk-tabs-pane.active:nth-child(2) div.wizardOverHeroImage.all-x-padding-six form.WizardFlightPWA div.uitk-tabs-container:nth-child(2) div.uitk-tabs-content div.uitk-tabs-pane.active:nth-child(1) div.uitk-layout-grid.uitk-layout-grid-gap-three.uitk-layout-grid-columns-small-4.uitk-layout-grid-columns-medium-6.uitk-layout-grid-columns-large-12.uitk-spacing.uitk-spacing-margin-blockstart-three div.uitk-layout-grid-item.uitk-layout-grid-item-columnspan-small-4.uitk-layout-grid-item-columnspan-medium-6.uitk-layout-grid-item-columnspan-large-8:nth-child(1) div.uitk-layout-grid.uitk-layout-grid-gap-three.uitk-layout-grid-columns-small-1.uitk-layout-grid-columns-medium-2.Location.locationWithSwap div.uitk-layout-grid-item.uitk-layout-grid-item-columnspan-small-1.uitk-layout-grid-item-columnspan-medium-1:nth-child(3) div:nth-child(1) div.uitk-typeahead div.uitk-field.has-floatedLabel-label.has-icon.has-no-placeholder > label.uitk-field-label.is-visually-hidden:nth-child(1)").send_keys("Kampala")
# try:
#     element = driver.find_element_by_xpath('//*[@id="location-field-leg1-destination-input"]').send_keys("Kampala")
# except Exception as e:
#     print(e)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div[2]/div/form/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/button').send_keys("Kampala")
# time.sleep(2)
# driver.find_element_by_id("d1-btn").send_keys("2020-12-04")

# time.sleep(2)
# driver.find_element_by_id("d2-btn").send_keys("2020-12-19")


# driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()