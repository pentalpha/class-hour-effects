import pandas as pd
import numpy as np
from tqdm import tqdm

turmasDfPath = 'input/turmas.csv'
turmasMiniDfPath = 'input/turmas-05.csv'
matriculasDfPath = 'input/matriculas.csv'
matriculasMiniDfPath = 'input/matriculas-05.csv'

matriculasPlusDfPath = 'input/matriculas-plus.csv'
matriculasPlusMiniDfPath = 'input/matriculas-plus-05.csv'

infosToAdd = ['noite34', 'noite12', 
'tarde56', 'tarde34', 'tarde12',
'manha56', 'manha34', 'manha12',
'sabado', 'nivel_ensino']

classInfo = dict()
classes = set()

doAll = True
if not doAll:
    matriculasDfPath = matriculasMiniDfPath
    matriculasPlusDfPath = matriculasPlusMiniDfPath

def getClassInfo(row):
    newInfo = dict()
    for info in infosToAdd:
        newInfo[info] = row[info]
    classInfo[str(row['id_turma'])] = newInfo

def getClassInfos():
    print("Reading input class infos")
    classDf = pd.read_csv(turmasDfPath,sep='\t')
    classesList = classDf['id_turma'].unique().tolist()
    global classes
    classes = set()
    for n in tqdm(classesList):
        classes.add(str(n))
    print(str(len(classes)) + ' classes')
    classDf.apply(lambda row: getClassInfo(row), axis=1)
    print(str(len(classInfo)) + " class infos")

getClassInfos()

print("Reading input 'matriculas' ")
matriculasDf = pd.read_csv(matriculasDfPath,sep='\t')
#print(matriculasDf.columns)
print(str(len(matriculasDf)) + " matriculas before...")
matriculasDf = matriculasDf[matriculasDf['id_turma'].isin(classInfo)]
print(str(len(matriculasDf)) + " matriculas, after erasing invalid classes.")

print("Adding new info to final DataFrame")

def getInfo(id_turma, info):
    if id_turma in classInfo:
        return classInfo[id_turma][info]
    else:
        return ''

for info in infosToAdd:
    matriculasDf[info] = ''

for info in tqdm(infosToAdd):
    matriculasDf[info] = matriculasDf.apply(lambda row: getInfo(str(row['id_turma']), info), axis=1)

print("Writing final dataframe")

for col in infosToAdd:
    matriculasDf[col].replace('', np.nan, inplace=True)
    matriculasDf.dropna(subset=[col], inplace=True)

matriculasDf['n1'] = matriculasDf['n1'].astype(float)
matriculasDf['n2'] = matriculasDf['n2'].astype(float)
matriculasDf['n3'] = matriculasDf['n3'].astype(float)
matriculasDf['media_final'] = matriculasDf['media_final'].astype(float)
matriculasDf['id_curso'] = matriculasDf['id_curso'].astype(int)
matriculasDf['id_turma'] = matriculasDf['id_turma'].astype(int)
matriculasDf['numero_total_faltas'] = matriculasDf['numero_total_faltas'].astype(int)

matriculasDf.to_csv(matriculasPlusDfPath, sep='\t', index=False)