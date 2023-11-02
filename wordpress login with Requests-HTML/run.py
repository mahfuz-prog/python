from utils import create_html_page, load_page
from requests_html import HTML, HTMLSession
session = HTMLSession()

payload = {
    'log': 'admin',
    'pwd': 'pass'
}

# login in session
r = session.post('https://demo.com/mahfuj/wp-login.php/', data=payload)
print(f'response for login {r}')

admin_post_page = session.get('https://demo.com/mahfuj/wp-admin/edit.php').text
print(f'response for requested page {r}')

# save the post as a html file
page_html = create_html_page('demo', admin_post_page)

# load the html file
html = load_page(page_html)

# extract information
match = html.find('tr.iedit')
for _ in match:
    print(_)
