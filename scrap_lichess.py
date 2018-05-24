from selenium import webdriver
import time

options = webdriver.ChromeOptions()
#options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://lichess.org/@/grossmendPro')

driver.implicitly_wait(5)

driver.find_element_by_xpath("//a[@class='intertab to_games ']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[@class='intertab to_rated']").click()

gamelist = driver.find_elements_by_xpath("//a[@class='game_link_overlay']")

for game in gamelist:
    game.click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//a[@data-panel='fen_pgn']").click()
    print(driver.find_element_by_xpath("//div[@class='pgn']").text)
    driver.execute_script("window.history.go(-1)")

html = driver.page_source
print(len(html))