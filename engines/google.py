from lxml import etree, html
import requests


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
}


def get_weather(location: str, lang: str = 'en-US') -> dict:
    url = f'https://www.google.com/search?hl={lang}&q=weather in {location}'
    content = requests.get(url, headers=HEADERS).content
    tree = html.fromstring(content)
    abox = tree.xpath('//*[@id="rso"]/div[1]/div/div')[0]

    return {
        'location': abox.xpath('//*[@id="wob_loc"]')[0].text,
        'last_update': abox.xpath('//*[@id="wob_dts"]')[0].text,
        'description': abox.xpath('//*[@id="wob_dc"]')[0].text,
        'temperature_c': abox.xpath('//*[@id="wob_tm"]')[0].text,
        'temperature_f': abox.xpath('//*[@id="wob_ttm"]')[0].text,
        'precipitation': abox.xpath('//*[@id="wob_pp"]')[0].text,
        'humudity': abox.xpath('//*[@id="wob_hm"]')[0].text,
        'wind_kph': abox.xpath('//*[@id="wob_ws"]')[0].text,
        'wind_mph': abox.xpath('//*[@id="wob_tws"]')[0].text
    }


def get_time(location: str, lang: str = 'en-US') -> dict:
    url = f'https://www.google.com/search?hl={lang}&q=time in {location}'
    content = requests.get(url, headers=HEADERS).content
    tree = html.fromstring(content)
    abox = tree.xpath('//*[@id="rso"]/div[1]/div/div')[0]

    return {
        'time': abox.xpath('./div[1]')[0].text,
        'date': abox.xpath('./div[2]')[0].text_content().strip(),
        'description': abox.xpath('./span[1]')[0].text.strip()
    }


if __name__ == "__main__":
    print(get_weather('usa'))
    print(get_time('usa'))
