#!/usr/bin/env python3

import json
import os

scriptDir = os.path.split(os.path.dirname(__file__))[0]
dataDir = os.path.join(scriptDir, "data")

quote_files = [os.path.join(dataDir, f) for f in os.listdir(dataDir) if os.path.isfile(os.path.join(dataDir, f))]
quotes = []
for f in quote_files:
    with open(f, 'r') as quote_file:
        quotes += json.load(quote_file)['data']

unique_quotes = []
seen_quotes = set()
for x in quotes:
    if x['quote'] not in seen_quotes:
        unique_quotes.append(x)
        seen_quotes.add(x['quote'])		

with open('tmp', 'w') as unique_quotes_file:
    json.dump({'data': list(unique_quotes)}, unique_quotes_file, indent=4, ensure_ascii=False)
    unique_quotes_file.write('\n')
