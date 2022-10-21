from packages.AminoacidParser import *
import csv

def querygenerator(pathfilecsv):

    #pathfilecsv = '/home/chelo/Downloads/datos_genes-Hoja1.csv'
    parser = AminocidParser()

    
    querys = []

    entrada = list(csv.reader(open(pathfilecsv)))   #read in the csv file
    variantes = entrada[1:]
    csv_dic = {}
    genes = entrada[0]
    index = 0
    


    while index < len(genes): 

        variantesporgen = []
        for listas in variantes: 
            #print(listas[index])
            variantesporgen.append(listas[index])
        print(variantesporgen)
        csv_dic[genes[index]] = variantesporgen
        index = index + 1
    
    for key,value in csv_dic.items():
        for index,valu in enumerate(value):
            querys.append(parser.ncbi_query_bilder(key,value[index]))
    
    print(querys)
    return querys
    
    


if __name__ == '__main__':
    querygenerator('/home/chelo/Downloads/datos_genes-Hoja2.csv') 