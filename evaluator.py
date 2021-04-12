from bs4 import BeautifulSoup
import requests


def extract_text(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    return text


def clean_from_html(text):
    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script'
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    return output


# example of evaluatin website based on criteries
# TODO need to think about criteria
def evaluate(text, criteries):
    score = 0

    for criteria in criteries:
        if criteria in text:
            score += criteries[criteria]

    print("Score of site is {}".format(score))


url = 'https://www.expertcen.ru/article/ratings/luchshie-teploventilyatori.html'
crits = {'плюсы': 3, 'Ballu BFH/S-10': 10}

cleaned_text = clean_from_html(extract_text(url))
evaluate(cleaned_text, crits)
