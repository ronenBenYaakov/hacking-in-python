import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By

repo = input("paste url page to scrape ")
service = Service(r"C:\developer\chromedriver.exe")
driver = webdriver.Chrome(service= service)
driver.get(f"{repo}")
res = driver.find_elements(By.CLASS_NAME, "repo")


links = []
flink = []


def going_for_raw(second_page):
    driver.get(second_page)
    raw = driver.find_element(By.CLASS_NAME, "types__StyledButton-sc-ws60qy-0")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    if "password" in html:
        print(f"found password: {second_page}")

def loop(next_page):
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "Link--primary")
    for a in res2:
        if "sc" in a.text:
            second_page = f"{next_page}/blob/main/{a.text}"
        elif "py" in a.text:
            second_page = f"{next_page}/blob/main/{a.text}"
            going_for_raw(second_page)
            #print(second_page)
            #time.sleep(2)
for i in res:
    links.append(i.text)

for l in links:
    next_page = f"{repo}/{l}"
    flink.append(next_page)
    #print(flink)
    loop(next_page)

driver.quit()