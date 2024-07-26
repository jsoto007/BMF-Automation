
import atexit
import re
import time
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




from selenium import webdriver


count = 1


driver = webdriver.Firefox()


driver.get("https://mpx.natera.com/log-in")

time.sleep(10)

user_name = driver.find_element("xpath", 
                                "//input[contains(@id, 'email')]")

keyboard = Controller()
user_name.click()

time.sleep(1)

keyboard.type('burdiercorp@gmail.com')

time.sleep(1)

pass_word = driver.find_element("xpath", 
                                "//input[contains(@id, 'password')]")

pass_word.click()

keyboard.type('Barahona@1030')

time.sleep(1)

# log_in = driver.find_element("xpath", 
#                              "//button[contains(@class, 'mdc-button__label')]")
# time.sleep(1)

# log_in.click()

time.sleep(30)



def checks_for_jobs():

  client_links = driver.find_elements("xpath", 
                             "//div[contains(@class, 'css-j7qwjs')][.//div[contains(@class, 'css-8v90jo')]]")

  time.sleep(1)

  for client_link in client_links:

      client_link_html = client_link.get_attribute("innerHTML")
      html_code = f"{client_link_html}"

      soup = BeautifulSoup(html_code, 'html.parser')

      span_tag = soup.find('span')

      if span_tag:
          miles = span_tag.text.strip()
          mile = re.findall('\d+', miles)
          total_miles = int(mile[0])
      else:
          print("No miles found error: 5555")

      time.sleep(1)
      if total_miles < 60: 
          print("I tried to click")
          job_opportunity = client_link.find_element("xpath", 
                                                    "//div[contains(@class, 'test-card__left-side')]")
          job_opportunity.click()
          time.sleep(4)

          accept_btn = driver.find_element("xpath", 
                                         "//button[contains(@class, '_button_qs46x_1 undefined _medium_qs46x_5 mdc-button mdc-button--unelevated')][.//span[contains(@class, 'mdc-button__label')]][.//span[text()[contains(., 'Accept')]]]")
          time.sleep(3)

          # accept_btn.click()
          print(":) just accepted a job!")
          time.sleep(2)
          driver.get("https://mpx.natera.com/jobs")
          time.sleep(20)
          
          driver.switch_to.window(driver.window_handles[0])
          break
      else:
          print("This Job is not under 60 miles :(")

      time.sleep(1)

starttime = time.monotonic()     

while True:
    checks_for_jobs()
    print(f"Just Checked for Jobs: {count}")
    count += 1
    time.sleep(1.0 - ((time.monotonic() - starttime) % 1.0))

    def restart_program():
      driver.get("https://mpx.natera.com/jobs")
      time.sleep(20)
      driver.switch_to.window(driver.window_handles[0])
      while True:
        
        checks_for_jobs()
        print(f"Just Checked for Jobs FROM RESTAER:")
        count = 1
        count += 1
        time.sleep(1.0 - ((time.monotonic() - starttime) % 1.0))

    atexit.register(restart_program)