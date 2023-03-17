from bs4 import BeautifulSoup
import requests as re
import pandas as pd

data = {"spotahome_title" :[],
        "spotahome_room_type" :[],
        "spotahome_availability" :[],
        "spotahome_price"  : [] }

def start_scraper( url):
    # HEADERS = ({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', 'Accept-Language':'en-us'})
    
    # webpage = re.get(url, headers = HEADERS)
    webpage = re.get(url)

    soup = BeautifulSoup(webpage.content, 'html.parser')

    

    title = soup.find_all('p', attrs = {'class': 'homecard-content__title__HomecardContent___OmV4c homecard-content__title--rebranding-style__HomecardContent___OmV4c'})
    for i in title:
        data["spotahome_title"].append(i.text.strip())

    room_type = soup.find_all('span', attrs = {'class': 'homecard-content__type__HomecardContent___OmV4c homecard-content__type--rebranding-style__HomecardContent___OmV4c'})
    for i in room_type:
        data["spotahome_room_type"].append(i.text.strip())

    availability = soup.find_all('span', attrs = {'class': 'homecard-content__available-from__HomecardContent___OmV4c homecard-content__available-from--rebranding-style__HomecardContent___OmV4c'})
    for i in availability:
        data["spotahome_availability"].append(i.text.strip())

    price = soup.find_all('span', attrs = {'class': 'price__Price___OmV4c'})
    for i in price:
        data["spotahome_price"].append(i.text.strip())
    
    return  data  



def run_spotahome_etl():
    for i in range (2):
        page_number = i
        city = "milan"
        url = f"https://www.spotahome.com/s/{city}--italy/page:{i}"
        start_scraper(url)

    df = pd.DataFrame.from_dict(data)
    df.to_csv("s3://satvik-data-pipeline-bucket/Test1.csv")









