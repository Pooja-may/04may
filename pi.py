from selenium import webdriver          ## importing selenuim module
driver = webdriver.Chrome()           ## create and and load chrome driver obejct
#####driver = webdriver.chrome()  dont use c small chrome             ## create and and load chrome driver obejct
###driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")             ## create and and load chrome driver obejct

driver.get("https://www.facebook.com")      ## open website/ url
driver.maximize_window()
print("Page title : ", driver.title)