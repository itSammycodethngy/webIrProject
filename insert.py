
from elasticsearch import  helpers, Elasticsearch

import csv

es = Elasticsearch()

with open('scapedJob.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es,reader,index='indeed', doc_type='jobs')