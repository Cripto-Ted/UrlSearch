from bs4 import BeautifulSoup
import requests
import time
print('Привет, меня зовут UrlSearh, и я помогаю найти ссылки и текст на сайтах.')
time.sleep(3)
url = input('Введите сайт на котором вы хотите найти ссылки/текст: ')

# Запрос к сайту
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Поиск всех ссылок на странице
    links = [a['href'] for a in soup.find_all('a', href=True)]
    texts = [p.get_text(strip=True) for p in soup.find_all('p')]
    texts1 = [p.get_text(strip=True) for p in soup.find_all('div')]
    texts2 = [p.get_text(strip=True) for p in soup.find_all('span')]
    texts3 = [p.get_text(strip=True) for p in soup.find_all('h1')]
    texts4 = [p.get_text(strip=True) for p in soup.find_all('h2')]
    print("\nСсылки на сайте:")
    time.sleep(2)
    for link in links:
        if "https" in link or "http" in link:
            print(link)
            time.sleep(0.1)
    print("\nТекст на странице:")
    time.sleep(2)
    for text in texts:
        print(text)
        time.sleep(0.1)
    time.sleep(2)
    for text in texts1:
        print(text)
        time.sleep(0.1)
    time.sleep(2)
    for text in texts2:
        print(text)
        time.sleep(0.1)
    time.sleep(2)
    for text in texts3:
        print(text)
        time.sleep(0.1)
    time.sleep(2)
    for text in texts4:
        print(text)
        time.sleep(0.1)
else:
    print(f"Не удалось получить данные с сайта. Статус-код: {response.status_code}")
