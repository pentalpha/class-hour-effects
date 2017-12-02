# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 02:12:58 2017

@author: 3green
"""

import csv
import numpy as np
from matplotlib import pyplot as plt

#Arquivo 1
Lista_N34 = []
Lista_N12 = []
Lista_T56 = []
Lista_T34 = []
Lista_T12 = []
Lista_M56 = []
Lista_M34 = []
Lista_M12 = []
Lista_faltas = []
Lista_medias = []
faltasN34 = 0
faltasN12 = 0
faltasT56 = 0
faltasT34 = 0
faltasT12 = 0
faltasM56 = 0
faltasM34 = 0
faltasM12 = 0
mediasN34 = 0.0
mediasN12 = 0.0
mediasT56 = 0.0
mediasT34 = 0.0
mediasT12 = 0.0
mediasM56 = 0.0
mediasM34 = 0.0
mediasM12 = 0.0
qntN34 = 0
qntN12 = 0
qntT56 = 0
qntT34 = 0
qntT12 = 0
qntM56 = 0
qntM34 = 0
qntM12 = 0

#Arquivo 2
Lista_aulas = []
Lista_aulas_N34 = []
Lista_aulas_N12 = []
Lista_aulas_T56 = []
Lista_aulas_T34 = []
Lista_aulas_T12 = []
Lista_aulas_M56 = []
Lista_aulas_M34 = []
Lista_aulas_M12 = []
Lista_id_turma = []
Lista_medianas = []
Lista_medianasN34 = []
Lista_medianasN12 = []
Lista_medianasT56 = []
Lista_medianasT34 = []
Lista_medianasT12 = []
Lista_medianasM56 = []
Lista_medianasM34 = []
Lista_medianasM12 = []
Lista_Nomes = []
medianasN34 = 0.0
medianasN12 = 0.0
medianasT56 = 0.0
medianasT34 = 0.0
medianasT12 = 0.0
medianasM56 = 0.0
medianasM34 = 0.0
medianasM12 = 0.0
aulasN34 = 0
aulasN12 = 0
aulasT56 = 0
aulasT34 = 0
aulasT12 = 0
aulasM56 = 0
aulasM34 = 0
aulasM12 = 0


#Arquivo 1
with open('./input/matriculas-plus.csv',encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
       Lista_N34.append(row[6])
       Lista_N12.append(row[7])
       Lista_T56.append(row[8])
       Lista_T34.append(row[9])
       Lista_T12.append(row[10])
       Lista_M56.append(row[11])
       Lista_M34.append(row[12])
       Lista_M12.append(row[13])
       Lista_faltas.append(row[4])
       Lista_medias.append(row[3])
   
Lista_N34.remove("noite34")
Lista_N12.remove("noite12")
Lista_T56.remove("tarde56")
Lista_T34.remove("tarde34")
Lista_T12.remove("tarde12")
Lista_M56.remove("manha56")
Lista_M34.remove("manha34")
Lista_M12.remove("manha12")
Lista_faltas.remove("numero_total_faltas")
Lista_medias.remove("media_final")

for i in range(0, len(Lista_faltas)):
    if Lista_N34[i] == "True":
     faltasN34 += int(Lista_faltas[i])
     mediasN34 += float(Lista_medias[i])
     qntN34 += 1
       
    if Lista_N12[i] == "True":
     faltasN12 += int(Lista_faltas[i])
     mediasN12 += float(Lista_medias[i])
     qntN12 += 1
   
    if Lista_T56[i] == "True":
     faltasT56 += int(Lista_faltas[i])
     mediasT56 += float(Lista_medias[i])
     qntT56 += 1
    
    if Lista_T34[i] == "True":
     faltasT34 += int(Lista_faltas[i])
     mediasT34 += float(Lista_medias[i])
     qntT34 += 1
     
    if Lista_T12[i] == "True":
     faltasT12 += int(Lista_faltas[i])
     mediasT12 += float(Lista_medias[i])
     qntT12 += 1
    
    if Lista_M56[i] == "True":
     faltasM56 += int(Lista_faltas[i])
     mediasM56 += float(Lista_medias[i])
     qntM56 += 1
     
    if Lista_M34[i] == "True":
     faltasM34 += int(Lista_faltas[i])
     mediasM34 += float(Lista_medias[i])
     qntM34 += 1
     
    if Lista_M12[i] == "True":
     faltasM12 += int(Lista_faltas[i])
     mediasM12 += float(Lista_medias[i])
     qntM12 += 1


#Arquivo 2  
with open('./input/turmas-plus.csv', encoding="utf8") as csvfile:
    read = csv.reader(csvfile, delimiter = ',')
    
    for row in read:
        aux = 0
        if not Lista_Nomes:
            Lista_Nomes.append(row[0])
            Lista_Nomes.append(row[8])
            Lista_Nomes.append(row[9])
            Lista_Nomes.append(row[10])
            Lista_Nomes.append(row[11])
            Lista_Nomes.append(row[12])
            Lista_Nomes.append(row[13])
            Lista_Nomes.append(row[14])
            Lista_Nomes.append(row[15])
            Lista_Nomes.append(row[11])
            Lista_Nomes.append(row[17])
            Lista_Nomes.append(row[18])
            Lista_Nomes.append(row[20])
        else:
            if not Lista_id_turma:
                Lista_id_turma.append(row[0])
                Lista_aulas_N34.append(row[8])
                Lista_aulas_N12.append(row[9])
                Lista_aulas_T56.append(row[10])
                Lista_aulas_T34.append(row[11])
                Lista_aulas_T12.append(row[12])
                Lista_aulas_M56.append(row[13])
                Lista_aulas_M34.append(row[14])
                Lista_aulas_M12.append(row[15])
                Lista_aulas.append(int(row[17]) * int(row[18]))
                Lista_medianas.append(row[20])
            else:
                for i in range(0, len(Lista_id_turma)):
                    if row[0] == Lista_id_turma[i]:
                        aux = 1
                   
                #Procedimento para tirar as turmas repetidas e n atrapalhar o calculo das faltas pelas aulas
                if aux == 0:
                    Lista_id_turma.append(row[0])
                    Lista_aulas_N34.append(row[8])
                    Lista_aulas_N12.append(row[9])
                    Lista_aulas_T56.append(row[10])
                    Lista_aulas_T34.append(row[11])
                    Lista_aulas_T12.append(row[12])
                    Lista_aulas_M56.append(row[13])
                    Lista_aulas_M34.append(row[14])
                    Lista_aulas_M12.append(row[15])
                    Lista_aulas.append(int(row[17]) * int(row[18]))
                    Lista_medianas.append(row[20])
                
#print (Lista_id_turma)

for i in range(0, len(Lista_aulas)):
    if Lista_aulas_N34[i] == "True":
     aulasN34 += int(Lista_aulas[i])
     Lista_medianasN34.append(float(Lista_medianas[i]))
    
    if Lista_aulas_N12[i] == "True":
     aulasN12 += int(Lista_aulas[i])
     Lista_medianasN12.append(float(Lista_medianas[i]))
   
    if Lista_aulas_T56[i] == "True":
     aulasT56 += int(Lista_aulas[i])
     Lista_medianasT56.append(float(Lista_medianas[i]))
    
    if Lista_aulas_T34[i] == "True":
     aulasT34 += int(Lista_aulas[i])
     Lista_medianasT34.append(float(Lista_medianas[i]))
   
    if Lista_aulas_T12[i] == "True":
     aulasT12 += int(Lista_aulas[i])
     Lista_medianasT12.append(float(Lista_medianas[i]))
    
    if Lista_aulas_M56[i] == "True":
     aulasM56 += int(Lista_aulas[i])
     Lista_medianasM56.append(float(Lista_medianas[i]))
    
    if Lista_aulas_M34[i] == "True":
     aulasM34 += int(Lista_aulas[i])
     Lista_medianasM34.append(float(Lista_medianas[i]))
    
    if Lista_aulas_M12[i] == "True":
     aulasM12 += int(Lista_aulas[i])
     Lista_medianasM12.append(float(Lista_medianas[i]))
    

Lista_medianasN34 = sorted(Lista_medianasN34)
Lista_medianasN12 = sorted(Lista_medianasN12)
Lista_medianasT56 = sorted(Lista_medianasT56)
Lista_medianasT34 = sorted(Lista_medianasT34)
Lista_medianasT12 = sorted(Lista_medianasT12)
Lista_medianasM56 = sorted(Lista_medianasM56)
Lista_medianasM34 = sorted(Lista_medianasM34)
Lista_medianasM12 = sorted(Lista_medianasM12)

n = 0;

#Pègar a mediana das listas
if len(Lista_medianasN34) % 2 == 0:                                                                      
    n = len(Lista_medianasN34)
    medianasN34 = (Lista_medianasN34[int(n/2-1)]+ Lista_medianasN34[int(n/2)])/2                                                      
else:                                                                                    
    medianasN34 = Lista_medianasN34[int(len(Lista_medianasN34)/2)]  

if len(Lista_medianasN12) % 2 == 0:                                                                      
    n = len(Lista_medianasN12)
    medianasN12 = (Lista_medianasN12[int((n/2)-1)]+ Lista_medianasN12[int(n/2)])/2                                                      
else:                                                                                    
    medianasN12 = Lista_medianasN12[int(len(Lista_medianasN12)/2)] 
    
if len(Lista_medianasT56) % 2 == 0:                                                                      
    n = len(Lista_medianasT56)
    medianasT56 = (Lista_medianasT56[int(n/2-1)]+ Lista_medianasT56[int(n/2)])/2                                                      
else:                                                                                    
    medianasT56 = Lista_medianasT56[int(len(Lista_medianasT56)/2)] 
    
if len(Lista_medianasT34) % 2 == 0:                                                                      
    n = len(Lista_medianasT34)
    medianasT34 = (Lista_medianasT34[int(n/2-1)]+ Lista_medianasT34[int(n/2)])/2                                                      
else:                                                                                    
    medianasT34 = Lista_medianasT34[int(len(Lista_medianasT34)/2)] 
    
if len(Lista_medianasT12) % 2 == 0:                                                                      
    n = len(Lista_medianasT12)
    medianasT12 = (Lista_medianasT12[int(n/2-1)]+ Lista_medianasT12[int(n/2)])/2                                                      
else:                                                                                    
    medianasT12 = Lista_medianasT12[int(len(Lista_medianasT12)/2)] 
    
if len(Lista_medianasM56) % 2 == 0:                                                                      
    n = len(Lista_medianasM56)
    medianasM56 = (Lista_medianasM56[int(n/2-1)]+ Lista_medianasM56[int(n/2)])/2                                                      
else:                                                                                    
    medianasM56 = Lista_medianasM56[int(len(Lista_medianasM56)/2)] 
    
if len(Lista_medianasM34) % 2 == 0:                                                                      
    n = len(Lista_medianasM34)
    medianasM34 = (Lista_medianasM34[int(n/2-1)]+ Lista_medianasM34[int(n/2)])/2                                                      
else:                                                                                    
    medianasM34 = Lista_medianasM34[int(len(Lista_medianasM34)/2)] 
    
if len(Lista_medianasM12) % 2 == 0:                                                                      
    n = len(Lista_medianasM12)
    medianasM12 = (Lista_medianasM12[int(n/2-1)]+ Lista_medianasM12[int(n/2)])/2                                                      
else:                                                                                    
    medianasM12 = Lista_medianasM12[int(len(Lista_medianasM12)/2)] 



#print(medianasM12)
Lista_medias_horarios = []
Lista_medias_horarios.append(mediasN34/qntN34)
Lista_medias_horarios.append(mediasN12/qntN12)
Lista_medias_horarios.append(mediasT56/qntT56)
Lista_medias_horarios.append(mediasT34/qntT34)
Lista_medias_horarios.append(mediasT12/qntT12)
Lista_medias_horarios.append(mediasM56/qntM56)
Lista_medias_horarios.append(mediasM34/qntM34)
Lista_medias_horarios.append(mediasM12/qntM12)

#print(Lista_medias_horarios)

Lista_porcentagens = []
Lista_porcentagens.append(faltasN34/aulasN34 * 100)
Lista_porcentagens.append(faltasN12/aulasN12 * 100)
Lista_porcentagens.append(faltasT56/aulasT56 * 100)
Lista_porcentagens.append(faltasT34/aulasT34 * 100)
Lista_porcentagens.append(faltasT12/aulasT12 * 100)
Lista_porcentagens.append(faltasM56/aulasM56 * 100)
Lista_porcentagens.append(faltasM34/aulasM34 * 100)
Lista_porcentagens.append(faltasM12/aulasM12 * 100)

#print (Lista_porcentagens)

plt.bar(range(len(Lista_porcentagens)),Lista_porcentagens)
y_pos = np.arange(len(Lista_porcentagens))
plt.xticks(y_pos, ("N34", "N12","T56","T34","T12","M56","M34","M12"))
plt.title("Gráfico de barras da quantidade de faltas em relação as aulas")
plt.ylabel('Porcentagem em relação ao total de aulas')
plt.show()
        
plt.bar(range(len(Lista_medias_horarios)),Lista_medias_horarios)
y_pos = np.arange(len(Lista_medias_horarios))
plt.xticks(y_pos, ("N34", "N12","T56","T34","T12","M56","M34","M12"))
plt.title("Gráfico de barras das medias finais de cada horario")
plt.ylabel('Media das notas')
plt.show() 

pop = {"N34": medianasN34, "N12": medianasN12, "T56": medianasT56, "T34": medianasT34, "T12": medianasT12, "M56": medianasM56, "M34": medianasM34, "M12": medianasM12}
horarios = [i for i in pop.keys()]
Mediana = [j for j in pop.values()]
popPos = np.arange(len(horarios))

plt.barh(popPos, Mediana, align='center') 
plt.yticks(popPos, horarios)   
plt.title("Gráfico de barras das medianas de cada horario") 
plt.show();
   