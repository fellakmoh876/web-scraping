# requests for fetching html of website
import requests
# Make the GET request to a url
r = requests.get('http://www.cleveland.com/metro/index.ssf/2017/12/case_western_reserve_university_president_barbara_snyders_base_salary_and_bonus_pay_tops_among_private_colleges_in_ohio.html')
# Extract the content
c = r.content
from bs4 import BeautifulSoup
# Create a soup object
soup = BeautifulSoup(c)

# Find the element on the webpage
main_content = soup.find('div', attrs = {'class': 'entry-content'})

# Extract the relevant information as text
content = main_content.find('ul').text