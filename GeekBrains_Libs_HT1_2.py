import pandas as pd
#1
a = {'author_id':[1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']}
authors = pd.DataFrame(a)
print(authors)
b = {'author_id':[1, 1, 1, 2, 2, 3, 3], 'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price': [450, 300, 350, 500, 450, 370, 290]}
books = pd.DataFrame(b)
print(books)
#2
authors_price = pd.merge(authors, books, on='author_id', how='inner')
print(authors_price)
#3
top5 = authors_price.nlargest(5, 'price')
print(top5)
#4
groupby = authors_price.groupby('author_name')
authors_stat = groupby.agg ({'price': 'min'})
authors_stat['min_price'] = groupby.agg ({'price': 'min'})
authors_stat['max_price'] = groupby.agg ({'price': 'max'})
authors_stat['mean_price'] = groupby.agg ({'price': 'mean'})
authors_stat.drop('price', axis=1,inplace=True)
print(authors_stat)
#5
authors_price['cover']=['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
print(authors_price)