from selenium import webdriver
import time
import string    
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import random

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)
driver.set_window_size(2048,1536)

count = 0

with open("report.txt") as f:
    for line in f:
        url = line.strip()  # to remove the trailing \n
        count = count +1

        driver.get(url)
    
        time.sleep(5)  
        element = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article')

        result = ''.join((random.choice(string.ascii_lowercase) for x in range(6)))

        comb = f'{count}''.png'

        time.sleep(3)
        element.screenshot(comb)

        print('Success screenshot : ',comb)