import requests
from bs4 import BeautifulSoup as bs


def search(keyword):
    kw = keyword.replace(" ", "+")
    link = "https://anikyojin.net/?s="+kw+"&post_type=post"
    main_page = requests.get(link)
    soup = bs(main_page.content, 'lxml')
    card = soup.findAll('article', class_="artikel")

    nama_anime_arr = []
    link_anime_arr = []

    for i in card:
        href = i.find('a')
        nama_anime = href['title']
        link_anime = href['href']
        nama_anime_arr.append(nama_anime)
        link_anime_arr.append(link_anime)

    for x in range(1, len(nama_anime_arr)+1):
        print(str(x) + "." + nama_anime_arr[x - 1] + "\n")

    ans = input("Pilih anime :")

    try:
        if ans == "0":
            print("Gagal")
        else:
            url_anime = link_anime_arr[int(ans) - 1]
            page_anime = requests.get(url_anime)
            get = bs(page_anime.content, 'lxml')
            findAllDiv = get.findAll('div', class_="downloadcloud")

            for title in findAllDiv:
                print("==========================================")
                print(title.find('h2').text + "\n")
                for x in title.findAll('li'):
                    print(x.find('strong').text)
                    print(x.find('a')['href']+"\n")

    except:
        print("Gagal")


# def download(link):
#     link_download = link
#     main_page = requests.get(link_download)
#     soup = bs(main_page.content, 'lxml')


# Progressssss


search(input("Cari anime : "))
