def html_special_chars(data):
    symbols = {'<': '&lt;', '>': '&gt;', '"': '&quot;','&': '&amp;'}
    return ''.join(symbols.get(char,char) for char in data)

print(html_special_chars("<h2>Hello World</h2>"))
print("&lt;h2&gt;Hello World&lt;/h2&gt;" == html_special_chars("<h2>Hello World</h2>"))