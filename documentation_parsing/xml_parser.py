"""
Convert xml documentation to csv file.

Csv file has two columns: chapter name and corresponding text content, including
various links.
Draft parser script. Should be run from this folder.
usage:
python xml_parser.py
"""

import pandas as pd
import bs4

xml_path = '../raw_data/publication-19879--en.xml'

with open(xml_path, 'r') as f:
    contents = f.read()
    soup = bs4.BeautifulSoup(contents, 'lxml')

titles = soup.find_all('title')

result = []
for section in soup.find_all('section', role="internal"):
    title = section.find('title')
    info = section.find_all('para')
    result.append(
        {
        'section_title': title.getText(),
        'section_text': '\n'.join([element.getText() for element in info]),
        }
        )

output = pd.DataFrame(result)
output.to_csv('../parsed_data/publication-19879--en_sections.csv')