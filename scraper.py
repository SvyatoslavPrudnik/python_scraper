import requests
from bs4 import BeautifulSoup
import pandas as pd


def run_scraper():
    html_data_list = []
    legend_data = get_legends()['devices']
    result = []
    for item in legend_data[20:40]:
        id = item['i']
        # print(item['i'])
        detail_data = get_map_data(id)
        # print(detail_data)
        html_data_list.append(detail_data)
        html = detail_data['content']
        soup = BeautifulSoup(html, 'html.parser')
        result.append(
            {
                'radiation': soup.find('b').text,
                'address': soup.findAll("p", {"class": "title"})[0].text,
                'date': soup.findAll("p", {"class": "updated"})[0].text,
                'source': soup.findAll("p", {"class": "source"})[0].text
            })
    print(result)
    df = pd.DataFrame(result)
    print(result)
    df.to_csv(r'export_dataframe.csv', index=False, header=True)


def get_legends():
    cookies = {
        '_ga': 'GA1.2.935412511.1660489973',
        '_gid': 'GA1.2.1841021113.1660489973',
        '_fbp': 'fb.1.1660489972789.1939586185',
        'XSRF-TOKEN': 'eyJpdiI6IlRoRU1lRFc2NEFab2tVcytjQWo0SFE9PSIsInZhbHVlIjoiMHBSejR2UFIySTZMQ2RWakd0NS94ZXNIVzJRZ3dOWk4xMnhxTFRPQVltYVRlaHhYY2RrakhPelpZUHFPNHJreHk5WDVjWHBIUEZKYSttYkRoTlgxUHlFZ1pGWk1VOWE3YzlicVBVV0dZZ1FzRzBvMW1udXE2aUllQWdYeGdja3kiLCJtYWMiOiJiMjkwZDkwYTMwYzNiM2QwOGQ1YTMzOWY0OGUzM2MwNDdiN2E0ZTM1MWU5NzZmYWE1MDJlMDIzMWVlYzQwNzdkIiwidGFnIjoiIn0%3D',
        'laravel_session': 'eyJpdiI6IlY5WjVHT2Y4V2x2QmpaNVl6VXpyQ0E9PSIsInZhbHVlIjoibkRwYkw3L0V3cENqbFBraUpieEwvMHcxbndNQzVrVERWZHpwL3huK2p3N0dyOXZjSHFyTkhmWlVOUGV5OWpoZDlVQXY5azlVTjYrOGdCMkdENlVlRGNFQnhkZm4vRW92T3BYQWRYYm5YZ3JzZDQySG5DdkJONkZsSnJLNUdLalgiLCJtYWMiOiJhMTczYmQ2MTExNTI1MGFhMjExNTQxN2IxMDcwMzdjMTdmYmQyODM4NTlmYTQ5NjVkY2NjNzE0NmRjMWVkNjdmIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'authority': 'www.saveecobot.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.935412511.1660489973; _gid=GA1.2.1841021113.1660489973; _fbp=fb.1.1660489972789.1939586185; XSRF-TOKEN=eyJpdiI6IlRoRU1lRFc2NEFab2tVcytjQWo0SFE9PSIsInZhbHVlIjoiMHBSejR2UFIySTZMQ2RWakd0NS94ZXNIVzJRZ3dOWk4xMnhxTFRPQVltYVRlaHhYY2RrakhPelpZUHFPNHJreHk5WDVjWHBIUEZKYSttYkRoTlgxUHlFZ1pGWk1VOWE3YzlicVBVV0dZZ1FzRzBvMW1udXE2aUllQWdYeGdja3kiLCJtYWMiOiJiMjkwZDkwYTMwYzNiM2QwOGQ1YTMzOWY0OGUzM2MwNDdiN2E0ZTM1MWU5NzZmYWE1MDJlMDIzMWVlYzQwNzdkIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IlY5WjVHT2Y4V2x2QmpaNVl6VXpyQ0E9PSIsInZhbHVlIjoibkRwYkw3L0V3cENqbFBraUpieEwvMHcxbndNQzVrVERWZHpwL3huK2p3N0dyOXZjSHFyTkhmWlVOUGV5OWpoZDlVQXY5azlVTjYrOGdCMkdENlVlRGNFQnhkZm4vRW92T3BYQWRYYm5YZ3JzZDQySG5DdkJONkZsSnJLNUdLalgiLCJtYWMiOiJhMTczYmQ2MTExNTI1MGFhMjExNTQxN2IxMDcwMzdjMTdmYmQyODM4NTlmYTQ5NjVkY2NjNzE0NmRjMWVkNjdmIiwidGFnIjoiIn0%3D',
        'referer': 'https://www.saveecobot.com/radiation-maps',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get('https://www.saveecobot.com/storage/maps_data.js?date=2022-08-14T1535:29',
                            headers=headers)

    return response.json()

def get_map_data(marker_id):

    headers = {
        'authority': 'www.saveecobot.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = {
        'marker_id': f'{marker_id}',
        'marker_type': 'device',
        'pollutant': 'gamma',
        'is_wide': '1',
        'is_iframe': '0',
        'is_widget': '0',
        'rand': '2022-08-14T16-08:15',
    }

    response = requests.get('https://www.saveecobot.com/maps/marker.json', params=params, headers=headers)

    return response.json()
