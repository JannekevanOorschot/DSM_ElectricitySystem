# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:47:19 2020

@author: oorschotjvan

This script splits the results for wind turbines into elements.

Script is not very efficient, you need to specify the input data: either constant or decreasing MI, and comment the other scenario
To run for constant MI:
    Uncomment line 21 - 32, comment line 36 - 46
    Uncomment line 256- 258, comment line 261 - 263
    Uncomment line 96, 113 and 130, comment line 94, 111, 128
To run for decreasing MI:
    change uncomment and commented regions above
    
    
"""


#%% Import libraries
import pandas as pd


#%% Select either  CONSTANT MI or DECREASING MI

# CONSTANT MI
# HD_on = pd.read_excel(r'in-out-stock-high-scenario.xlsx', sheet_name = 'Onshore')
# HD_off = pd.read_excel(r'in-out-stock-high-scenario.xlsx', sheet_name = 'Offshore')
# HD_total = pd.read_excel(r'in-out-stock-high-scenario.xlsx', sheet_name = 'Total')

# MD_on = pd.read_excel(r'in-out-stock-mid-scenario.xlsx', sheet_name = 'Onshore')
# MD_off = pd.read_excel(r'in-out-stock-mid-scenario.xlsx', sheet_name = 'Offshore')
# MD_total = pd.read_excel(r'in-out-stock-mid-scenario.xlsx', sheet_name = 'Total')

# LD_on = pd.read_excel(r'in-out-stock-low-scenario.xlsx', sheet_name = 'Onshore')
# LD_off = pd.read_excel(r'in-out-stock-low-scenario.xlsx', sheet_name = 'Offshore')
# LD_total = pd.read_excel(r'in-out-stock-low-scenario.xlsx', sheet_name = 'Total')


# DECREASING MI
HD_on = pd.read_excel(r'in-out-stock-high-scenario_s.xlsx', sheet_name = 'Onshore')
HD_off = pd.read_excel(r'in-out-stock-high-scenario_s.xlsx', sheet_name = 'Offshore')
HD_total = pd.read_excel(r'in-out-stock-high-scenario_s.xlsx', sheet_name = 'Total')

MD_on = pd.read_excel(r'in-out-stock-mid-scenario_s.xlsx', sheet_name = 'Onshore')
MD_off = pd.read_excel(r'in-out-stock-mid-scenario_s.xlsx', sheet_name = 'Offshore')
MD_total = pd.read_excel(r'in-out-stock-mid-scenario_s.xlsx', sheet_name = 'Total')

LD_on = pd.read_excel(r'in-out-stock-low-scenario_s.xlsx', sheet_name = 'Onshore')
LD_off = pd.read_excel(r'in-out-stock-low-scenario_s.xlsx', sheet_name = 'Offshore')
LD_total = pd.read_excel(r'in-out-stock-low-scenario_s.xlsx', sheet_name = 'Total')

#%% rename sheets

HD_on = HD_on.rename(columns={'Time':'Jaar'})
HD_off = HD_off.rename(columns={'Time':'Jaar'})
HD_total = HD_total.rename(columns={'Time':'Jaar'})

MD_on = MD_on.rename(columns={'Time':'Jaar'})
MD_off = MD_off.rename(columns={'Time':'Jaar'})
MD_total = MD_total.rename(columns={'Time':'Jaar'})

LD_on = LD_on.rename(columns={'Time':'Jaar'})
LD_off = LD_off.rename(columns={'Time':'Jaar'})
LD_total = LD_total.rename(columns={'Time':'Jaar'})

#%%

Totalen = pd.DataFrame()



#%%
materialen = ['steel', 'iron', 'copper', '_al', 'GFRP', 'resin', 'cast_iron', 'NdFeB', 'fibre', 'GF', 'CF', 'FRP', 'balsa', 'PVC', 'concrete' , 'Yt', 'composite']
S_I_O = ['inflow', 'outflow', 'stock']

#%% overbodig, loop geeft index namen
tuples = list()
for materiaal in materialen:
    for flow in S_I_O:
        tuples.append((materiaal,flow))
    
    
#%%
Totalen_LD = pd.DataFrame()
Totalen_LD.index = MD_on['Jaar']

for materiaal in materialen:    
    for flow in S_I_O:
        f1 = LD_total.filter(regex = materiaal)
        f2 = f1.filter(regex = flow)
        f3 = f2.sum(axis=1) 
        Totalen_LD[(materiaal,flow)]=f3

#Decreasing MI
Totalen_LD.to_excel('LD_total_edit_s.xlsx')
#Constant MI
#Totalen_LD.to_excel('LD_total_edit.xlsx')



Totalen_MD = pd.DataFrame()
Totalen_MD.index = MD_on['Jaar']

for materiaal in materialen:    
    for flow in S_I_O:
        f1 = MD_total.filter(regex = materiaal)
        f2 = f1.filter(regex = flow)
        f3 = f2.sum(axis=1) 
        Totalen_MD[(materiaal,flow)]=f3

#Decreasing MI
Totalen_MD.to_excel('MD_total_edit_s.xlsx')
#Constant MI
#Totalen_MD.to_excel('MD_total_edit.xlsx')



Totalen_HD = pd.DataFrame()
Totalen_HD.index = MD_on['Jaar']

for materiaal in materialen:    
    for flow in S_I_O:
        f1 = HD_total.filter(regex = materiaal)
        f2 = f1.filter(regex = flow)
        f3 = f2.sum(axis=1) 
        Totalen_HD[(materiaal,flow)]=f3

#Decreasing MI
Totalen_HD.to_excel('HD_total_edit_s.xlsx')
#Constant MI
#Totalen_HD.to_excel('HD_total_edit.xlsx')

#%% Elementen
Elementen_HD = pd.DataFrame()

Elementen_HD[('V','stock')] = HD_total['gearbox_steel_stock']*0.0015
Elementen_HD[('V','inflow')] = HD_total['gearbox_steel inflow']*0.0015
Elementen_HD[('V', 'outflow')] = HD_total['gearbox_steel outflow']*0.0015

Elementen_HD[('Mn','stock')] = HD_total['gearbox_steel_stock']*0.0065 + 0.0041*(HD_total['shaft_steel_stock']+HD_total['pitch_steel_stock']+HD_total['yaw_steel_stock'])
Elementen_HD[('Mn','inflow')] = HD_total['gearbox_steel inflow']*0.0065 + 0.0041*(HD_total['shaft_steel inflow']+HD_total['pitch_steel inflow']+HD_total['yaw_steel inflow'])
Elementen_HD[('Mn', 'outflow')] = HD_total['gearbox_steel outflow']*0.0065 + 0.0041*(HD_total['shaft_steel outflow']+HD_total['pitch_steel outflow']+HD_total['yaw_steel outflow'])

Elementen_HD[('Cr','stock')] = HD_total['gearbox_steel_stock']*0.021 + 0.0065*(HD_total['shaft_steel_stock']+HD_total['pitch_steel_stock']+HD_total['yaw_steel_stock'])
Elementen_HD[('Cr','inflow')] = HD_total['gearbox_steel inflow']*0.021 + 0.0065*(HD_total['shaft_steel inflow']+HD_total['pitch_steel inflow']+HD_total['yaw_steel inflow'])
Elementen_HD[('Cr', 'outflow')] = HD_total['gearbox_steel outflow']*0.021 + 0.0065*(HD_total['shaft_steel outflow']+HD_total['pitch_steel outflow']+HD_total['yaw_steel outflow'])

Elementen_HD[('Mo','stock')] = HD_total['gearbox_steel_stock']*0.0025 + 0.00215*(HD_total['shaft_steel_stock']+HD_total['pitch_steel_stock']+HD_total['yaw_steel_stock'])
Elementen_HD[('Mo','inflow')] = HD_total['gearbox_steel inflow']*0.0025 +  0.00215*(HD_total['shaft_steel inflow']+HD_total['pitch_steel inflow']+HD_total['yaw_steel inflow'])
Elementen_HD[('Mo', 'outflow')] = HD_total['gearbox_steel outflow']*0.0025 + 0.00215*(HD_total['shaft_steel outflow']+HD_total['pitch_steel outflow']+HD_total['yaw_steel outflow'])

Elementen_HD[('Ni','stock')] = HD_total['gearbox_steel_stock']*0.0085 + HD_total['generator_NdFeB_stock']*0.0286 # volgens Munchen et al., 2018 rond de 2.86% Ni in NdFeB magneten
Elementen_HD[('Ni','inflow')] = HD_total['gearbox_steel inflow']*0.0085 + HD_total['generator_NdFeB inflow']*0.0286
Elementen_HD[('Ni', 'outflow')] = HD_total['gearbox_steel outflow']*0.0085 + HD_total['generator_NdFeB outflow']*0.0286

Elementen_HD[('Si','stock')] = HD_total['gearbox_steel_stock']*0.004 + 0.0035*(HD_total['shaft_steel_stock']+HD_total['pitch_steel_stock']+HD_total['yaw_steel_stock'])
Elementen_HD[('Si','inflow')] = HD_total['gearbox_steel inflow']*0.004 + 0.0035*(HD_total['shaft_steel inflow']+HD_total['pitch_steel inflow']+HD_total['yaw_steel inflow'])
Elementen_HD[('Si', 'outflow')] = HD_total['gearbox_steel outflow']*0.004 + + 0.0035*(HD_total['shaft_steel outflow']+HD_total['pitch_steel outflow']+HD_total['yaw_steel outflow'])

Elementen_HD[('Nd','stock')] = HD_total['generator_NdFeB_stock']*0.2395
Elementen_HD[('Nd', 'inflow')] = HD_total['generator_NdFeB inflow']*0.2395
Elementen_HD[('Nd', 'outflow')] = HD_total['generator_NdFeB outflow']*0.2395

Elementen_HD[('B','stock')] = HD_total['generator_NdFeB_stock']*0.009
Elementen_HD[('B', 'inflow')] = HD_total['generator_NdFeB inflow']*0.009
Elementen_HD[('B', 'outflow')] = HD_total['generator_NdFeB outflow']*0.009

Elementen_HD[('Dy','stock')] = HD_total['generator_NdFeB_stock']*0.0098
Elementen_HD[('Dy', 'inflow')] = HD_total['generator_NdFeB inflow']*0.0098
Elementen_HD[('Dy', 'outflow')] = HD_total['generator_NdFeB outflow']*0.0098

Elementen_HD[('Pr','stock')] = HD_total['generator_NdFeB_stock']*0.042
Elementen_HD[('Pr', 'inflow')] = HD_total['generator_NdFeB inflow']*0.042
Elementen_HD[('Pr', 'outflow')] = HD_total['generator_NdFeB outflow']*0.042

Elementen_HD[('Tb','stock')] = HD_total['generator_NdFeB_stock']*0.0019
Elementen_HD[('Tb', 'inflow')] = HD_total['generator_NdFeB inflow']*0.0019
Elementen_HD[('Tb', 'outflow')] = HD_total['generator_NdFeB outflow']*0.0019

Elementen_HD.index = LD_on['Jaar']

#%%
Elementen_MD = pd.DataFrame()

Elementen_MD[('V','stock')] = MD_total['gearbox_steel_stock']*0.0015
Elementen_MD[('V','inflow')] = MD_total['gearbox_steel inflow']*0.0015
Elementen_MD[('V', 'outflow')] = MD_total['gearbox_steel outflow']*0.0015

Elementen_MD[('Mn','stock')] = MD_total['gearbox_steel_stock']*0.0065 + 0.0041*(MD_total['shaft_steel_stock']+MD_total['pitch_steel_stock']+MD_total['yaw_steel_stock'])
Elementen_MD[('Mn','inflow')] = MD_total['gearbox_steel inflow']*0.0065 + 0.0041*(MD_total['shaft_steel inflow']+MD_total['pitch_steel inflow']+MD_total['yaw_steel inflow'])
Elementen_MD[('Mn', 'outflow')] = MD_total['gearbox_steel outflow']*0.0065 + 0.0041*(MD_total['shaft_steel outflow']+MD_total['pitch_steel outflow']+MD_total['yaw_steel outflow'])

Elementen_MD[('Cr','stock')] = MD_total['gearbox_steel_stock']*0.021 + 0.0065*(MD_total['shaft_steel_stock']+MD_total['pitch_steel_stock']+MD_total['yaw_steel_stock'])
Elementen_MD[('Cr','inflow')] = MD_total['gearbox_steel inflow']*0.021 + 0.0065*(MD_total['shaft_steel inflow']+MD_total['pitch_steel inflow']+MD_total['yaw_steel inflow'])
Elementen_MD[('Cr', 'outflow')] = MD_total['gearbox_steel outflow']*0.021 + 0.0065*(MD_total['shaft_steel outflow']+MD_total['pitch_steel outflow']+MD_total['yaw_steel outflow'])

Elementen_MD[('Mo','stock')] = MD_total['gearbox_steel_stock']*0.0025 + 0.00215*(MD_total['shaft_steel_stock']+MD_total['pitch_steel_stock']+MD_total['yaw_steel_stock'])
Elementen_MD[('Mo','inflow')] = MD_total['gearbox_steel inflow']*0.0025 +  0.00215*(MD_total['shaft_steel inflow']+MD_total['pitch_steel inflow']+MD_total['yaw_steel inflow'])
Elementen_MD[('Mo', 'outflow')] = MD_total['gearbox_steel outflow']*0.0025 + 0.00215*(MD_total['shaft_steel outflow']+MD_total['pitch_steel outflow']+MD_total['yaw_steel outflow'])

Elementen_MD[('Ni','stock')] = MD_total['gearbox_steel_stock']*0.0085 + MD_total['generator_NdFeB_stock']*0.0286 # volgens Munchen et al., 2018 rond de 2.86% Ni in NdFeB magneten
Elementen_MD[('Ni','inflow')] = MD_total['gearbox_steel inflow']*0.0085 + MD_total['generator_NdFeB inflow']*0.0286
Elementen_MD[('Ni', 'outflow')] = MD_total['gearbox_steel outflow']*0.0085 + MD_total['generator_NdFeB outflow']*0.0286

Elementen_MD[('Si','stock')] = MD_total['gearbox_steel_stock']*0.004 + 0.0035*(MD_total['shaft_steel_stock']+MD_total['pitch_steel_stock']+MD_total['yaw_steel_stock'])
Elementen_MD[('Si','inflow')] = MD_total['gearbox_steel inflow']*0.004 + 0.0035*(MD_total['shaft_steel inflow']+MD_total['pitch_steel inflow']+MD_total['yaw_steel inflow'])
Elementen_MD[('Si', 'outflow')] = MD_total['gearbox_steel outflow']*0.004 + + 0.0035*(MD_total['shaft_steel outflow']+MD_total['pitch_steel outflow']+MD_total['yaw_steel outflow'])

Elementen_MD[('Nd','stock')] = MD_total['generator_NdFeB_stock']*0.2395
Elementen_MD[('Nd', 'inflow')] = MD_total['generator_NdFeB inflow']*0.2395
Elementen_MD[('Nd', 'outflow')] = MD_total['generator_NdFeB outflow']*0.2395

Elementen_MD[('B','stock')] = MD_total['generator_NdFeB_stock']*0.009
Elementen_MD[('B', 'inflow')] = MD_total['generator_NdFeB inflow']*0.009
Elementen_MD[('B', 'outflow')] = MD_total['generator_NdFeB outflow']*0.009

Elementen_MD[('Dy','stock')] = MD_total['generator_NdFeB_stock']*0.0098
Elementen_MD[('Dy', 'inflow')] = MD_total['generator_NdFeB inflow']*0.0098
Elementen_MD[('Dy', 'outflow')] = MD_total['generator_NdFeB outflow']*0.0098

Elementen_MD[('Pr','stock')] = MD_total['generator_NdFeB_stock']*0.042
Elementen_MD[('Pr', 'inflow')] = MD_total['generator_NdFeB inflow']*0.042
Elementen_MD[('Pr', 'outflow')] = MD_total['generator_NdFeB outflow']*0.042

Elementen_MD[('Tb','stock')] = MD_total['generator_NdFeB_stock']*0.0019
Elementen_MD[('Tb', 'inflow')] = MD_total['generator_NdFeB inflow']*0.0019
Elementen_MD[('Tb', 'outflow')] = MD_total['generator_NdFeB outflow']*0.0019

Elementen_MD.index = LD_on['Jaar']        

#%%

Elementen_LD = pd.DataFrame()

Elementen_LD[('V','stock')] = LD_total['gearbox_steel_stock']*0.0015
Elementen_LD[('V','inflow')] = LD_total['gearbox_steel inflow']*0.0015
Elementen_LD[('V', 'outflow')] = LD_total['gearbox_steel outflow']*0.0015

Elementen_LD[('Mn','stock')] = LD_total['gearbox_steel_stock']*0.0065 + 0.0041*(LD_total['shaft_steel_stock']+LD_total['pitch_steel_stock']+LD_total['yaw_steel_stock'])
Elementen_LD[('Mn','inflow')] = LD_total['gearbox_steel inflow']*0.0065 + 0.0041*(LD_total['shaft_steel inflow']+LD_total['pitch_steel inflow']+LD_total['yaw_steel inflow'])
Elementen_LD[('Mn', 'outflow')] = LD_total['gearbox_steel outflow']*0.0065 + 0.0041*(LD_total['shaft_steel outflow']+LD_total['pitch_steel outflow']+LD_total['yaw_steel outflow'])

Elementen_LD[('Cr','stock')] = LD_total['gearbox_steel_stock']*0.021 + 0.0065*(LD_total['shaft_steel_stock']+LD_total['pitch_steel_stock']+LD_total['yaw_steel_stock'])
Elementen_LD[('Cr','inflow')] = LD_total['gearbox_steel inflow']*0.021 + 0.0065*(LD_total['shaft_steel inflow']+LD_total['pitch_steel inflow']+LD_total['yaw_steel inflow'])
Elementen_LD[('Cr', 'outflow')] = LD_total['gearbox_steel outflow']*0.021 + 0.0065*(LD_total['shaft_steel outflow']+LD_total['pitch_steel outflow']+LD_total['yaw_steel outflow'])

Elementen_LD[('Mo','stock')] = LD_total['gearbox_steel_stock']*0.0025 + 0.00215*(LD_total['shaft_steel_stock']+LD_total['pitch_steel_stock']+LD_total['yaw_steel_stock'])
Elementen_LD[('Mo','inflow')] = LD_total['gearbox_steel inflow']*0.0025 +  0.00215*(LD_total['shaft_steel inflow']+LD_total['pitch_steel inflow']+LD_total['yaw_steel inflow'])
Elementen_LD[('Mo', 'outflow')] = LD_total['gearbox_steel outflow']*0.0025 + 0.00215*(LD_total['shaft_steel outflow']+LD_total['pitch_steel outflow']+LD_total['yaw_steel outflow'])

Elementen_LD[('Ni','stock')] = LD_total['gearbox_steel_stock']*0.0085 + LD_total['generator_NdFeB_stock']*0.0286 # volgens Munchen et al., 2018 rond de 2.86% Ni in NdFeB magneten
Elementen_LD[('Ni','inflow')] = LD_total['gearbox_steel inflow']*0.0085 + LD_total['generator_NdFeB inflow']*0.0286
Elementen_LD[('Ni', 'outflow')] = LD_total['gearbox_steel outflow']*0.0085 + LD_total['generator_NdFeB outflow']*0.0286

Elementen_LD[('Si','stock')] = LD_total['gearbox_steel_stock']*0.004 + 0.0035*(LD_total['shaft_steel_stock']+LD_total['pitch_steel_stock']+LD_total['yaw_steel_stock'])
Elementen_LD[('Si','inflow')] = LD_total['gearbox_steel inflow']*0.004 + 0.0035*(LD_total['shaft_steel inflow']+LD_total['pitch_steel inflow']+LD_total['yaw_steel inflow'])
Elementen_LD[('Si', 'outflow')] = LD_total['gearbox_steel outflow']*0.004 + + 0.0035*(LD_total['shaft_steel outflow']+LD_total['pitch_steel outflow']+LD_total['yaw_steel outflow'])

Elementen_LD[('Nd','stock')] = LD_total['generator_NdFeB_stock']*0.2395
Elementen_LD[('Nd', 'inflow')] = LD_total['generator_NdFeB inflow']*0.2395
Elementen_LD[('Nd', 'outflow')] = LD_total['generator_NdFeB outflow']*0.2395

Elementen_LD[('B','stock')] = LD_total['generator_NdFeB_stock']*0.009
Elementen_LD[('B', 'inflow')] = LD_total['generator_NdFeB inflow']*0.009
Elementen_LD[('B', 'outflow')] = LD_total['generator_NdFeB outflow']*0.009

Elementen_LD[('Dy','stock')] = LD_total['generator_NdFeB_stock']*0.0098
Elementen_LD[('Dy', 'inflow')] = LD_total['generator_NdFeB inflow']*0.0098
Elementen_LD[('Dy', 'outflow')] = LD_total['generator_NdFeB outflow']*0.0098

Elementen_LD[('Pr','stock')] = LD_total['generator_NdFeB_stock']*0.042
Elementen_LD[('Pr', 'inflow')] = LD_total['generator_NdFeB inflow']*0.042
Elementen_LD[('Pr', 'outflow')] = LD_total['generator_NdFeB outflow']*0.042

Elementen_LD[('Tb','stock')] = LD_total['generator_NdFeB_stock']*0.0019
Elementen_LD[('Tb', 'inflow')] = LD_total['generator_NdFeB inflow']*0.0019
Elementen_LD[('Tb', 'outflow')] = LD_total['generator_NdFeB outflow']*0.0019

Elementen_LD.index = LD_on['Jaar']        

#%%

# Select constant or decreasing MI and make sure to align with previous steps

# Constant MI
# Elementen_LD.to_excel('Elementen_LD.xlsx')
# Elementen_MD.to_excel('Elementen_MD.xlsx')
# Elementen_HD.to_excel('Elementen_HD.xlsx')

# Decreasing MI
Elementen_LD.to_excel('Elementen_LD_s.xlsx')
Elementen_MD.to_excel('Elementen_MD_s.xlsx')
Elementen_HD.to_excel('Elementen_HD_s.xlsx')

