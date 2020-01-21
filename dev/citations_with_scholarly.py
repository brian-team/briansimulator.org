'''
Some ideas for automatically generating a list of papers that use Brian using Google Scholar citations.
Not quite convinced by this idea.
'''

import scholarly
import itertools

# dan_goodman = next(scholarly.search_author('Dan F. M. Goodman')).fill()
# for pub in dan_goodman.publications:
#     is_brian_paper = False
#     if 'brian' in pub.bib['title'].lower():
#         is_brian_paper = True
#     else:
#         try:
#             pub = pub.fill()
#         except Exception as e:
#             print('ERROR: ', pub.bib['title'])
#         try:
#             if 'brian' in pub.bib.get('abstract', '').lower():
#                 is_brian_paper = True
#         except Exception as e:
#             print('ERROR: ', pub.bib['title'])
#         try:
#             if 'stimberg' in pub.bib.get('author', '').lower():
#                 is_brian_paper = True
#         except Exception as e:
#             print('ERROR: ', pub.bib['title'])
#     if is_brian_paper:
#         print('FOUND:', pub.bib['title'])

# pub = next(scholarly.search_pubs_query('Brian 2, an intuitive and efficient neural simulator'))
# for citation in pub.get_citedby():
#     print(citation.bib['title'])

brian_paper_titles = [
    'Brian 2, an intuitive and efficient neural simulator',
    'Equation-oriented specification of neural models for simulations',
    'Brian: a simulator for spiking neural networks in Python',
    'The Brian simulator Frontiers in Neuroscience',
]

for title in brian_paper_titles:
    pub = next(scholarly.search_pubs_query(title))
    cites = itertools.islice(pub.get_citedby(), 10)
    for cite in cites:
        print(cite.bib['title'])