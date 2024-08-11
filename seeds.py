from models import Authors, Qoutes, Tag
import connect
import json


with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)
    
for author in authors_data:
    new_author = Authors(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )
    new_author.save()


with open('qoutes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)

for quote in quotes_data:
    author = Authors.objects(fullname=quote['author']).first()
    
    if author:
        new_quote = Qoutes(
            tags=[Tag(name=tag) for tag in quote['tags']],
            author=author,
            quote=quote['quote']
        )
        new_quote.save()