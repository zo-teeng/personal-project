import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

browser = webdriver.Chrome() # 웹드라이버 설치
browser.maximize_window()

url = 'https://flight.naver.com/'
browser.get(url)

begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click() # 가는 날이 쓰여있는 버튼을 클릭

# time.sleep(1) # 1초 대기
wait_until('//b[text() = "27"]')
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "27"]')))
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day27[0].click() # 여러 27일 중 0번째 27일을 클릭

wait_until('//b[text() = "31"]')
day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')
day31[0].click()

wait_until('//b[text() = "ICN"]')
departure = browser.find_element(By.XPATH, '//b[text() = "ICN"]')
departure.click()

wait_until('//button[text() = "국내"]')
domestic1 = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic1.click()

wait_until('//i[contains(text(), "KWJ")]')
dept = browser.find_element(By.XPATH, '//i[contains(text(), "KWJ")]')
dept.click()

wait_until('//b[text() = "도착"]')
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

wait_until('//button[text() = "국내"]')
domestic2 = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic2.click()

wait_until('//i[contains(text(), "GMP")]')
arri = browser.find_element(By.XPATH, '//i[contains(text(), "GMP")]')
arri.click()

wait_until('//span[contains(text(), "항공권 검색")]')
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

input('종료하려면 Enter 키를 입력하세요')
browser.quit()

# 왕복 항공권 검색