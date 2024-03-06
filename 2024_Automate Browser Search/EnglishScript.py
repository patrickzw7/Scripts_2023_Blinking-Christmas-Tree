from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re

options = Options()
options.add_experimental_option("detach", True)

topics = input("Please input the keywords you want to search (split with commas): ")
topics = re.split(',| ，', topics)
how = input("Whether you would like a separate window pop up for each keyword you want to search (1 for yes and 0 for no): ")

# Initialize the browser

if how == "0":
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    for topic in topics:
        # Open under the same window
        browser.execute_script(f"window.open('https://www.baidu.com/s?wd={topic}')")
        browser.execute_script(f"window.open('https://www.bing.com/search?q={topic}')")
        browser.execute_script(f"window.open('https://www.sogou.com/web?query={topic}')")
        browser.execute_script(f"window.open('https://www.so.com/s?q={topic}')")
else:
    for topic in topics:
        # Open in a new window or tab
        browser_new = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        browser_new.execute_script(f"window.open('https://www.baidu.com/s?wd={topic}')")
        browser_new.execute_script(f"window.open('https://www.bing.com/search?q={topic}')")
        browser_new.execute_script(f"window.open('https://www.sogou.com/web?query={topic}')")
        browser_new.execute_script(f"window.open('https://www.so.com/s?q={topic}')")