

class AminocidParser:
  

  def one_to_three_name(self, aminoacid):
    self.aminoacid = aminoacid
    if  self.aminoacid == "G":
      aminoacido = "Gly"
      return aminoacido
    elif  self.aminoacid == "A":
      aminoacido = "Ala"
      return aminoacido
    elif  self.aminoacid == "V":
      aminoacido = "Val"
      return aminoacido
    elif  self.aminoacid == "L":
      aminoacido = "Leu"
      return aminoacido
    elif  self.aminoacid == "I":
      aminoacido = "Ile"
      return aminoacido
    elif  self.aminoacid == "M":
      aminoacido = "Met"
      return aminoacido
    elif  self.aminoacid == "F":
      aminoacido = "Phe"
      return aminoacido
    elif  self.aminoacid == "W":
      aminoacido = "Trp"
      return aminoacido
    elif  self.aminoacid == "P":
      aminoacido = "Pro"
      return aminoacido
    elif  self.aminoacid == "S":
      aminoacido = "Ser"
      return aminoacido
    elif  self.aminoacid == "T":
      aminoacido = "Thr"
      return aminoacido
    elif  self.aminoacid == "C":
      aminoacido = "Cys"
      return aminoacido
    elif  self.aminoacid == "Y":
      aminoacido = "Tyr"
      return aminoacido
    elif  self.aminoacid == "N":
      aminoacido = "Asn"
      return aminoacido
    elif  self.aminoacid == "Q":
      aminoacido = "Gln"
      return aminoacido
    elif  self.aminoacid == "K":
      aminoacido = "Lys"
      return aminoacido
    elif  self.aminoacid == "R":
      aminoacido = "Arg"
      return aminoacido
    elif  self.aminoacid == "H":
      aminoacido = "His"
      return aminoacido
    elif  self.aminoacid == "D":
      aminoacido = "Asp"
      return aminoacido
    elif  self.aminoacid == "E":
      aminoacido = "Glu"
      return aminoacido
    else:
      print('Wrong one-letter-aminoacid code')
  def ncbi_query_bilder(self,gen,var):
    parseador = AminocidParser()
    am1 = var[0]
    am2 = var[-1]
    change1 = parseador.one_to_three_name(am1)
    change2 =  parseador.one_to_three_name(am2)
    varf = change1+var[1:-1]+change2
    query = gen +'[Title/Abstract] AND ('+ var + '[Title/Abstract] OR ' + varf + '[Title/Abstract])'
    return query

