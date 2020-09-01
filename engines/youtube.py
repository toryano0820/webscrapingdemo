from lxml import etree, html
import requests
import json
import re


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
}


def get_list(query: str) -> list:
    url = f'https://www.youtube.com/results?search_query={query}'
    content = requests.get(url, headers=HEADERS).content
    tree = html.fromstring(content)
    script = tree.xpath('//script[contains(text(), \'window["ytInitialData"] = \')]')[0]
    yt_data = json.loads(re.findall(r"{.*}", script.text)[0])
    yt_contents = yt_data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"]
    data = []
    for content in yt_contents:
        if "itemSectionRenderer" in content:
            for sub_content in content["itemSectionRenderer"]["contents"]:
                if "videoRenderer" in sub_content:
                    video_data = sub_content["videoRenderer"]
                    item_obj = {
                        'url': 'https://www.youtube.com/watch?v=' + video_data["videoId"],
                        'title': video_data["title"]["runs"][0]["text"],
                        'labels': []
                    }

                    if "badges" in video_data:
                        badges = video_data["badges"]
                        item_obj["labels"] = [b["metadataBadgeRenderer"]["label"] for b in badges]

                    if "LIVE NOW" not in [l.upper() for l in item_obj["labels"]]:
                        data.append(item_obj)

    return data


if __name__ == "__main__":
    print(get_list('programming'))
