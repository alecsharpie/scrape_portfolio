from bs4 import BeautifulSoup
import requests

def get_project(soup, side, idx):

    template = {
        'title':
        soup.find_all(class_ = side)[idx].find(
            class_='project-title').text,
        'date':
        soup.find_all(class_=side)[idx],#.find(
              # class_='flex-block').find(class_='flex-item').find(
              #  class_='info-link').find_all('span')[2].text,
        'description':
        soup.find_all(class_=side)[idx].find(
            class_='project-description').text,
        'links': {
            link.text: link.get('href')
            for link in soup.find_all(class_=side)[idx].find_all('a')
        },
        'image_path':
        soup.find('img').get('src'),
        'image_alt':
        soup.find('img').get('alt'),
        'links': {
            tag.text: tag.get('class')[1]
            for tag in soup.find_all(class_=side)[idx].find_all('span', class_= 'tag')
        }
    }

    print(template['date'])

    print(template['description'])

    return template


def get_html():

    url = 'https://www.alecsharpie.me'

    html_doc = requests.get(url).content

    soup = BeautifulSoup(html_doc, 'html.parser')

    projects = []

    # for side in ['project-row-r', 'project-row-l']:
    #     for idx in range(len(soup.find_all(class_=side))):
    #         proj = get_project(soup, side = side, idx = idx)
    #         projects.append(proj)

    proj = get_project(soup, side='project-row-l', idx=0)

    # print(proj)

    #.find(attrs={"name" : "stainfo"})


    # print(projects)

    return soup

if __name__ == "__main__":
    get_html()
