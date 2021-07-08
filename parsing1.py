import csv
import requests
from bs4 import BeautifulSoup
def get_html(url):
    response = requests.get(url)
    return response.text



def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    product_list = soup.find("ul",class_= "posts-items").find_all("li")

    for product in product_list:
        try:
            photo = product.find("a",class_="post-thumb").find("img").get("src")
        except:
            photo = ""   
        try:
            link = product.find("a",class_="post-thumb").get("href")
        except:
            link = ""
        try:
            title = product.find("div", class_ = "post-details").find("h2", {"class":"post-title"}).find("a").text
        except:
            title = ""
        data = {"link":link.strip().replace('\n', ''), "photo":photo, "title": title.strip().replace('\n', '')}
        write_to_csv(data)

def write_to_csv(data):
    with open("agro.csv", "a") as csv_file:
        writer = csv.writer(csv_file, delimiter="/")
        writer.writerow((data["photo"], data["link"], data["title"]))


def main():
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/"
    get_html(agro_url)
    p1 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/2/"
    get_html(agro_url)
    p2 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/3/"
    get_html(agro_url)
    p3 = get_data(get_html(agro_url))
    agro1_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/4/"
    get_html(agro_url)
    p4 = get_data(get_html(agro1_url))
    agro1_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/5/"
    get_html(agro_url)
    p5 = get_data(get_html(agro1_url))
    agro1_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/6/"
    get_html(agro_url)
    p6 = get_data(get_html(agro1_url))
    agro1_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/7/"
    get_html(agro_url)
    p7 = get_data(get_html(agro1_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/8/"
    get_html(agro_url)
    p8 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/9/"
    get_html(agro_url)
    p9 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/10/"
    get_html(agro_url)
    p10 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/11/"
    get_html(agro_url)
    p11 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/12/"
    get_html(agro_url)
    p12 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/13/"
    get_html(agro_url)
    p13 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/14/"
    p14 = get_html(agro_url)
    get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/15/"
    get_html(agro_url)
    p15 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/16/"
    get_html(agro_url)
    p16 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/17/"
    get_html(agro_url)
    p17 = get_data(get_html(agro_url))
    agro_url = "https://agro.gov.kg/language/ru/category/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/page/18/"
    get_html(agro_url)
    p18 = get_data(get_html(agro_url))



main()