import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

topics = input("请输入关键词（关键词之间用逗号分隔）： ")
topics = re.split(',| ，', topics)
how = input("每条搜索是否打开新窗口（是：1，不是：0）： ")

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