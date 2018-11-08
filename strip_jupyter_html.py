import sys
import bs4

input_name = sys.argv[1]
output_name = '{}_stripped.html'.format(input_name[:-5])

with open(input_name, 'r') as f:
    txt = f.read()
    soup = bs4.BeautifulSoup(txt, features='html5lib')

[x.extract() for x in soup.find_all('div', 'input')]

with open(output_name, 'w') as f:
    f.write(str(soup))
