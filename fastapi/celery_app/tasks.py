from celery_app import app
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# import os

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  
options=chrome_options


@app.task
def find_competitions():
  remote_url = "http://selenium_scraper:4444/wd/hub"
  url = 'http://backend:8000/competitions'
  driver = webdriver.Remote(
    command_executor=remote_url,
    options=chrome_options
  ) 
  driver.get(url)
  competitions = {}
  counter = 1
  competition = driver.find_element(by=By.XPATH, value=f'/html/body/div/div/ul[{counter}]/li/span[2]')
  while competition:
    try:
      competition = driver.find_element(by=By.XPATH, value=f'/html/body/div/div/ul[{counter}]/li/span[2]')
      competition_date = driver.find_element(by=By.XPATH, value=f'/html/body/div/div/ul[{counter}]/li/span[4]')
      competition_end_date = driver.find_element(by=By.XPATH, value=f'/html/body/div/div/ul[{counter}]/li/span[6]')
      competitions[competition.text] = [competition_date.text, competition_end_date.text]
      counter += 1
      
    except NoSuchElementException:
      print(f"Something went wrong here Counter: {counter}")
      break
  driver.quit()
  return competitions