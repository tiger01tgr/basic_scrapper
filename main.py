import requests
from bs4 import BeautifulSoup
import csv

def main():

    URL = 'https://twitchtracker.com/channels/viewership/english'
    file = open("streamer_list.txt", mode = 'w')

    read_page(URL, file)




    for i in range(1, 4):
        URL = f'https://twitchtracker.com/channels/viewership/english?page={i}'
        read_page(URL, file)


    file.close()

def read_page(URL, file):

    page = requests.get(URL, headers={'User-Agent': 'Chrome'})

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("div", class_="table-responsive")

    results = results.find_all('tr')


    for result in results:
        streamer = result.find('a')

        try:
            name = streamer.get('href')
            pic = streamer.find(class_="img-circle")
            pic = pic.get('src')
            print([name, pic])
            file.write(f"['{name[1:]}', '{pic}']\n,")


        except:
            continue


if __name__ == '__main__':
    main()
