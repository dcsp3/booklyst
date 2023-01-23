import json
import requests

def fix_title(title, ch):
    return ch.join([x for x in title.split()])


def get_search_title(title):
    final = fix_title(title, '+')
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={final}')
    data = json.loads(response.text)
    var = data['items'][0]['volumeInfo']
    return var['title']


def SearchOne(title):
    final = fix_title(title, '+')
    try:
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={final}')
        data = json.loads(response.text)
        l=[]
        d={}
        var = data['items'][0]['volumeInfo']
        d['id'] = data['items'][0]['id']
        d['genre'] = var['categories'][0]
        if 'imageLinks' in var.keys():
            d['img'] = var['imageLinks']['thumbnail']
        else:
            d['img'] = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH0AAACiCAMAAABbNjLtAAAAA1BMVEUAAACnej3aAAAAK0lEQVR4nO3BgQAAAADDoPlT3+AEVQEAAAAAAAAAAAAAAAAAAAAAAAAAzwBPvAABvQfCagAAAABJRU5ErkJggg=='
        d['title'] = var['title']
        if 'subtitle' in var.keys():
            d['subtitle'] = ' : ' + var['subtitle']
        else:
            d['subtitle'] = ''
        if 'authors' in var.keys():
            d['author'] = var['authors'][0]
        if 'description' in var.keys():
            if len(var['description']) <= 616:
                d['summary'] = var['description']
            else:
                d['summary'] = var['description'][0:616] + '...'
        else:
            d['summary'] = ''
        l.append(d)
    except:
        l = None
    return l


def get_book_info(book):
    l = []
    d = {}
    d['book_id'] = book.book_id
    d['title'] = book.title
    d['subtitle'] = book.subtitle
    d['img'] = book.cover
    d['author'] = book.author
    d['genre'] = book.genre
    d['date_fin'] = book.date_fin
    d['sentence_1'] = book.sentence_1
    d['sentence_2'] = book.sentence_2
    d['sentence_3'] = book.sentence_3
    d['highlights'] = book.highlights
    d['my_rating'] = book.my_rating
    l.append(d)
    return l
