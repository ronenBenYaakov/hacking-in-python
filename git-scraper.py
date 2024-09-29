from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager

service = Service(r"C:\developer\chromedriver.exe")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s)
#driver = webdriver.Chrome(service= service)

driver.get("https://www.amazon.com/%D7%90%D7%9C%D7%97%D7%95%D7%98%D7%99%D7%AA-%D7%9C%D7%99%D7%AA%D7%99%D7%95%D7%9D-%D7%97%D7%A9%D7%9E%D7%9C%D7%99%D7%AA-%D7%9E%D7%94%D7%99%D7%A8%D7%95%D7%AA-%D7%99%D7%97%D7%99%D7%93%D7%95%D7%AA/dp/B07CR1GPBQ/ref=asc_df_B07CR1GPBQ/?tag=ilgogshpadde-20&linkCode=df0&hvadid=621144167450&hvpos=&hvnetw=g&hvrand=2594552273509470963&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9198958&hvtargid=pla-566961491980&psc=1&language=he_IL&mcid=201c470fa7443dc8b52932c983f95a9d")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)
driver.quit()