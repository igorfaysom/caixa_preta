from operator import itemgetter
from pickle import TRUE
import random

MAX_GENES = 9
def gerarIndividuo():
  genes =[]
  for i in range(MAX_GENES):
    num = random.randint(0,15)
    bit = '{0:04b}'.format(num)
    genes.append(bit)
    unir_genes = ''
    individuo = unir_genes.join(genes)
  return { 'individuo': individuo, 'fitness': 0}

def gerarPopulacao(tam_populacao):
  pop = []
  for i in range(tam_populacao):
    pop.append( gerarIndividuo())
  return pop

def avalicao(pop):

  for i in range(len(pop)):
    aci_nuc = list(pop[i]['individuo'])
    expressao = (9 + int(aci_nuc[1]) * int(aci_nuc[4]) - int(aci_nuc[22]) * int(aci_nuc[13])
    + int(aci_nuc[23]) * int(aci_nuc[3]) - int(aci_nuc[20]) * int(aci_nuc[9])
    + int(aci_nuc[35]) * int(aci_nuc[14]) - int(aci_nuc[10]) *  int(aci_nuc[25])
    + int(aci_nuc[15]) * int(aci_nuc[16]) + int(aci_nuc[2])  * int(aci_nuc[32])
    + int(aci_nuc[27]) * int(aci_nuc[18]) + int(aci_nuc[11]) * int(aci_nuc[33])
    - int(aci_nuc[30]) * int(aci_nuc[31]) - int(aci_nuc[21]) * int(aci_nuc[24])
    + int(aci_nuc[34]) * int(aci_nuc[26]) - int(aci_nuc[28]) * int(aci_nuc[6])
    + int(aci_nuc[7]) * int(aci_nuc[12]) - int(aci_nuc[5]) * int(aci_nuc[8])
    + int(aci_nuc[17]) * int(aci_nuc[19]) - int(aci_nuc[0]) * int(aci_nuc[29])
    + int(aci_nuc[22]) * int(aci_nuc[3]) + int(aci_nuc[20]) * int(aci_nuc[14])
    + int(aci_nuc[25]) * int(aci_nuc[15]) + int(aci_nuc[30]) * int(aci_nuc[11])
    + int(aci_nuc[24]) * int(aci_nuc[18]) + int(aci_nuc[6]) * int(aci_nuc[7])
    + int(aci_nuc[8]) * int(aci_nuc[17]) + int(aci_nuc[0]) * int(aci_nuc[32]))
    pop[i]['fitness'] = expressao

def roleta(pop_ord):
  soma_fitness = 0
  soma_roleta = 0

  for i in range(len(pop_ord)):   
    soma_fitness  += pop_ord[i]['fitness']
    num_sort=random.randint(1, soma_fitness)
  
  for i in range(len(pop_ord)):
    soma_roleta  += pop_ord[i]['fitness']
      
    if soma_roleta >=  num_sort:
      return i
      break

def selecao(pop):

  pop_ord = sorted(pop,key=itemgetter('fitness'))
  pares = []
  for i in range(len(pop)):
    ind1 = roleta(pop_ord)
    ind2 = roleta(pop_ord)
    pares.append({'ind1': pop_ord[ind1], 'ind2':pop_ord[ind2]})
  
  return pares

def cruzamento(ind1, ind2):
  genes_filho = []

  n = len( ind1['individuo'] )
  
  p = random.randint(0, n-1)
  print(p)
  for i in range( n ):
      if i <= p:
        genes_filho.append( ind1['individuo'][i])
      else:
        genes_filho.append(ind2['individuo'][i])
  
  return { 'individuo': genes_filho, 'fitness': 0}

def cruzamento_unicorte(ind1, ind2):
  genes_filho = []
  
  n = len( ind1['individuo'] )
  
  p = random.randint(0, n-1)

  for i in range( n ):
      
      if i <= p:
        genes_filho.append( ind1['individuo'][i])
      else:
        genes_filho.append( ind2['individuo'][i])
  
  return { 'individuo': genes_filho, 'fitness': 0}

""" Mutação """

def mutacao (ind1, ind2):
  n = len( ind1 ['genes'], ind2['genes'] )
  
  p = random.randind(0, n -1)

  mutado = {
    'genes': ind1['genes'].copy(),
    'fitnes': 0
    }
  
  if mutado['genes'][p] == 0:
    mutado['genes'][p] = 1
  else:
    mutado['genes'][p] = 0
      
  return mutado
  
pop = gerarPopulacao(3)
avalicao(pop)
print(selecao(pop))