
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Firefox

driver=webdriver.Chrome()
#wait = WebDriverWait(driver, 20)

#driver.implicitly_wait(20) # seconds

#driver.get("http://somedomain/url_that_delays_loading")
#myDynamicElement = driver.find_element_by_id("myDynamicElement")

driver.get('http://www.python.org')

driver.get('http://orsk.ru/')
driver.find_element_by_link_text("Объявление").click()

driver.find_element_by_link_text("Войдите").click()
#driver.find_element_by_id("Имя пользователя:").send_keys("nexa2008") # Ввод символов
