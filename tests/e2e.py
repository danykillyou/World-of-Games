from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
def test_scores_service():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=Options())
    driver.get("http://127.0.0.1:5000")
    x=driver.find_element(By.XPATH,"/html/body/h1/div").text
    print(x)
    return 1<int(x)<100


def main_function():
    if test_scores_service():
        return 0
    return -1

