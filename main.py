# bs link https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# class details http://timetable.unsw.edu.au/2019/COMP4418.html


from bs4 import BeautifulSoup
import requests


courses_t3 = ['COMP4418']#, 'COMP9444']

with open('soup.txt', 'w') as f:
    for course in courses_t3:
        url = 'http://timetable.unsw.edu.au/2019/' + course + '.html'
        response = requests.get(url)
        try:
            response.raise_for_status()
        except HTTPError as http_err:
            print('HTTP error has occured: {http_err}')
        except Exception as err:
            print('Not HTTP error has occured: {err}')
        else:
            soup = BeautifulSoup(response.text)
