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
   
    for gen in csv_dic.keys():
        for index,value in enumerate(csv_dic.values()):
            querys.append(parser.ncbi_query_bilder(gen,value[index]))
    print(querys)
    return querys
    

if __name__ == '__main__':
    querygenerator('/home/chelo/Downloads/datos_genes-Hoja1.csv') 