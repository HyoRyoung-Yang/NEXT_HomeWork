import requests
from bs4 import BeautifulSoup
import csv
from movie import data

file = open('movie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["제목","평점","이미지","감독","배우", "개봉일"])

MOVIE_URL = f'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(MOVIE_URL)
movie_soup = BeautifulSoup(movie_html.text,"html.parser")

movie_list_box = movie_soup.find("ul", {"class" : "lst_detail_t1"})
movie_list = movie_list_box.find_all('li')

final_result = data(movie_list)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['star'])
    row.append(result['img_src'])
    row.append(result['director'])
    row.append(result['act'])
    row.append(result['date'])
    writer.writerow(row)

print(final_result)