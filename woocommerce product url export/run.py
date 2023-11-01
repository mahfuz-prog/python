import time
from requests_html import HTML, HTMLSession
session = HTMLSession()

f=open('link.txt',mode='w')
# loop over WooCommerce pagination product page in this case i have 25

for page in range(1,25):
  # usages requests library to get a response
  response = session.get(f'https://www.nirvanalighting.com/products/?product-page={page}')

  # select css of this page using this response. return a list of selected elements
  products = response.html.find('li.product')
  for product in products:
    # product contain a set of string {'like this'}
    # convert the set into string and slice to get actual link
    product_url = str(product.absolute_links)[2:-2]

    # save into text file
    f.write(f'{product_url}\n')
    print(product_url)

  total_products = len(products)
  print(f'Total {total_products} product in page {page}')
  print('----------------------------')
  time.sleep(2)
f.close()
