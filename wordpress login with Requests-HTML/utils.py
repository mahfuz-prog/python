from requests_html import HTML

def create_html_page(filename, page_text):
    f = open(f'pages/{filename}.html', mode = 'w')
    f.write(page_text)
    f.close()
    return f'{filename}.html'

def load_page(page_name):
    with open(f'pages/{page_name}') as html_file:
      source = html_file.read()
      html = HTML(html=source)    
      return html
