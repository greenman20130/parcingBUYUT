import requests
from bs4 import BeautifulSoup as BS


source = requests.get('https://www.bayut.com/index/sale-prices-apartments-dubai.html').text
soup = BS(source, 'lxml')
data = soup.find(class_='residential related-detail no-border').find_all(class_="left")

#счетчик для скипа названий
titles_count = 0 
#счетчик для распределения колонок
columns_count = 0


hotels = {}
for item in data:
    if titles_count > 5:
        item_text = item.text
        item_text = item_text.replace('\n', '')
        item_text = item_text.replace('  ', '')

        if columns_count == 0:
            #удаляем пробелы в конце, если такие имеются
            while True:
                if item_text[-1] == " ":
                    item_text = item_text[:-1]
                else:
                    break
            last_name_hotel = item_text
            hotels[last_name_hotel] = {}
            columns_count += 1

        elif columns_count == 1:
            hotels[last_name_hotel]['index'] = item_text
            columns_count += 1
        
        elif columns_count == 2:
            hotels[last_name_hotel]['price'] = item_text
            columns_count += 1
        
        elif columns_count == 3:
            hotels[last_name_hotel]['3m'] = item_text
            columns_count += 1
        
        elif columns_count == 4:
            hotels[last_name_hotel]['6m'] = item_text
            columns_count += 1
        
        elif columns_count == 5:
            hotels[last_name_hotel]['1y'] = item_text
            columns_count = 0 

    else:
        titles_count += 1


for key, value in hotels.items():
    print(key, value)
    print("-" * 70) 
