import requests
from bs4 import BeautifulSoup


def parse_website_content(vgm_url):

    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    #print(soup.get_text())

    lst = []
    for link in soup.find_all('a'):
        lst.append(link.get('href'))
    about_lst = []
    for val in lst:
        if('https://kcgcollege.ac.in/about/' in val):
            about_lst.append(val)
        else:
            pass

    ptag_lst = []
    for data in about_lst:
        vgm_url = data
        html_text = requests    .get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        for link in soup.find_all('p'):
            ptag_lst.append(link.get_text())
    final_lst = []
    with open("ptag_text.txt",'w',encoding='utf-8') as f:
        for data in range(len(ptag_lst)):
            if(len(ptag_lst[data])<100):
                pass
            else:
                f.write(f"{ptag_lst[data]}\n")
                final_lst.append(ptag_lst[data])

    return final_lst