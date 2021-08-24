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

Tower = pd.read_excel(r'Tower_HV.xlsx', sheet_name= 'Tower_stock')


# Steel intensity

Tower_MI = pd.read_excel(r'Tower_HV.xlsx', sheet_name= 'MI_towers')
MI_steel = Tower_MI.iloc[8,9]

Tower['Stock_H_steel'] = Tower['H']*MI_steel
Tower['Stock_M_steel'] = Tower['M']*MI_steel
Tower['Stock_L_steel'] = Tower['L']*MI_steel

#%%

years = Tower['Year']

scenarios = ['Stock_H_steel', 'Stock_M_steel', 'Stock_L_steel']
for scenario in scenarios:
    lifespan = 40
    DSM = DynamicStockModel(t = years, s = Tower[scenario], lt = {'Type': 'Normal', 'Mean': np.array([lifespan]), 'StdDev': np.array([lifespan*0.214])})


    CheckStr = DSM.dimension_check()

    S_C, O_C, I = DSM.compute_stock_driven_model()

    O = DSM.compute_outflow_total()
    DS = DSM.compute_stock_change()
    Bal = DSM.check_stock_balance()
    
    Tower['Inflow_'+scenario[6:7]+'_steel'] = I
    Tower['Outflow_'+ scenario[6:7]+'_steel'] = O
    


#%%
Tower.to_excel('Tower_output.xlsx')


