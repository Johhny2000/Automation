import requests
from bs4 import BeautifulSoup


def find_images_on_page(url):
    my_user_agent = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    response = requests.get(url, headers=my_user_agent)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        if 'src' in img.attrs:
            images.append(img['src'])
    return images

# Example usage:
url = "https://reaperscans.com/comics/8072-the-unbeatable-dungeons-lazy-boss-monster/chapters/74373584-chapter-33"
print(find_images_on_page(url))
