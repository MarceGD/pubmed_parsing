from packages.AminoacidParser import *
from packages.Querybilder import *
import csv
from pymed import PubMed
import json
import pandas as pd
import time

#df = pd.DataFrame(columns=['doi', 'title', 'Abs', 'Aut'] )
df = pd.DataFrame(columns=['gen','var', 'Abs', 'doi'] )
pubmed = PubMed(tool="MyTool", email="mdgamarraok@gmail.com")
querys = querygenerator('datos_genes-Hoja1.csv')
#querys = ["PTPN11[Title/Abstract] AND (T42A[Title/Abstract] OR Thr42Ala[Title/Abstract])", "PTPN11[Title/Abstract] AND (D61G[Title/Abstract] OR Asp61Gly[Title/Abstract])"]
#for i,n in enumerate(querys):
#    print(i,n)


#        time.sleep(60)

for iquery in querys:
    
# Execute the query against the API
    
    results = pubmed.query(iquery, max_results=50)
    
    for article in results:
        a = article.toJSON()  
        ay = json.loads(a)
        abs = ay["abstract"]
        title =  ay["title"]
        doi = ay["doi"]
        Authors = ay["authors"]
        for i in Authors:
            au = i["firstname"]
        gen = iquery.split('[Title/Abstract]')[0]
        variante = iquery.split('[Title/Abstract]')[1].split('(')[1]
        df = df.append({'gen':gen, 'var': variante, 'Abs': abs, 'doi':doi}, ignore_index=True)
        print('Terminando la busqueda para {}-{}'.format(gen,variante))
        
df.to_csv('ncbi_pru1.csv', mode='a', index=False, header=False)
time.sleep(40) #time in seconds
#print(df)

