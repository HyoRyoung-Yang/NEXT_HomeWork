def data(movie_list):
    final_result = []
    for movie in movie_list:
        title = movie.find("dt", {"class" : "tit"}).find("a").text
        star = movie.find("div", {"class" : "star_t1"}).find("span", {"class" : "num"}).text
        img_src = movie.find("div", {"class" : "thumb"}).find("img")['src']

        mid = []
        mid = movie.find("dl", {"class" : "info_txt1"}).find_all("dd")
        
        director = mid[1].find("span", {"class" : "link_txt"}).find("a").text

        if len(mid) == 2:
            act = None
        else:
            temp = mid[2].find("span", {"class" : "link_txt"}).find_all("a")
            act = []
            for temp2 in temp:
                act.append(temp2.text)

        date = mid[0].text.replace('\n', '').replace('\t', '').replace('\r', '').split("|")[-1].replace("개봉", "")

        print(">>:",date)
        
        movie_info = {
            'title' : title,
            'star' : star,
            'img_src' : img_src,
            'director' : director,
            'act' : act,
            'date' : date
        }
        
        final_result.append(movie_info)
    return final_result