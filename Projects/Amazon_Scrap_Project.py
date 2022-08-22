import streamlit as st
from dputils import scrape as sc
import pandas as pd

query = 'laptops'
url = f'https://www.amazon.in/s?k={query}'
print(url)
soup = sc.get_webpage_data(url)


target ={
    'tag':'div', 'attrs':{'s-main-slot s-result-list s-search-results sg-row'}
}

product ={
    'tag':'h2', 'attrs':{'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}
}

items = {
    'tag':'div', 'attrs':{'a-section a-spacing-small a-spacing-top-small'}
}

rating ={
    'tag':'div', 'attrs':{'a-row a-size-small'}
}

result = sc.extract_many(soup, target=target,product=product, items=items, rating=rating)

df = pd.DataFrame(result)
print(df)
