# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:00:33 2021

@author: jvano
"""

#%% import libraries
import numpy as np
import pandas as pd


from dynamic_stock_model_odym import DynamicStockModel #imports the Open Dynamic Material Systems Model (ODYM)

#%% Load Excel sheet, input data

# Set to L, M or H
ST = pd.read_excel(r'Substat_trafos.xlsx', sheet_name= 'st_stock_L')


#%%

years = ST['Year']

types = ['Stock_Sub_HV', 'Stock_Sub_MV', 'Stock_Sub_LV', 'Stock_Trafo_HV', 'Stock_Trafo_MV','Stock_Trafo_LV']


for type in types: 
    t = type.split('_')
    if t[1] == 'Sub':
        lifespan = 40
    elif t[1] == 'Trafo':
        lifespan = 30
    DSM = DynamicStockModel(t = years, s = ST[type], lt = {'Type': 'Normal', 'Mean': np.array([lifespan]), 'StdDev': np.array([lifespan*0.214])})


    CheckStr = DSM.dimension_check()

    S_C, O_C, I = DSM.compute_stock_driven_model()

    O = DSM.compute_outflow_total()
    DS = DSM.compute_stock_change()
    Bal = DSM.check_stock_balance()
    
    ST['Inflow_'+ t[1]+'_'+t[2]] = I
    ST['Outflow_'+ t[1]+'_'+t[2]] = O


#%%
ST_mat = pd.DataFrame(years)
ST_MI = pd.read_excel(r'Substat_trafos.xlsx', sheet_name= 'st_MI')
ST_MI = ST_MI.set_index('kg/unit')
materials = ['Steel', 'Al', 'Cu']

#%%
for column in ST.columns:
    c = column.split('_')
    if column != 'Year':
        for mat in materials:
            if c[1] == 'Sub':
                if c[2] == 'HV':
                    ST_mat[column+'_'+mat] = ST_MI.loc['Sub_HV', mat]*ST.loc[:,column]
                elif c[2] == 'MV':
                    ST_mat[column+'_'+mat] = ST_MI.loc['Sub_MV', mat]*ST.loc[:, column]
                elif c[2] == 'LV':
                    ST_mat[column+'_'+mat] = ST_MI.loc['Sub_LV', mat]*ST.loc[:, column]   
            elif c[1] == 'Trafo':
                if c[2] == 'HV':
                    ST_mat[column+'_'+mat] = ST_MI.loc['Trafo_HV', mat]*ST.loc[:, column]
                elif c[2] == 'MV':
                    ST_mat[column+'_'+mat] = ST_MI.loc['Trafo_MV', mat]*ST.loc[:, column]
                elif c[2] == 'LV':
                    ST_mat[column+'_'+mat] = ST_MI.loc['Trafo_LV', mat]*ST.loc[:, column]            
#%%      

# Set name to H, M or L

ST_mat.to_excel('substat_trafo_output_L.xlsx')

ST_mat_aggr = pd.DataFrame(years)


P = ['Stock', 'Inflow', 'Outflow']
T = ['Sub', 'Trafo']
M = ['Steel', 'Al', 'Cu']


for process in P:
    print(f"Process is {process}")
    for tech in T:
        for material in M:
            filter = []
            for columnName in ST_mat.columns:    
                if columnName != 'Year':
                    d = columnName.split('_')
                    if ((d[0] == process) & (d[1] == tech) & (d[3] == material)):
                        filter = filter + [columnName]
            print(filter)
            ST_mat_aggr[process+'_'+tech+'_'+material] = ST_mat[filter].sum(axis = 1)
#%%

# Set name to H, M or L

ST_mat_aggr.to_excel('Substat_trafo_aggr_L.xlsx')


