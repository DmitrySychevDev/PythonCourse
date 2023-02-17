from bs4 import BeautifulSoup
import requests


def parse():
    try:
        url = "https://auto.drom.ru/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        if page.status_code != 200:
            raise Exception("Connection error")
        cards = soup.findAll("a", class_="css-xb5nz8 e1huvdhj1")

        with open("output.txt", "w") as file:
            for card in cards:
                title = card.find("span", attrs={"data-ftid": "bull_title"}).text.strip()
                descriptionItems = card.findAll("span", attrs={"data-ftid": "bull_description-item"})
                description = ""
                price = card.find("span", attrs={"data-ftid": "bull_price"}).text.strip().replace(" "," ")
                for item in descriptionItems:
                    description += item.text.strip()
                file.write("Наименование:{0} Описание:{1} Цена:{2} \n".format(title, description, price))

    except Exception as e:
        print(e)


parse()
