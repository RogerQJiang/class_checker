from bs4 import BeautifulSoup
import requests

def check_class(course):
    url = 'http://timetable.unsw.edu.au/2019/' + course + '.html'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    sessions = soup.find_all('tr', 'rowLowlight')
    for session in sessions:
        enrollment = [e.string for e in session if e.string != '\n'][5].split('/')
        if enrollment[0] < enrollment [1]:
            return True

    return False
