# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:24:54 2020

@author: Judith
"""

# -*- coding: utf-8 -*-
"""
Judith van der Horst

EHS and HS overhead
"""
# Import libraries

import numpy as np

from dynamic_stock_model_odym import DynamicStockModel #imports the Open Dynamic Material Systems Model (ODYM)

#packages voor exceldata
import pandas as pd

#%%
# Define path
data_path = 'Datasheet_EHS_HS.xlsx'

#reading the excel datafile and defining the historic stock
dfhistoric = pd.read_excel (data_path, sheet_name='aggregated_overhead')
dffuture = pd.read_excel (data_path, sheet_name='future_overhead')
mat_intens = pd.read_excel (data_path, sheet_name= 'material_intensities')





#%% defining the EHS stocks
#defining stock of the regional scenario

historicstockEHS = dfhistoric['stock EHS [km]'].tolist()

regionalstockEHS = historicstockEHS.copy()
regfstockEHS = dffuture['EHS regional'].tolist()
for i in regfstockEHS:
    regionalstockEHS.append(i)

#defining stock of the national scenario
nationalstockEHS = historicstockEHS.copy()
natfstockEHS = dffuture['EHS national'].tolist()
for i in natfstockEHS:
    nationalstockEHS.append(i)
    
#defining stock of the international scenario
internationalstockEHS = historicstockEHS.copy()
intfstockEHS = dffuture['EHS international'].tolist()
for i in intfstockEHS:
    internationalstockEHS.append(i)

#defining stock of the generic scenario
genericstockEHS = historicstockEHS.copy()
genfstockEHS = dffuture['EHS generic'].tolist()
for i in genfstockEHS:
    genericstockEHS.append(i)






#%% defining the HS stocks
historicstockHS = dfhistoric['stock HS [km]'].tolist()

#defining stock of the regional scenario
regionalstockHS = historicstockHS.copy()
regfstockHS = dffuture['HS regional'].tolist()
for i in regfstockHS:
    regionalstockHS.append(i)

#defining stock of the national scenario
nationalstockHS = historicstockHS.copy()
natfstockHS = dffuture['HS national'].tolist()
for i in natfstockHS:
    nationalstockHS.append(i)
    
#defining stock of the international scenario
internationalstockHS = historicstockHS.copy()
intfstockHS = dffuture['HS international']
for i in intfstockHS:
    internationalstockHS.append(i)

#defining stock of the generic scenario
genericstockHS = historicstockHS.copy()
genfstockHS = dffuture['HS generic']
for i in genfstockHS:
    genericstockHS.append(i)





#%% defining other needed variables
    
#lifetime distribution for the dynamic stock models    
lifetime_distribution = {'Type': 'Normal', 'Mean': np.array([60]), 'StdDev': np.array([8])}

#the timespan of the model
timespan = np.arange(1933, 2051, 1)

#the timespan for future flows, used for graphs
future_timespan = np.arange(2000, 2051, 1)  



    
#%% calculating the EHS DSMs for all four scenarios
    
#calculating regional dynamic stock model
EHSregionalDSM = DynamicStockModel(t = timespan, s = regionalstockEHS, lt = lifetime_distribution)

S_C_regEHS, O_C_regEHS, I_regEHS = EHSregionalDSM.compute_stock_driven_model()
O_regEHS = EHSregionalDSM.compute_outflow_total()
DS_regEHS = EHSregionalDSM.compute_stock_change()
Bal_regEHS = EHSregionalDSM.check_stock_balance()

#calculating national dynamic stock model
EHSnationalDSM = DynamicStockModel(t = timespan, s = nationalstockEHS, lt = lifetime_distribution)

S_C_natEHS, O_C_natEHS, I_natEHS = EHSnationalDSM.compute_stock_driven_model()
O_natEHS = EHSnationalDSM.compute_outflow_total()
DS_natEHS = EHSnationalDSM.compute_stock_change()
Bal_natEHS = EHSnationalDSM.check_stock_balance()

#calculating international dynamic stock model
EHSinternationalDSM = DynamicStockModel(t = timespan, s = internationalstockEHS, lt = lifetime_distribution)

S_C_intEHS, O_C_intEHS, I_intEHS = EHSinternationalDSM.compute_stock_driven_model()
O_intEHS = EHSinternationalDSM.compute_outflow_total()
DS_intEHS = EHSinternationalDSM.compute_stock_change()
Bal_intEHS = EHSinternationalDSM.check_stock_balance()

#calculating generic dynamic stock model
EHSgenericDSM = DynamicStockModel(t = timespan, s = genericstockEHS, lt = lifetime_distribution)

S_C_genEHS, O_C_genEHS, I_genEHS = EHSgenericDSM.compute_stock_driven_model()
O_genEHS = EHSgenericDSM.compute_outflow_total()
DS_genEHS = EHSgenericDSM.compute_stock_change()
Bal_genEHS = EHSgenericDSM.check_stock_balance()





#%% calculating the HS DSM's for all 4 scenarios

#calculating regional dynamic stock model
HSregionalDSM = DynamicStockModel(t = timespan, s = regionalstockHS, lt = lifetime_distribution)

S_C_regHS, O_C_regHS, I_regHS = HSregionalDSM.compute_stock_driven_model()
O_regHS = HSregionalDSM.compute_outflow_total()
DS_regHS = HSregionalDSM.compute_stock_change()
Bal_regHS = HSregionalDSM.check_stock_balance()


#calculating national dynamic stock model
HSnationalDSM = DynamicStockModel(t = timespan, s = nationalstockHS, lt = lifetime_distribution)

S_C_natHS, O_C_natHS, I_natHS = HSnationalDSM.compute_stock_driven_model()
O_natHS = HSnationalDSM.compute_outflow_total()
DS_natHS = HSnationalDSM.compute_stock_change()
Bal_natHS = HSnationalDSM.check_stock_balance()

#calculating international dynamic stock model
HSinternationalDSM = DynamicStockModel(t = timespan, s = internationalstockHS, lt = lifetime_distribution)

S_C_intHS, O_C_intHS, I_intHS = HSinternationalDSM.compute_stock_driven_model()
O_intHS = HSinternationalDSM.compute_outflow_total()
DS_intHS = HSinternationalDSM.compute_stock_change()
Bal_intHS = HSinternationalDSM.check_stock_balance()

#calculating generic dynamic stock model
HSgenericDSM = DynamicStockModel(t = timespan, s = genericstockHS, lt = lifetime_distribution)

S_C_genHS, O_C_genHS, I_genHS = HSgenericDSM.compute_stock_driven_model()
O_genHS = HSgenericDSM.compute_outflow_total()
DS_genHS = HSgenericDSM.compute_stock_change()
Bal_genHS = HSgenericDSM.check_stock_balance()





#%% material intensities
steel_intensity = mat_intens.loc[1, '(E)HS_overhead']
aluminium_intensity = mat_intens.loc[0, '(E)HS_overhead']


#%% calculating the steel in and outflows (combined EHS and HS)

#inflows
steel_inflow_reg = [(EHSregionalDSM.i[i] + HSregionalDSM.i[i])*steel_intensity for i in range(len(EHSregionalDSM.i))]
steel_inflow_nat = [(EHSnationalDSM.i[i] + HSnationalDSM.i[i])*steel_intensity for i in range(len(EHSregionalDSM.i))]
steel_inflow_int = [(EHSinternationalDSM.i[i] + HSinternationalDSM.i[i])*steel_intensity for i in range(len(EHSregionalDSM.i))]
steel_inflow_gen = [(EHSgenericDSM.i[i] + HSgenericDSM.i[i])*steel_intensity for i in range(len(EHSregionalDSM.i))]

#outflows
#Because of the long lifespan, the outflows only depend on historical inflows, which are the same for each scenario. 
#Thus the outflows are also the same for each scenario. We use here the regional scenario to calculate those.
steel_outflow = [(EHSregionalDSM.o[i] + HSregionalDSM.o[i])*steel_intensity for i in range(len(EHSregionalDSM.o))]



#%% calculating the alumiinium in and outflows (combined EHS and HS) 

#inflows
alu_inflow_reg = [(EHSregionalDSM.i[i] + HSregionalDSM.i[i])*aluminium_intensity for i in range(len(EHSregionalDSM.i))]
alu_inflow_nat = [(EHSnationalDSM.i[i] + HSnationalDSM.i[i])*aluminium_intensity for i in range(len(EHSregionalDSM.i))]
alu_inflow_int = [(EHSinternationalDSM.i[i] + HSinternationalDSM.i[i])*aluminium_intensity for i in range(len(EHSregionalDSM.i))]
alu_inflow_gen = [(EHSgenericDSM.i[i] + HSgenericDSM.i[i])*aluminium_intensity for i in range(len(EHSregionalDSM.i))]

#outflows
#Because of the long lifespan, the outflows only depend on historical inflows, which are the same for each scenario. 
#Thus the outflows are also the same for each scenario. We use here the regional scenario to calculate those.
alu_outflow = [(EHSregionalDSM.o[i] + HSregionalDSM.o[i])*aluminium_intensity for i in range(len(EHSregionalDSM.i))]






#%% putting all data into excelsheet. Needed in order to combine the data of all different voltage levels.

# creating dataframes to write to excel
EHS_stocks = {'years': timespan,
             'regional_EHS_stocks': EHSregionalDSM.s,
             'national_EHS_stocks': EHSnationalDSM.s,
             'international_EHS_stocks': EHSinternationalDSM.s,
             'generic_EHS_stocks': EHSgenericDSM.s}
dfEHSstocks = pd.DataFrame(EHS_stocks, columns=['years', 'regional_EHS_stocks', 'national_EHS_stocks', 'international_EHS_stocks', 'generic_EHS_stocks'])

# creating dataframes to write to excel
HS_stocks = {'years': timespan,
             'regional_HS_stocks': HSregionalDSM.s,
             'national_HS_stocks': HSnationalDSM.s,
             'international_HS_stocks': HSinternationalDSM.s,
             'generic_HS_stocks': HSgenericDSM.s}
dfHSstocks = pd.DataFrame(HS_stocks, columns=['years', 'regional_HS_stocks', 'national_HS_stocks', 'international_HS_stocks', 'generic_HS_stocks'])

aluminium_total = {'years': timespan,
             'regional_EHS_HS': alu_inflow_reg,
             'national_EHS_HS': alu_inflow_nat,
             'international_EHS_HS': alu_inflow_int,
             'generic_EHS_HS': alu_inflow_gen,
             'outflows_EHS_HS': alu_outflow}
dfaluminium_total = pd.DataFrame(aluminium_total, columns=['years','regional_EHS_HS', 'national_EHS_HS', 'international_EHS_HS', 'generic_EHS_HS', 'outflows_EHS_HS'])

steel_total = {'years': timespan,
         'regional_EHS_HS': steel_inflow_reg,
             'national_EHS_HS': steel_inflow_nat,
             'international_EHS_HS': steel_inflow_int,
             'generic_EHS_HS': steel_inflow_gen,
             'outflows_EHS_HS': steel_outflow}
dfsteel_total = pd.DataFrame(steel_total, columns=['years', 'regional_EHS_HS', 'national_EHS_HS', 'international_EHS_HS', 'generic_EHS_HS', 'outflows_EHS_HS'])

#writing the dataframes to excel
with pd.ExcelWriter('EHS_HS_overhead_result_data.xlsx') as writer:
    dfaluminium_total.to_excel(writer, sheet_name='total_aluminium', index=False)
    dfsteel_total.to_excel(writer, sheet_name='EHS_HS_steel', index=False)
    dfEHSstocks.to_excel(writer, sheet_name='EHS_stocks', index=False)
    dfHSstocks.to_excel(writer, sheet_name='HS_stocks', index=False)
    



