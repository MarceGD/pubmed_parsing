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
    #print(genes)
    
        
    
    while index < len(genes): 

    # listagenindex = []
        variantesporgen = []
        for listas in variantes: 
            #print(listas[index])
            variantesporgen.append(listas[index])
        #print(variantesporgen)
        csv_dic[genes[index]] = variantesporgen
        index = index + 1

    #print(csv_dic) #printea el dictionario limpio de nones
    
    for key,value in csv_dic.items():
        while('' in value): 
                value.remove('') #aca se remueven los valores sin tipo
        #print(key,value)
    #print(" ")  
    #print(" ")    Estos prints son para testear donde ocurre los problemas
    #print(csv_dic)
   # print(csv_dic.items())
    for key,value in csv_dic.items():
        #print(" prueba valor")  
        #print( value)
        for index,vr in enumerate(value):
            print(key,value[index])
            querys.append(parser.ncbi_query_bilder(key,value[index]))
          #  genx = key
    #print(querys)
    return querys
    for i,q in enumerate(querys):
        print(i,q)
    


if __name__ == '__main__':
    querygenerator('/home/chelo/proyectos/varmed-bench/pubmed_parser/datos_genes-Hoja1.csv') 
