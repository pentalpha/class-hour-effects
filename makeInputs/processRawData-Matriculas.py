#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:18:48 2017

@author: pitagoras
"""
import pandas as pd
import numpy as np
from threading import Thread, Lock
from tqdm import tqdm

matriculaFilesPaths2014 = ["../raw/matricula-2014.1.csv", "../raw/matricula-2014.2.csv"]
matriculaFilesPaths2015 = ["../raw/matricula-2015.1.csv", "../raw/matricula-2015.2.csv"]
matriculaFilesPaths2016 = ["../raw/matricula-2016.1.csv", "../raw/matricula-2016.2.csv"]
matriculaFilesPaths2017 = ["../raw/matricula-2017.1.csv"]

outputDfPath = "../input/matriculas.csv"
cols = ['id_turma', 'discente', 'id_curso', 'periodo', 'n1','n2','n3','media_final',
           'numero_total_faltas','descricao']
rows = []
rowsLock = Lock()

def addRows(df,periodo):
    print(periodo+"\tStoring matriculaSet (3/5)")
    localRows = []
    matriculas = dict()
    for turma in tqdm(df['id_turma'].unique().tolist()):
        matriculas[turma] = set()
        turmaDf = df[df['id_turma'] == turma]
        turmaDf.apply(lambda row: matriculas[turma].add(row['discente']),axis=1)
    #print("\tStoring matriculaSet")
    #df.apply(lambda row: matriculaSet.add((row['id_turma'],row['discente'])),axis=1)
    print(periodo+"\tCreating single rows (4/5)")
    for turma, alunos in tqdm(matriculas.items()):
        turmaDf = df[df['id_turma'] == turma]
        for aluno in alunos:
            newRow = dict()
            newRow['id_turma'] = turma
            newRow['discente'] = aluno
            newRow['id_curso'] = ''
            newRow['n1'] = np.NaN
            newRow['n2'] = np.NaN
            newRow['n3'] = np.NaN
            newRow['media_final'] = np.NaN
            newRow['numero_total_faltas'] = np.NaN
            newRow['descricao'] = ''
            newRow['periodo'] = periodo

            alunoDf = turmaDf[turmaDf['discente'] == aluno]
            first = True
            for index, row in alunoDf.iterrows():
                if(first):
                    newRow['media_final'] = row['media_final']
                    newRow['numero_total_faltas'] = row['numero_total_faltas']
                    newRow['descricao'] = row['descricao']
                    newRow['id_curso'] = row['id_curso']
                if row['unidade'] == 1:
                    newRow['n1'] = row['nota']
                elif row['unidade'] == 2:
                    newRow['n2'] = row['nota']
                else:
                    newRow['n3'] = row['nota']
            localRows.append(newRow)
    print(periodo+"\tDONE (5/5)")
    return localRows

def processDfInPath(path):
    print("Processing " + path + ": ")
    df = pd.read_csv(path,sep=';')
    #df = df.iloc[
    #    np.random.choice(df.index, int(len(df)*0.001))]
    print(path[14:20]+"\tFiltering rows (1/5)")
    mandatoryCols = ['id_turma', 'discente', 'id_curso','unidade', 
                     'media_final', 'numero_total_faltas', 'descricao']
    for mandatory in mandatoryCols:
        df = df[df[mandatory].notnull()]
    df = df[df['unidade'].isin([1,2,3])]
    df = df[df['media_final'] >= 0.0]
    df = df[df['media_final'] <= 10.0]
    df = df[df['descricao'] != 'EXCLUIDA']
    df = df[df['descricao'] != 'DISPENSADO']
    df = df[df['descricao'] != 'MATRICULADO']
    df = df[df['numero_total_faltas'] >= 0]
    print(path[14:20]+"\tAdding rows (2/5)")
    newRows = addRows(df,path[14:20])
    with rowsLock:
        rows.extend(newRows)
    return path[14:20]

#for path in matriculaFilesPaths:
#    processDfInPath(path)

def readSetOfFilesParalell(paths):
    threads = set()
    for path in paths:
        th = Thread(target=processDfInPath,args=(path,))
        th.start()
        threads.add(th)
    for th in threads:
        th.join()

def createMatriculasDf():
    readSetOfFilesParalell(matriculaFilesPaths2014)
    readSetOfFilesParalell(matriculaFilesPaths2015)
    readSetOfFilesParalell(matriculaFilesPaths2016)
    readSetOfFilesParalell(matriculaFilesPaths2017)

    print("Storing results in " + outputDfPath)
    finalDf = pd.DataFrame(rows, columns=cols)
    finalDf['n1'] = finalDf['n1'].astype(float)
    finalDf['n2'] = finalDf['n2'].astype(float)
    finalDf['n3'] = finalDf['n3'].astype(float)
    finalDf['media_final'] = finalDf['media_final'].astype(float)
    finalDf['id_curso'] = finalDf['id_curso'].astype(int)
    finalDf['id_turma'] = finalDf['id_turma'].astype(int)
    finalDf['numero_total_faltas'] = finalDf['numero_total_faltas'].astype(int)
    finalDf.to_csv(outputDfPath, sep='\t', index=False)

def makeSamplingOfMatriculas():
    df = pd.read_csv(outputDfPath, sep='\t')
    df = df.iloc[np.random.choice(df.index, int(len(df)*0.05))]
    df.to_csv('../input/matriculas-05.csv',index=False,sep='\t')

createMatriculasDf()
makeSamplingOfMatriculas()