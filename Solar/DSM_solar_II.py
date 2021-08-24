# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:12:05 2020

@author: oorschotjvan
"""


#%% import libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt   

from dynamic_stock_model_odym import DynamicStockModel #imports the Open Dynamic Material Systems Model (ODYM)

#%% 

solar_H = pd.read_excel(r'Solar_DSM.xlsx', sheet_name = 'H') 
solar_M = pd.read_excel(r'Solar_DSM.xlsx', sheet_name = 'M')
solar_L = pd.read_excel(r'Solar_DSM.xlsx', sheet_name = 'L')


MS = pd.read_excel(r'Solar_DSM.xlsx', sheet_name = 'MS') #Marketshares of technologies

solar = solar_L

solar_DSM = DynamicStockModel(t=solar['Year'], s = solar['MW'],lt= {'Type':'Weibull', 'Shape':np.array([5.3759]),'Scale': solar['lt']})

#%% Calculate inflow, outflow, stock balance, stock per cohort, outfloc per cohort

CheckStr = solar_DSM.dimension_check()

S_C, O_C, I = solar_DSM.compute_stock_driven_model()

O = solar_DSM.compute_outflow_total()
DS = solar_DSM.compute_stock_change()
Bal = solar_DSM.check_stock_balance()

#%% Create DataFrames

years = {'year': np.arange(1990, 2051, 1)}
solar_dsm = pd.DataFrame(years)
solar_dsm['Stock total'] = solar['MW']
solar_dsm['Inflow total'] = I
solar_dsm['Outflow total'] = O
solar_dsm['%m c-Si']=MS['m% c-Si']
solar_dsm['%m a-Si']=MS['m% a-Si']
solar_dsm['%m CdTe']=MS['m% CdTe']
solar_dsm['%m CIGS']=MS['m% CIGS']

#solar_dsm['Stock change'] = DS
#solar_dsm['Stock balance']= Bal

Stock_change_cohort = pd.DataFrame(S_C)
Outflow_cohort = pd.DataFrame(O_C)

#%% Add material intensities (in ton/MW for 17 materials/elements)

MI = pd.read_excel(r'Solar_DSM.xlsx', sheet_name = 'MI') 

#%%
# ['Steel','Aluminum', 'Copper', 'Ag', 'Cd', 'Te', 'Ga', 'In', 'Ge', 'Si']
materials = list(MI.columns)
print(materials)
#%%
for column in materials:
    newColumn = []
    if column != "Unnamed: 0":
        print(column)
        for index, row in solar_dsm.iterrows():
            print(index,row)
            inflow_material = solar_dsm.loc[index, 'Inflow total']*solar_dsm.loc[index,'%m c-Si']*MI.at[1,column] + solar_dsm.loc[index, 'Inflow total']*solar_dsm.loc[index,'%m a-Si']*MI.at[2,column] + solar_dsm.loc[index, 'Inflow total']*solar_dsm.loc[index,'%m CdTe']*MI.at[3,column] + solar_dsm.loc[index, 'Inflow total']*solar_dsm.loc[index,'%m CIGS']*MI.at[4,column]
            newColumn.append(inflow_material)   
        solar_dsm['I_' + column] = newColumn


#%% Compute inflow driven model
        
for column in solar_dsm:
    columnName = column.split('_')
    if columnName[0] == 'I':
        solar_DSM_2 = DynamicStockModel(t = solar_dsm['year'], i = solar_dsm[column], lt = {'Type': 'Weibull', 'Shape': np.array([5.3759]), 'Scale': solar['lt']})
        #CheckStr, ExitFlag = solar_DSM_2.dimension_check()
        #print(CheckStr)
        Stock_by_cohort = solar_DSM_2.compute_s_c_inflow_driven()
        S = solar_DSM_2.compute_stock_total()
        O_C = solar_DSM_2.compute_o_c_from_s_c()
        O = solar_DSM_2.compute_outflow_total()
        #DS, ExitFlag  = solar_DSM_2.compute_stock_change()
        #print(solar_DSM_2.dimension_check()[0]) # dimension_check returns two variables, but we only print the first one, which has index 0.
        #Bal, ExitFlag = solar_DSM_2.check_stock_balance()
        solar_dsm['S_'+ columnName[1]] = S
        solar_dsm['O_'+ columnName[1]] = O

#%% To excel

# Set name to H, M or L

solar_dsm.to_excel('Solar_output_L_constant_MI.xlsx')





