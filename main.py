import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

url = "https://monkeytype.com/"
driver.get(url)
time.sleep(5)  # Let the page load

typing_speed_wpm = 10000  # words per minute
typing_delay = 60 / typing_speed_wpm

driver.find_element("tag name", "body").click()

while True:
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    active_word = soup.find("div", class_="word active")

    if active_word:
        letters = active_word.get_text(strip=True)
        actions = ActionChains(driver)
        for letter in letters:
            actions.send_keys(letter)
            time.sleep(typing_delay)
        actions.send_keys(" ").perform()
    else:
        break

time.sleep(500)
driver.quit()
