from packages.AminoacidParser import *
import csv

def querygenerator(pathfilecsv):

    #pathfilecsv = '/home/chelo/Downloads/datos_genes-Hoja1.csv'
    parser = AminocidParser()

    variantes = list(csv.reader(open(pathfilecsv)))   #read in the csv file
    csv_dic = {}
    genes = variantes[0]
    index = 0
    querys = []

    while index < len(genes) and index < len(variantes):
        csv_dic[genes[index]] = variantes[index + 1]
        index = index + 1
   
    
    
    for key,value in csv_dic.items():
        for index,valu in enumerate(value):
            querys.append(parser.ncbi_query_bilder(key,value[index]))
    
    print(querys)
    return querys
    
    


if __name__ == '__main__':
    querygenerator('/home/chelo/Downloads/datos_genes-Hoja1.csv') 