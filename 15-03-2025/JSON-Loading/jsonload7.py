from jsonpath_ng.ext import parse

# JSON data
data = {
    "store": {
        "book": [
            {"category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95},
            {"category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99},
            {"category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "price": 15.99}
        ],
        "bicycle": {"color": "red", "price": 19.95}
    }
}

# Example 1: Extract all authors
jsonpath_expr = parse('$.store.book[*].author')
authors = [match.value for match in jsonpath_expr.find(data)]
print("Authors:", authors)
# Output: Authors: ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville']

# Example 2: Extract the price of the bicycle
jsonpath_expr = parse('$.store.bicycle.price')
bicycle_price = [match.value for match in jsonpath_expr.find(data)]
print("Bicycle Price:", bicycle_price)
# Output: Bicycle Price: [19.95]

# Example 3: Extract all book titles
jsonpath_expr = parse('$.store.book[*].title')
titles = [match.value for match in jsonpath_expr.find(data)]
print("Book Titles:", titles)
# Output: Book Titles: ['Sayings of the Century', 'Sword of Honour', 'Moby Dick']
