#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:20:00 2017

@author: pitagoras
"""
import pandas as pd
import numpy as np

turmasDfPath = 'input/turmas.csv'
turmasMiniDfPath = 'input/turmas-05.csv'
matriculasDfPath = 'input/matriculas.csv'
matriculasMiniDfPath = 'input/matriculas-05.csv'

matriculasPlusDfPath = 'input/matriculas-plus.csv'
matriculasPlusMiniDfPath = 'input/matriculas-plus-05.csv'
turmasPlusDfPath = 'input/turmas-plus.csv'
turmasPlusMiniDfPath = 'input/turmas-plus-05.csv'

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

turmasDf = pd.read_csv(turmasDfPath,sep='\t')

studentesOf = dict()
turmas = set(turmasDf['id_turma'].unique.tolist())

for turma in turmas:
    studentesOf[turma] = turmasDf[turmasDf['id_turma'] == turma]

def getAvgFreq(turma):

def getAvgScore(turma):
    
def getStatesPerc(turma):




