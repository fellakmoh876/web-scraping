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

# Create a pattern to match names
name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)
# Find all occurrences of the pattern
names = name_pattern.findall(content)

# Make school pattern and extract schools
school_pattern = re.compile(r'(?:,|,\s)([A-Z]{1}.*?)(?:\s\(|:|,))')
schools = school_pattern.findall(content)
# Pattern to match the salaries
salary_pattern = re.compile(r'\$.+')
salaries = salary_pattern.findall(content)

# Messy salaries
salaries = ['$876,001', '$543,903', '$2453,896']
# Convert salaries to numbers in a list comprehension 
[int(''.join(s[1:].split(','))) for s in salaries]