from packages.AminoacidParser import *
from packages.Querybilder import *
import csv
from pymed import PubMed
import json
import pandas as pd

#df = pd.DataFrame(columns=['doi', 'title', 'Abs', 'Aut'] )
df = pd.DataFrame(columns=['doi','Abs'] )
pubmed = PubMed(tool="MyTool", email="my@email.address")
querys = querygenerator('datos_genes-Hoja1.csv')
#query = "PTPN11[Title/Abstract] AND (D61G[Title/Abstract] OR Asp61Gly[Title/Abstract])"

for iquery in querys:
    print(iquery)
# Execute the query against the API
    
    results = pubmed.query(iquery, max_results=500)
    
    for article in results:
        a = article.toJSON()  
        ay = json.loads(a)
        abs = ay["abstract"]
        title =  ay["title"]
        doi = ay["doi"]
        Authors = ay["authors"]
        for i in Authors:
            au = i["firstname"]
        df = df.append({'doi':doi, 'Abs': abs}, ignore_index=True)
#df.to_csv('ncbi_pru1.csv')
print(df)

