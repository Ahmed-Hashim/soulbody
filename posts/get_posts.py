"""import requests
from bs4 import BeautifulSoup
import threading
from concurrent.futures import ThreadPoolExecutor

adslinks = []

ads = []
link = "https://almazadi.com/en/search?_token=YeuJnSSKYGLXH44dSfHRvWHTKa2XA8M7UQ4XgoSp&postedDate=2"


def get_pages_count(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    pagnation = soup.find_all('li', class_='page-item')

    try:
        pagecount = pagnation[-2].text
        return int(pagecount)+1
    except:
        pagecount = 1
        return int(pagecount)


def get_add_details(link):
    # print(f"Ad Link : {link}")
    ad = requests.get(link)
    adsoup = BeautifulSoup(ad.content, 'html.parser')
    add_categorty = adsoup.find('span', class_="category").text.strip()
    adimage = adsoup.find("ul", class_="bxslider")
    adimagelinks = adimage.find_all("li")
    adimagelink = adimagelinks[0].find('img')['src']
    adtitle = adsoup.find(
        'h2', class_="enable-long-words").find('strong').text.strip()
    adowner = adsoup.find('span', class_="name").find_all("a")[0].text.strip()
    add_details = {
        'link': link,
        'add_image': adimagelink,
        'add_title': adtitle,
        'add_owner': adowner,
        'category': add_categorty
    }
    ads.append(add_details)


def get_ads(pagecount):
    print(pagecount)
    if pagecount == 1:
        page = requests.get(
            f"https://almazadi.com/en/search?_token=YeuJnSSKYGLXH44dSfHRvWHTKa2XA8M7UQ4XgoSp&postedDate=2")
        soup = BeautifulSoup(page.content, 'html.parser')
        postsList = soup.find_all("h5", class_='add-title')
        for link in postsList:
            ads_link = link.find('a')['href']
            adslinks.append(ads_link)
        return adslinks
    else:
        for i in range(1, pagecount):
            page_number = i
            print(f"page number : {page_number}/{pagecount-1}")
            page = requests.get(
                f"https://almazadi.com/en/search?_token=YeuJnSSKYGLXH44dSfHRvWHTKa2XA8M7UQ4XgoSp&postedDate=2&page={page_number}")
            soup = BeautifulSoup(page.content, 'html.parser')
            postsList = soup.find_all("h5", class_='add-title')
            for link in postsList:
                ads_link = link.find('a')['href']
                adslinks.append(ads_link)
        return adslinks


def main():
    print('start_cheking')
    pagescount = get_pages_count(link)
    ads_link = get_ads(pagescount)
    ads_count = 0
    print("Working on {} ads".format(len(ads_link)))
    print(f"page Count : {pagescount}")
    with ThreadPoolExecutor() as exec:
        exec.map(get_add_details, get_ads(pagescount))
    return ads


def products_checking():
    print('start_cheking')
    pagescount = get_pages_count(link)
    ads_link = set(get_ads(pagescount))
    ads_count = 0
    print("Working on {} ads".format(len(ads_link)))
    for ad_link in ads_link:
        get_add_details(ad_link)
        ads_count += 1

    return ads
"""