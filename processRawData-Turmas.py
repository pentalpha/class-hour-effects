import pandas as pd
import numpy as np
from tqdm import tqdm


turmasPaths = ['raw/turmas-2014.1.csv', 'raw/turmas-2014.2.csv',
 'raw/turmas-2015.1.csv', 'raw/turmas-2015.2.csv', 
 'raw/turmas-2016.1.csv', 'raw/turmas-2016.2.csv', 
 'raw/turmas-2017.1.csv']

columns = ['id_turma', 'descricao_horario', 'id_componente_curricular', 
'id_docente_interno', 'id_docente_externo', 
'nivel_ensino', 'ano', 'periodo']

horarioColumns = ['noite34', 'noite12', 
'tarde56', 'tarde34', 'tarde12',
'manha56', 'manha34', 'manha12',
'sabado']

newColumns = ['aulas','alunos']

numerals = set()
for n in range(0,10):
    numerals.add(str(n))

optionalCols = [columns[4], columns[5]]
rows = []

def getHorario(description):
    hourValues = dict()
    for col in horarioColumns:
        hourValues[col] = False
    description = description.split('(')[0]
    splits = description.split(' ')
    for split in splits:
        if len(split) > 0:
            if split[0] in numerals and split[-1] in numerals:
                days = True
                turno = ''
                for ch in split:
                    if days:
                        if ch in numerals:
                            if ch == '7':
                                hourValues['sabado'] = True
                        else:
                            if ch == 'M':
                                turno = 'manha'
                            elif ch == 'T':
                                turno = 'tarde'
                            elif ch == 'N':
                                turno = 'noite'
                            days = False
                    else:
                        if ch == '1' or ch == '2':
                            hourValues[turno+'12'] = True
                        elif ch == '3' or ch == '4':
                            hourValues[turno+'34'] = True
                        elif ch == '5' or ch == '6':
                            hourValues[turno+'56'] = True
    return hourValues


def addRow(row):
    newRow = dict()
    for col in columns:
        newRow[col] = row[col]
    hourValues = getHorario(row['descricao_horario'])
    newRow['aulas'] = row['qtd_aulas_lancadas']
    newRow['alunos'] = min([row['capacidade_aluno'], row['total_solicitacoes']])
        
    for col in horarioColumns:
        newRow[col] = hourValues[col]
    rows.append(newRow)

def addRows(df):
    df.apply(lambda row: addRow(row), axis=1)

for path in tqdm(turmasPaths):
    print('Processing ' + path)
    df = pd.read_csv(path, sep=';')
    for col in columns:
        if not (col in optionalCols) and (col in df.columns):
            df[col].replace('', np.nan, inplace=True)
            df.dropna(subset=[col], inplace=True)
    df.dropna(subset=['capacidade_aluno','total_solicitacoes','qtd_aulas_lancadas'],
              inplace=True)
    df = df[df['situacao_turma'] == "CONSOLIDADA"]
    df = df[df['distancia'] == 'f']

    #print(str(df.columns))
    addRows(df)

def makeTurmasDf():
    print(str(len(rows)))
    print('Writing final dataframe')
    columns.extend(horarioColumns)
    columns.extend(newColumns)
    finalDf = pd.DataFrame(rows, columns=columns)

    finalDf['id_turma'] = finalDf['id_turma'].astype(int)
    finalDf['id_componente_curricular'] = finalDf['id_componente_curricular'].astype(int)
    finalDf['ano'] = finalDf['ano'].astype(int)
    finalDf['periodo'] = finalDf['periodo'].astype(int)

    finalDf.to_csv('input/turmas.csv', index=False, sep='\t')
    finalDf = finalDf.iloc[np.random.choice(finalDf.index, int(len(finalDf)*0.05))]
    finalDf.to_csv('input/turmas-05.csv', index=False, sep='\t')

makeTurmasDf()