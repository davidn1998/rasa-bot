import pandas as pd
import numpy as np

db = pd.read_csv('terms.csv')

term = db['Term'].values
defen = db['Definition'].values

faq_string = ""
resp_string = ""

for i, j in zip(term, defen):
    faq_string += '## intent: faq/{}\n- What does {} mean?\n'.format(i.lower().replace(' ', '_'), i)
    resp_string += '## {}\n* faq/{}\n - {}\n'.format(i.lower(), i.lower().replace(' ','_'), j)

o = open('data/nlu.md','w')
o.write(faq_string)
o.flush()
o.close()

o = open('data/responses.md', 'w')
o.write(resp_string)
o.flush()
o.close()





