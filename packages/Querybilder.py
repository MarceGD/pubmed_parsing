import csv

from packages.AminoacidParser import *


def querygenerator(pathfilecsv):
    pathfilecsv = '/home/chelo/proyectos/varmed-bench/pubmed_parser/datos_genes-Hoja1.csv'
    parser = AminocidParser()

    
    querys = []

    entrada = list(csv.reader(open(pathfilecsv)))   #read in the csv file
    variantes = entrada[1:]
    csv_dic = {}
    genes = entrada[0]
    index = 0
    print(genes)
    
        
    
    while index < len(genes): 

    # listagenindex = []
        variantesporgen = []
        for listas in variantes: 
            #print(listas[index])
            variantesporgen.append(listas[index])
        print(variantesporgen)
        csv_dic[genes[index]] = variantesporgen
        index = index + 1


    for key,value in csv_dic.items():
    
        print(key,value)
        while("" in value) : 
            value.remove("") 
    for key,value in csv_dic.items():
        for index,vr in enumerate(value):
        
            print(key,value[index])
            querys.append(parser.ncbi_query_bilder(key,value[index]))
            genx = key
    print(querys)
    return querys,genx
    for i,q in enumerate(querys):
        print(i,q)
    


if __name__ == '__main__':
    querygenerator('/home/chelo/proyectos/varmed-bench/pubmed_parser/datos_genes-Hoja2.csv') 
