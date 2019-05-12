from bs4 import BeautifulSoup
import requests
import time



def check_enrollment(course):
    '''Checks UNSW timetable if class is available.'''

    url = 'http://timetable.unsw.edu.au/2019/' + course + '.html'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Luckily only the contents of classes have class rowLowlight
    sessions = soup.find_all('tr', 'rowLowlight')
    for session in sessions:
        enrollment = [e.string for e in session if e.string != '\n'][5].split('/')
        time_now = time.strftime('%H:%M:%S')
        print(f'{time_now} {course} enrolled:{enrollment[0]}, capacity:{enrollment[0]}')
        if enrollment[0] < enrollment [1]:
            return True

    return False
