from bs4 import BeautifulSoup
import requests
import json

def get_html_soup():

    url = 'https://www.alecsharpie.me'

    html_doc = requests.get(url).content

    soup = BeautifulSoup(html_doc, 'html.parser')

    return soup

def get_project(soup, side, idx):

    if side.endswith('l'):
        info_idx = 1
    if side.endswith('r'):
        info_idx = 0


    template = {
        'title':
        soup.find_all(class_=side)[idx].find(class_='project-title').text,
        'date':
        soup.find_all(class_=side)[idx].find_all(
            class_='flex-block')[info_idx].find(class_='flex-item').find(
                class_='info-link').find_all('span')[2].text,
        'description':
        soup.find_all(class_=side)[idx].find(
            'p', class_='project-description').text.strip(),
        'links': {
            link.text: link.get('href')
            for link in soup.find_all(class_=side)[idx].find_all('a')
        },
        'image_path':
        soup.find_all(class_=side)[idx].find('img').get('src'),
        'image_alt':
        soup.find_all(class_=side)[idx].find('img').get('alt'),
        'tags': [
            tag.text for tag in soup.find_all(
                class_=side)[idx].find_all('span', class_='tag')
        ]
        # {
        #     tag.text: tag.get('class')[1]
        #     for tag in soup.find_all(class_=side)[idx].find_all('span', class_= 'tag')
        # }
    }


    return template



def get_projects(soup):

    projects = []

    for side in ['project-row-r', 'project-row-l']:
        for idx in range(len(soup.find_all(class_=side))):

            proj = get_project(soup, side = side, idx = idx)
            projects.append(proj)



    return projects


if __name__ == "__main__":
    soup = get_html_soup()
    get_projects(soup)
    json.dump(get_projects(soup), open('projects.json', 'w'))
