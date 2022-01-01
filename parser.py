"""
Создать телеграм бот который читает данные из файла 'kloop.json'
И отправляет их в пользователю

Скинуть мне ссылку на телеграм бота для теста
"""



from bs4 import BeautifulSoup
import requests
import json

JSON = 'kloop.json'
URL = 'https://kloop.kg/news/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'  #Замените на свой Юзер агент
}

def get_content():
    r = requests.get(url=URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('article', class_='elementor-post')

    new_posts = []

    for item in items:
        new_posts.append({
            "title" : item.find('div', class_='elementor-post__text').find(
                'h3').find('a').get_text(strip=True),
            "data" : item.find('div',
                               class_='elementor-post__meta-data').find(
                'span', 'elementor-post-date').get_text(strip=True),
            'photo' : item.find('a', 'elementor-post__thumbnail__link').find(
                'div', 'elementor-post__thumbnail').find('img').get('src'),
            'link' : "None" # Плюс 1 бал если спарсите ссылку на новость
        })

    with open('news.json', 'w') as file:
        json.dump(new_posts, file, indent=4, ensure_ascii=False)


def main():
    get_content()


if __name__ == "__main__":
    main()
