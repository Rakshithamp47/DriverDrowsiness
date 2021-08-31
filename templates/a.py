from bs4 import BeautifulSoup
with open("index3.html") as fp:
    html_doc = fp.read()
def remove_tags(html):
  
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)
  
  
# Print the extracted data
a=remove_tags(html_doc)
print(a)
