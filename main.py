from seleniumhandler import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import scrapy
import json

driver = new_driver()
driver.maximize_window()

# get a URL
get('https://leetcode.com/contest/weekly-contest-379/ranking/', driver)


time.sleep(20)

# Get the page source
page_source = driver.page_source

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(page_source, 'html.parser')
results_list = []
# Find and print username and country
for row in soup.select('#contest-app div.ranking-table-container__mOYm table.table tbody tr'):
  username_elem = row.select_one('td a.ranking-username span') or row.select_one('td a.ranking-username')
  country_elem = row.select_one('td span.country-name') or row.select_one('td span.country-name span')

  # Check if the elements are present
  if username_elem:
      username = username_elem.get_text(strip=True)
      if country_elem:
        country = country_elem['data-original-title']
      else:
        country = 'Unknown'
      results_list.append(({
                             'username': username,
                             'country': country
                         }))
  

start_page = 1
end_page = 100

# List to store results


for page_number in range(start_page, end_page + 1):
    # Construct the URL for each page
    url = f'https://leetcode.com/contest/weekly-contest-379/ranking/{page_number}/'

    # Get the page source
    get(url, driver)
    time.sleep(10)  # You might need to adjust this wait time

    # Parse the HTML with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    for row in soup.select('#contest-app div.ranking-table-container__mOYm table.table tbody tr'):
      username_elem = row.select_one('td a.ranking-username span') or row.select_one('td a.ranking-username')
      country_elem = row.select_one('td span.country-name') or row.select_one('td span.country-name span')

      # Check if the elements are present
      if username_elem:
          username = username_elem.get_text(strip=True)
          if country_elem:
            country = country_elem['data-original-title']
          else:
            country = 'Unknown'
          results_list.append(({
                                 'username': username,
                                 'country': country
                             }))
    

# Save the results to a JSON file
with open('leetcode_results.json', 'w') as json_file:
    json.dump(results_list, json_file, indent=2)

# Close the WebDriver
driver.quit()