#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:20:00 2017

@author: pitagoras
"""
import pandas as pd
import numpy as np
from tqdm import tqdm

turmasDfPath = '../input/turmas.csv'
turmasMiniDfPath = '../input/turmas-05.csv'
matriculasDfPath = '../input/matriculas.csv'
matriculasMiniDfPath = '../input/matriculas-05.csv'

matriculasPlusDfPath = '../input/matriculas-plus.csv'
matriculasPlusMiniDfPath = '../input/matriculas-plus-05.csv'
turmasPlusDfPath = '../input/turmas-plus.csv'
turmasPlusMiniDfPath = '../input/turmas-plus-05.csv'

doAll = True
if not doAll:
    turmasDfPath = turmasMiniDfPath
    turmasPlusDfPath = turmasPlusMiniDfPath

matriculaStates = ['APROVADO',
 'APROVADO POR NOTA',
 'REPROVADO POR M\xc3\x89DIA E POR FALTAS',
 'REPROVADO',
 'CANCELADO',
 'TRANCADO',
 'REPROVADO POR NOTA',
 'REPROVADO POR FALTAS',
 'REPROVADO POR NOTA E FALTA',
 'CUMPRIU',
 'DESISTENCIA',
 'TRANSFERIDO']

print("Reading input data")
matriculasPlusDf = pd.read_csv(matriculasPlusDfPath)
turmasDf = pd.read_csv(turmasDfPath)
studentsOf = dict()
turmas = set(turmasDf['id_turma'].unique().tolist())
turmaStatePerc = dict()

def getMeanFaults(turma):
    students = studentsOf[turma]
    return students['perc_faltas'].mean()

def getMeanScore(turma):
    students = studentsOf[turma]
    return students['media_final'].mean()
    
def getStatesPerc(turma):
    states = dict()
    students = studentsOf[turma]
    for state in matriculaStates:
        count = len(students[students['descricao'] == state])
        states[state] = count/float(len(students))
    turmaStatePerc[turma] = states
    return states
        
print("Beggining with " + str(len(turmasDf)) + " classes")
print("Dividing students by class.")
for turma in tqdm(turmas):
    studentsOf[turma] = matriculasPlusDf[matriculasPlusDf['id_turma'] == turma]

print("Removing classes with no students")
turmasDf['no_students'] = turmasDf.apply(lambda row: len(studentsOf[row['id_turma']]) == 0,
        axis = 1)
turmasDf = turmasDf[turmasDf['no_students'] == False]
del turmasDf['no_students']
print(str(len(turmasDf)) + " classes now")

print("Computing mean faults")
turmasDf['media_faltas'] = turmasDf.apply(
        lambda row: getMeanFaults(row['id_turma']), axis=1)

print("Computing mean scores")
turmasDf['media_alunos'] = turmasDf.apply(
        lambda row: getMeanScore(row['id_turma']), axis=1)

print("Computing student's registration states[1/2]")
turmasDf.apply(lambda row: getStatesPerc(row['id_turma']), axis=1)
print("Computing student's registration states[2/2]")
for state in tqdm(matriculaStates):
    turmasDf[state] = turmasDf.apply(
            lambda row: turmaStatePerc[row['id_turma']][state],
            axis=1)
    turmasDf[state] = turmasDf[state].astype(float)

print("Writing final dataframe")
turmasDf['media_alunos'] = turmasDf['media_alunos'].astype(float)
turmasDf['media_faltas'] = turmasDf['media_faltas'].astype(float)

turmasDf.to_csv(turmasPlusDfPath, index=False)