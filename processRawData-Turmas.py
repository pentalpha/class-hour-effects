import pandas as pd
import numpy as np

turmasPaths = ['raw/turmas-2014.1.csv', 'raw/turmas-2014.2.csv',
 'raw/turmas-2015.1.csv', 'raw/turmas-2015.2.csv', 
 'raw/turmas-2016.1.csv', 'raw/turmas-2016.2.csv', 
 'raw/turmas-2017.1.csv']

columns = ['id_turma', 'descricao_horario', 'id_componente_curricular', 
'situacao_turma', 'id_docente_interno', 'id_docente_externo', 
'nivel_ensino', 'ano', 'periodo', 'distancia']

rows = []

def addRow(row):
    newRow = dict()
    nullValue = False
    for col in columns:
        if col in row:
            newRow[col] = row[col]
        else:
            nullValue = True
            #print('no ' + col + ' row')
            break
    if not nullValue:
        rows.append(newRow)

def addRows(df):
    df.apply(lambda row: addRow(row), axis=1)

for path in turmasPaths:
    print('Processing ' + path)
    df = pd.read_csv(path, sep=';')
    #print(str(df.columns))
    addRows(df)

print(str(len(rows)))
print('Writing final dataframe')
finalDf = pd.DataFrame(rows, columns=columns)
finalDf.to_csv('input/turmas.csv', index=False, sep='\t')
finalDf = finalDf.iloc[np.random.choice(finalDf.index, int(len(finalDf)*0.05))]
finalDf.to_csv('input/turmas-05.csv', index=False, sep='\t')
