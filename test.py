# from selenium import webdriver

# # Create an instance of Chrome WebDriver
# driver = webdriver.Chrome()

# # Open a website
# driver.get("https://www.google.com")
# print(driver.title)
# print(driver.current_url)


# # driver.quit()  # Closes all browser windows
# # driver.close()  # Closes the current browser window

# # Locating Elements
# # By ID:
# element = driver.find_element_by_id('element_id')

# # By Name:
# element = driver.find_element_by_name('element_name')

# # By Class Name:
# element = driver.find_element_by_class_name('element_class')

# # By XPath:
# element = driver.find_element_by_xpath('//tag[@attribute="value"]')

# # By CSS Selector:
# element = driver.find_element_by_css_selector('css_selector')

# # By Link Text:
# element = driver.find_element_by_link_text('Link Text')

# # Interacting with Web Elements
# element.click()

# # Typing in a Text Box:
# element.send_keys('Your text here')

# # Clearing Text from a Text Box:
# element.clear()

# # Getting Text of an Element:
# print(element.text)

# # Getting an Element's Attribute:
# value = element.get_attribute('attribute_name')


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define Chrome options (for example, running in headless mode)
options = Options()

import pdb; pdb.set_trace()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
