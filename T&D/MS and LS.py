# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:54:50 2020

@author: Judith
"""

# Import libraries
import numpy as np
from dynamic_stock_model_odym import DynamicStockModel #imports the Open Dynamic Material Systems Model (ODYM)
import pandas as pd




#%%
#storing the path to the data
data_path = 'Datasheet_MS_LS.xlsx'

#reading the excel datafile and defining the historic stock
dfhistoric = pd.read_excel (data_path, sheet_name='historic')
dffuture = pd.read_excel (data_path, sheet_name='future_stocks')
dfhistoricmaterial = pd.read_excel (data_path, sheet_name='historic_inflows') 
dffuturematerial = pd.read_excel (data_path, sheet_name='inflows_material_separated')
mat_intens = pd.read_excel (data_path, sheet_name='material_intensities')





#%% the total MS stocks
historicstockMS = dfhistoric['stock MS [km]'].tolist()

#defining stock of the regional scenario
regionalstockMS = historicstockMS.copy()
regfstockMS = dffuture['Regional stock MS'].tolist()
for i in regfstockMS:
    regionalstockMS.append(i)

#defining stock of the national scenario
nationalstockMS = historicstockMS.copy()
natfstockMS = dffuture['National stock MS'].tolist()
for i in natfstockMS:
    nationalstockMS.append(i)
    
#defining stock of the international scenario
internationalstockMS = historicstockMS.copy()
intfstockMS = dffuture['International stock MS'].tolist()
for i in intfstockMS:
    internationalstockMS.append(i)

#defining stock of the generic scenario
genericstockMS = historicstockMS.copy()
genfstockMS = dffuture['Generic stock MS'].tolist()
for i in genfstockMS:
    genericstockMS.append(i)




#%% the total LS stocks
historicstockLS = dfhistoric['stock LS [km]'].tolist()

#defining stock of the regional scenario
regionalstockLS = historicstockLS.copy()
regfstockLS = dffuture['Regional stock LS'].tolist()
for i in regfstockLS:
    regionalstockLS.append(i)

#defining stock of the national scenario
nationalstockLS = historicstockLS.copy()
natfstockLS = dffuture['National stock LS'].tolist()
for i in natfstockLS:
    nationalstockLS.append(i)
    
#defining stock of the international scenario
internationalstockLS = historicstockLS.copy()
intfstockLS = dffuture['International stock LS'].tolist()
for i in intfstockLS:
    internationalstockLS.append(i)

#defining stock of the generic scenario
genericstockLS = historicstockLS.copy()
genfstockLS = dffuture['Generic stock LS'].tolist()
for i in genfstockLS:
    genericstockLS.append(i)




#%% defining other needed variables
    
#lifetime distribution for the dynamic stock models    
lifetime_distribution = {'Type': 'Normal', 'Mean': np.array([50]), 'StdDev': np.array([8])}

#the timespan of the model
timespan = np.arange(1933, 2051, 1)

#the timespan for future flows, used for graphs
future_timespan = np.arange(2000, 2051, 1)  

#hibernation percentage
hibernation_percentage = 0.75
hibernation_percentage_SA_1 = 0.65
hibernation_percentage_SA_2 = 0.85




#%% calculating the total DSMs for all four scenarios

#calculating regional dynamic stock model
MSregionalDSM = DynamicStockModel(t = timespan, s = regionalstockMS, lt = lifetime_distribution)

S_C_regMS, O_C_regMS, I_regMS = MSregionalDSM.compute_stock_driven_model()
O_regMS = MSregionalDSM.compute_outflow_total()
DS_regMS = MSregionalDSM.compute_stock_change()
Bal_regMS = MSregionalDSM.check_stock_balance()

#calculating national dynamic stock model
MSnationalDSM = DynamicStockModel(t = timespan, s = nationalstockMS, lt = lifetime_distribution)

S_C_natMS, O_C_natMS, I_natMS = MSnationalDSM.compute_stock_driven_model()
O_natMS = MSnationalDSM.compute_outflow_total()
DS_natMS = MSnationalDSM.compute_stock_change()
Bal_natM = MSnationalDSM.check_stock_balance()

#calculating international dynamic stock model
MSinternationalDSM = DynamicStockModel(t = timespan, s = internationalstockMS, lt = lifetime_distribution)

S_C_intMS, O_C_intMS, I_intMS = MSinternationalDSM.compute_stock_driven_model()
O_intMS = MSinternationalDSM.compute_outflow_total()
DS_intMS = MSinternationalDSM.compute_stock_change()
Bal_intMS = MSinternationalDSM.check_stock_balance()

#calculating generic dynamic stock model
MSgenericDSM = DynamicStockModel(t = timespan, s = genericstockMS, 
                                 lt = lifetime_distribution)

S_C_genMS, O_C_genMS, I_genMS = MSgenericDSM.compute_stock_driven_model()
O_genMS = MSgenericDSM.compute_outflow_total()
DS_genMS = MSgenericDSM.compute_stock_change()
Bal_genMS = MSgenericDSM.check_stock_balance()





#%% calculating the total DSMs for all four scenarios

#calculating regional dynamic stock model
LSregionalDSM = DynamicStockModel(t = timespan, s = regionalstockLS, 
                                  lt = lifetime_distribution)

S_C_regLS, O_C_regLS, I_regLS = LSregionalDSM.compute_stock_driven_model()
O_regLS = LSregionalDSM.compute_outflow_total()
DS_regLS = LSregionalDSM.compute_stock_change()
Bal_regLS = LSregionalDSM.check_stock_balance()

#calculating national dynamic stock model
LSnationalDSM = DynamicStockModel(t = timespan, s = nationalstockLS, lt = lifetime_distribution)

S_C_natLS, O_C_natLS, I_natL = LSnationalDSM.compute_stock_driven_model()
O_natLS = LSnationalDSM.compute_outflow_total()
DS_natLS = LSnationalDSM.compute_stock_change()
Bal_natLS = LSnationalDSM.check_stock_balance()

#calculating international dynamic stock model
LSinternationalDSM = DynamicStockModel(t = timespan, s = internationalstockLS, 
                                       lt = lifetime_distribution)

S_C_intLS, O_C_intLS, I_intLS = LSinternationalDSM.compute_stock_driven_model()
O_intLS = LSinternationalDSM.compute_outflow_total()
DS_intLS = LSinternationalDSM.compute_stock_change()
Bal_intLS = LSinternationalDSM.check_stock_balance()

#calculating generic dynamic stock model
LSgenericDSM = DynamicStockModel(t = timespan, s = genericstockLS, 
                                 lt = lifetime_distribution)

S_C_genLS, O_C_genLS, I_genLS = LSgenericDSM.compute_stock_driven_model()
O_genLS = LSgenericDSM.compute_outflow_total()
DS_genLS = LSgenericDSM.compute_stock_change()
Bal_genLS = LSgenericDSM.check_stock_balance()




#%% material separated inflows

#MS
expansion_until_1970_MS = dfhistoricmaterial['1933-1970 inflow MS'].tolist()
expansion_until_2009_MS = dfhistoricmaterial['1970-2009 inflow MS'].tolist()

regional_expansion_2050_MS = dffuturematerial['Regional inflow MS'].tolist()
national_expansion_2050_MS = dffuturematerial['National inflow MS'].tolist()
international_expansion_2050_MS = dffuturematerial['International inflow MS'].tolist()
generic_expansion_2050_MS = dffuturematerial['Generic inflow MS'].tolist()


#LS
expansion_until_1970_LS = dfhistoricmaterial['1933-1970 inflow LS'].tolist()
expansion_until_2009_LS = dfhistoricmaterial['1970-2009 inflow LS'].tolist()

regional_expansion_2050_LS = dffuturematerial['Regional inflow LS'].tolist()
national_expansion_2050_LS = dffuturematerial['National inflow LS'].tolist()
international_expansion_2050_LS = dffuturematerial['International inflow LS'].tolist()
generic_expansion_2050_LS = dffuturematerial['Generic inflow LS'].tolist()





#%% calculating the MS DSM material sorted for the regional scenario (periods 1933-1970 and 1970-2019 are the same for each scenario)

#1933-1970
MS_DSM1970 = DynamicStockModel(t = timespan, i = expansion_until_1970_MS, 
                               lt = lifetime_distribution)

Stock_by_cohort_1970_MS = MS_DSM1970.compute_s_c_inflow_driven()
S_1970_MS   = MS_DSM1970.compute_stock_total()
O_C_1970_MS = MS_DSM1970.compute_o_c_from_s_c()
O_1970_MS   = MS_DSM1970.compute_outflow_total()
DS_1970_MS  = MS_DSM1970.compute_stock_change()

#calculating the outflow between 1970 and 2019
outflow_1970_2009_MS = []

for i in range(118):
    if i < 37:
        outflow_1970_2009_MS.append(0)
    if 37 <= i < 77:
        outflow_1970_2009_MS.append(MS_DSM1970.o[i])
    if 77 <= i < 118:
        outflow_1970_2009_MS.append(0)
        


#1970-2019
inflow_until_2009_MS = [expansion_until_2009_MS[i]+outflow_1970_2009_MS[i] for i in range(len(expansion_until_2009_MS))]

#1970-2009
MS_DSM2009 = DynamicStockModel(t = timespan, i = (inflow_until_2009_MS), 
                               lt = lifetime_distribution)

Stock_by_cohort_2009_MS = MS_DSM2009.compute_s_c_inflow_driven()
S_2009_MS   = MS_DSM2009.compute_stock_total()
O_C_2009_MS = MS_DSM2009.compute_o_c_from_s_c()
O_2009_MS   = MS_DSM2009.compute_outflow_total()
DS_2009_MS  = MS_DSM2009.compute_stock_change()

#calculating the outflow between 2019 and 2050
outflow_2009_2050_MS = []

for i in range(118):
    if i < 77:
        outflow_2009_2050_MS.append(0)
    if 77 <= i < 118:
        outflow_2009_2050_MS.append(MS_DSM2009.o[i]+outflow_1970_2009_MS[i])





#%% calculating the LS DSM material sorted 
        
#1933-1970
LS_DSM1970 = DynamicStockModel(t = timespan, i = expansion_until_1970_LS, 
                               lt = lifetime_distribution)

Stock_by_cohort_1970_LS = LS_DSM1970.compute_s_c_inflow_driven()
S_1970_LS   = LS_DSM1970.compute_stock_total()
O_C_1970_LS = LS_DSM1970.compute_o_c_from_s_c()
O_1970_LS   = LS_DSM1970.compute_outflow_total()
DS_1970_LS  = LS_DSM1970.compute_stock_change()

#calculating the outflow between 1970 and 2019
outflow_1970_2009_LS = []

for i in range(118):
    if i < 37:
        outflow_1970_2009_LS.append(0)
    if 37 <= i < 77:
        outflow_1970_2009_LS.append(LS_DSM1970.o[i])
    if 77 <= i < 118:
        outflow_1970_2009_LS.append(0)
        

#1970-2019
inflow_until_2009_LS = [expansion_until_2009_LS[i]+outflow_1970_2009_LS[i] for i in range(len(expansion_until_2009_LS))]

#1970-2019
LS_DSM2009 = DynamicStockModel(t = timespan, i = (inflow_until_2009_LS), 
                               lt = lifetime_distribution)

Stock_by_cohort_2009_LS = LS_DSM2009.compute_s_c_inflow_driven()
S_2009_LS   = LS_DSM2009.compute_stock_total()
O_C_2009_LS = LS_DSM2009.compute_o_c_from_s_c()
O_2009_LS   = LS_DSM2009.compute_outflow_total()
DS_2009_LS  = LS_DSM2009.compute_stock_change()

#calculating the outflow between 2019 and 2050
outflow_2009_2050_LS = []

for i in range(118):
    if i < 77:
        outflow_2009_2050_LS.append(0)
    if 77 <= i < 118:
        outflow_2009_2050_LS.append(LS_DSM2009.o[i]+outflow_1970_2009_LS[i])





#%% the flows of the 2019-2050 stock MS

# regional
inflow_regional_MS = [regional_expansion_2050_MS[i]+outflow_2009_2050_MS[i] for i in range(len(regional_expansion_2050_MS))]

MSregionalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_regional_MS), 
                                      lt = lifetime_distribution)

Stock_by_cohort_reg2050_MS = MSregionalDSM2050.compute_s_c_inflow_driven()
S_reg2050_MS   = MSregionalDSM2050.compute_stock_total()
O_C_reg2050_MS = MSregionalDSM2050.compute_o_c_from_s_c()
O_reg2050_MS   = MSregionalDSM2050.compute_outflow_total()
DS_reg2050_MS  = MSregionalDSM2050.compute_stock_change()


# national
inflow_national_MS = [national_expansion_2050_MS[i]+outflow_2009_2050_MS[i] for i in range(len(national_expansion_2050_MS))]

MSnationalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_national_MS), 
                                      lt = lifetime_distribution)

Stock_by_cohort_nat2050_MS = MSnationalDSM2050.compute_s_c_inflow_driven()
S_nat2050_MS   = MSnationalDSM2050.compute_stock_total()
O_C_nat2050_MS = MSnationalDSM2050.compute_o_c_from_s_c()
O_nat2050_MS   = MSnationalDSM2050.compute_outflow_total()
DS_nat2050_MS  = MSnationalDSM2050.compute_stock_change()


# international
inflow_international_MS = [international_expansion_2050_MS[i]+outflow_2009_2050_MS[i] for i in range(len(international_expansion_2050_MS))]
#2019-2050
MSinternationalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_international_MS), 
                                           lt = lifetime_distribution)

Stock_by_cohort_int2050_MS = MSinternationalDSM2050.compute_s_c_inflow_driven()
S_int2050_MS   = MSinternationalDSM2050.compute_stock_total()
O_C_int2050_MS = MSinternationalDSM2050.compute_o_c_from_s_c()
O_int2050_MS   = MSinternationalDSM2050.compute_outflow_total()
DS_int2050_MS  = MSinternationalDSM2050.compute_stock_change()


# generic
inflow_generic_MS = [generic_expansion_2050_MS[i]+outflow_2009_2050_MS[i] for i in range(len(generic_expansion_2050_MS))]
#2019-2050
MSgenericDSM2050 = DynamicStockModel(t = timespan, i = (inflow_generic_MS), 
                                     lt = lifetime_distribution)

Stock_by_cohort_gen2050_MS = MSgenericDSM2050.compute_s_c_inflow_driven()
S_gen2050_MS   = MSgenericDSM2050.compute_stock_total()
O_C_gen2050_MS = MSgenericDSM2050.compute_o_c_from_s_c()
O_gen2050_MS   = MSgenericDSM2050.compute_outflow_total()
DS_gen2050_MS  = MSgenericDSM2050.compute_stock_change()





#%% the flows of the 2019-2050 stock LS
        
# regional
inflow_regional_LS = [regional_expansion_2050_LS[i]+outflow_2009_2050_LS[i] for i in range(len(regional_expansion_2050_LS))]

LSregionalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_regional_LS), 
                                      lt = lifetime_distribution)

Stock_by_cohort_reg2050_LS = LSregionalDSM2050.compute_s_c_inflow_driven()
S_reg2050_LS   = LSregionalDSM2050.compute_stock_total()
O_C_reg2050_LS = LSregionalDSM2050.compute_o_c_from_s_c()
O_reg2050_LS   = LSregionalDSM2050.compute_outflow_total()
DS_reg2050_LS  = LSregionalDSM2050.compute_stock_change()


# national
inflow_national_LS = [national_expansion_2050_LS[i]+outflow_2009_2050_LS[i] for i in range(len(national_expansion_2050_LS))]

LSnationalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_national_LS), 
                                      lt = lifetime_distribution)

Stock_by_cohort_nat2050_LS = LSnationalDSM2050.compute_s_c_inflow_driven()
S_nat2050_LS   = LSnationalDSM2050.compute_stock_total()
O_C_nat2050_LS = LSnationalDSM2050.compute_o_c_from_s_c()
O_nat2050_LS   = LSnationalDSM2050.compute_outflow_total()
DS_nat2050_LS  = LSnationalDSM2050.compute_stock_change()


# international 
inflow_international_LS = [international_expansion_2050_LS[i]+outflow_2009_2050_LS[i] for i in range(len(international_expansion_2050_LS))]

LSinternationalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_international_LS), 
                                           lt = lifetime_distribution)

Stock_by_cohort_int2050_LS = LSinternationalDSM2050.compute_s_c_inflow_driven()
S_int2050_LS   = LSinternationalDSM2050.compute_stock_total()
O_C_int2050_LS = LSinternationalDSM2050.compute_o_c_from_s_c()
O_int2050_LS   = LSinternationalDSM2050.compute_outflow_total()
DS_int2050_LS  = LSinternationalDSM2050.compute_stock_change()


# generic
inflow_generic_LS = [generic_expansion_2050_LS[i]+outflow_2009_2050_LS[i] for i in range(len(generic_expansion_2050_LS))]
#2019-2050
LSgenericDSM2050 = DynamicStockModel(t = timespan, i = (inflow_generic_LS), 
                                     lt = lifetime_distribution)

Stock_by_cohort_gen2050_LS = LSgenericDSM2050.compute_s_c_inflow_driven()
S_gen2050_LS   = LSgenericDSM2050.compute_stock_total()
O_C_gen2050_LS = LSgenericDSM2050.compute_o_c_from_s_c()
O_gen2050_LS   = LSgenericDSM2050.compute_outflow_total()
DS_gen2050_LS  = LSgenericDSM2050.compute_stock_change()




#%% hibernating stocks MS

# calculating hibernating MS stock from the 1933-1970 period
inflow_rh1970_MS=MS_DSM1970.o.copy()*hibernation_percentage

new1970_MS = []
hibernating_stock1970_MS = []

for i in range(len(inflow_rh1970_MS)):    
    new1970_MS.append(inflow_rh1970_MS[i])
    hibernating_stock1970_MS.append(sum(new1970_MS))
    

# calculating hibernating MS stock from the 1970-2009 period
inflow_rh2009_MS=MS_DSM2009.o.copy()*hibernation_percentage

new2009_MS = []
hibernating_stock2009_MS = []

for i in range(len(inflow_rh2009_MS)):    
    new2009_MS.append(inflow_rh2009_MS[i])
    hibernating_stock2009_MS.append(sum(new2009_MS))

#calculating hibernating MS stock from 2009-2050
inflow_rh2050_MS=MSregionalDSM2050.o.copy()*hibernation_percentage

new2050_MS = []
hibernating_stock2050_MS = []

for i in range(len(inflow_rh2050_MS)):
    new2050_MS.append(inflow_rh2009_MS[i])
    hibernating_stock2050_MS.append(sum(new2050_MS))


# total hibernating stock
total_hibernating_stock_MS = [hibernating_stock1970_MS[i] + hibernating_stock2009_MS[i] + hibernating_stock2050_MS[i] for i in range(len(hibernating_stock1970_MS))] 

#calculating the recovered MS cables
recovered1970_MS = MS_DSM1970.o.copy() - inflow_rh1970_MS.copy()
recovered2009_MS = MS_DSM2009.o.copy() - inflow_rh2009_MS.copy()
recovered2050_MS = MSregionalDSM2050.o.copy() - inflow_rh2050_MS.copy()

total_recovered_cables_MS = [recovered1970_MS[i] + recovered2009_MS[i] + recovered2050_MS[i] for i in range(len(recovered1970_MS))]




#%% hibernating stocks MS sensitivity analysis 1

# calculating hibernating MS stock from the 1933-1970 period
inflow_rh1970_MS_SA_1=MS_DSM1970.o.copy()*hibernation_percentage_SA_1

new1970_MS_SA_1 = []
hibernating_stock1970_MS_SA_1 = []

for i in range(len(inflow_rh1970_MS_SA_1)):    
    new1970_MS_SA_1.append(inflow_rh1970_MS_SA_1[i])
    hibernating_stock1970_MS_SA_1.append(sum(new1970_MS_SA_1))
    

# calculating hibernating MS stock from the 1970-2009 period
inflow_rh2009_MS_SA_1=MS_DSM2009.o.copy()*hibernation_percentage_SA_1

new2009_MS_SA_1 = []
hibernating_stock2009_MS_SA_1 = []

for i in range(len(inflow_rh2009_MS_SA_1)):    
    new2009_MS_SA_1.append(inflow_rh2009_MS_SA_1[i])
    hibernating_stock2009_MS_SA_1.append(sum(new2009_MS_SA_1))

#calculating hibernating MS stock from 2009-2050
inflow_rh2050_MS_SA_1=MSregionalDSM2050.o.copy()*hibernation_percentage_SA_1

new2050_MS_SA_1 = []
hibernating_stock2050_MS_SA_1 = []

for i in range(len(inflow_rh2050_MS_SA_1)):
    new2050_MS_SA_1.append(inflow_rh2009_MS_SA_1[i])
    hibernating_stock2050_MS_SA_1.append(sum(new2050_MS_SA_1))


# total hibernating stock
total_hibernating_stock_MS_SA_1 = [hibernating_stock1970_MS_SA_1[i] + hibernating_stock2009_MS_SA_1[i] + hibernating_stock2050_MS_SA_1[i] for i in range(len(timespan))] 

#calculating the recovered MS cables
recovered1970_MS_SA_1 = MS_DSM1970.o.copy() - inflow_rh1970_MS_SA_1.copy()
recovered2009_MS_SA_1 = MS_DSM2009.o.copy() - inflow_rh2009_MS_SA_1.copy()
recovered2050_MS_SA_1 = MSregionalDSM2050.o.copy() - inflow_rh2050_MS_SA_1.copy()

total_recovered_cables_MS_SA_1 = [recovered1970_MS_SA_1[i] + recovered2009_MS_SA_1[i] + recovered2050_MS_SA_1[i] for i in range(len(timespan))]





#%% hibernating stocks MS sensitivity analysis 2

# calculating hibernating MS stock from the 1933-1970 period
inflow_rh1970_MS_SA_2=MS_DSM1970.o.copy()*hibernation_percentage_SA_2

new1970_MS_SA_2 = []
hibernating_stock1970_MS_SA_2 = []

for i in range(len(inflow_rh1970_MS_SA_2)):    
    new1970_MS_SA_2.append(inflow_rh1970_MS_SA_2[i])
    hibernating_stock1970_MS_SA_2.append(sum(new1970_MS_SA_2))
    

# calculating hibernating MS stock from the 1970-2009 period
inflow_rh2009_MS_SA_2=MS_DSM2009.o.copy()*hibernation_percentage_SA_2

new2009_MS_SA_2 = []
hibernating_stock2009_MS_SA_2 = []

for i in range(len(inflow_rh2009_MS_SA_2)):    
    new2009_MS_SA_2.append(inflow_rh2009_MS_SA_2[i])
    hibernating_stock2009_MS_SA_2.append(sum(new2009_MS_SA_2))

#calculating hibernating MS stock from 2009-2050
inflow_rh2050_MS_SA_2=MSregionalDSM2050.o.copy()*hibernation_percentage_SA_2

new2050_MS_SA_2 = []
hibernating_stock2050_MS_SA_2 = []

for i in range(len(inflow_rh2050_MS_SA_2)):
    new2050_MS_SA_2.append(inflow_rh2009_MS_SA_2[i])
    hibernating_stock2050_MS_SA_2.append(sum(new2050_MS_SA_2))


# total hibernating stock
total_hibernating_stock_MS_SA_2 = [hibernating_stock1970_MS_SA_2[i] + hibernating_stock2009_MS_SA_2[i] + hibernating_stock2050_MS_SA_2[i] for i in range(len(timespan))] 

#calculating the recovered MS cables
recovered1970_MS_SA_2 = MS_DSM1970.o.copy() - inflow_rh1970_MS_SA_2.copy()
recovered2009_MS_SA_2 = MS_DSM2009.o.copy() - inflow_rh2009_MS_SA_2.copy()
recovered2050_MS_SA_2 = MSregionalDSM2050.o.copy() - inflow_rh2050_MS_SA_2.copy()

total_recovered_cables_MS_SA_2 = [recovered1970_MS_SA_2[i] + recovered2009_MS_SA_2[i] + recovered2050_MS_SA_2[i] for i in range(len(timespan))]




#%% hibernating stocks LS

# calculating hibernating LS stock from the 1933-1970 period
inflow_rh1970_LS=LS_DSM1970.o.copy()*hibernation_percentage

new1970_LS = []
hibernating_stock1970_LS = []

for i in range(len(inflow_rh1970_LS)):    
    new1970_LS.append(inflow_rh1970_LS[i])
    hibernating_stock1970_LS.append(sum(new1970_LS))


# calculating hibernating LS stock from the 1970-2019 period
inflow_rh2009_LS=LS_DSM2009.o.copy()*hibernation_percentage

new2009_LS = []
hibernating_stock2009_LS = []

for i in range(len(inflow_rh2009_LS)):    
    new2009_LS.append(inflow_rh2009_LS[i])
    hibernating_stock2009_LS.append(sum(new2009_LS))
    
#calculating hibernating MS stock from 2009-2050
inflow_rh2050_LS=LSregionalDSM2050.o.copy()*hibernation_percentage

new2050_LS = []
hibernating_stock2050_LS = []

for i in range(len(inflow_rh2050_LS)):
    new2050_LS.append(inflow_rh2009_LS[i])
    hibernating_stock2050_LS.append(sum(new2050_LS))
    
#total hibernating stock 
total_hibernating_stock_LS = [hibernating_stock1970_LS[i] + hibernating_stock2009_LS[i] + hibernating_stock2050_LS[i] for i in range (len(hibernating_stock1970_LS))]    

#calculating the recovered LS cables
recovered1970_LS = LS_DSM1970.o.copy() - inflow_rh1970_LS.copy()
recovered2009_LS = LS_DSM2009.o.copy() - inflow_rh2009_LS.copy()
recovered2050_LS = LSregionalDSM2050.o.copy() - inflow_rh2050_LS

total_recovered_cables_LS = [recovered1970_LS[i] + recovered2009_LS[i] + recovered2050_LS[i] for i in range(len(recovered1970_LS))]



#%% hibernating stocks LS sensitivity analysis 1

# calculating hibernating LS stock from the 1933-1970 period
inflow_rh1970_LS_SA_1=LS_DSM1970.o.copy()*hibernation_percentage_SA_1

new1970_LS_SA_1 = []
hibernating_stock1970_LS_SA_1 = []

for i in range(len(inflow_rh1970_LS_SA_1)):    
    new1970_LS_SA_1.append(inflow_rh1970_LS_SA_1[i])
    hibernating_stock1970_LS_SA_1.append(sum(new1970_LS_SA_1))


# calculating hibernating LS stock from the 1970-2019 period
inflow_rh2009_LS_SA_1=LS_DSM2009.o.copy()*hibernation_percentage_SA_1

new2009_LS_SA_1 = []
hibernating_stock2009_LS_SA_1 = []

for i in range(len(inflow_rh2009_LS_SA_1)):    
    new2009_LS_SA_1.append(inflow_rh2009_LS_SA_1[i])
    hibernating_stock2009_LS_SA_1.append(sum(new2009_LS_SA_1))
    
#calculating hibernating MS stock from 2009-2050
inflow_rh2050_LS_SA_1=LSregionalDSM2050.o.copy()*hibernation_percentage_SA_1

new2050_LS_SA_1 = []
hibernating_stock2050_LS_SA_1 = []

for i in range(len(inflow_rh2050_LS_SA_1)):
    new2050_LS_SA_1.append(inflow_rh2009_LS_SA_1[i])
    hibernating_stock2050_LS_SA_1.append(sum(new2050_LS_SA_1))
    
#total hibernating stock 
total_hibernating_stock_LS_SA_1 = [hibernating_stock1970_LS_SA_1[i] + hibernating_stock2009_LS_SA_1[i] + hibernating_stock2050_LS_SA_1[i] for i in range (len(timespan))]    

#calculating the recovered LS cables
recovered1970_LS_SA_1 = LS_DSM1970.o.copy() - inflow_rh1970_LS_SA_1.copy()
recovered2009_LS_SA_1 = LS_DSM2009.o.copy() - inflow_rh2009_LS_SA_1.copy()
recovered2050_LS_SA_1 = LSregionalDSM2050.o.copy() - inflow_rh2050_LS_SA_1

total_recovered_cables_LS_SA_1 = [recovered1970_LS_SA_1[i] + recovered2009_LS_SA_1[i] + recovered2050_LS_SA_1[i] for i in range(len(timespan))]



#%% hibernating stocks LS sensitivity analysis 2

# calculating hibernating LS stock from the 1933-1970 period
inflow_rh1970_LS_SA_2=LS_DSM1970.o.copy()*hibernation_percentage_SA_2

new1970_LS_SA_2 = []
hibernating_stock1970_LS_SA_2 = []

for i in range(len(inflow_rh1970_LS_SA_2)):    
    new1970_LS_SA_2.append(inflow_rh1970_LS_SA_2[i])
    hibernating_stock1970_LS_SA_2.append(sum(new1970_LS_SA_2))


# calculating hibernating LS stock from the 1970-2019 period
inflow_rh2009_LS_SA_2=LS_DSM2009.o.copy()*hibernation_percentage_SA_2

new2009_LS_SA_2 = []
hibernating_stock2009_LS_SA_2 = []

for i in range(len(inflow_rh2009_LS_SA_2)):    
    new2009_LS_SA_2.append(inflow_rh2009_LS_SA_2[i])
    hibernating_stock2009_LS_SA_2.append(sum(new2009_LS_SA_2))
    
#calculating hibernating MS stock from 2009-2050
inflow_rh2050_LS_SA_2=LSregionalDSM2050.o.copy()*hibernation_percentage_SA_2

new2050_LS_SA_2 = []
hibernating_stock2050_LS_SA_2 = []

for i in range(len(inflow_rh2050_LS_SA_2)):
    new2050_LS_SA_2.append(inflow_rh2009_LS_SA_2[i])
    hibernating_stock2050_LS_SA_2.append(sum(new2050_LS_SA_2))
    
#total hibernating stock 
total_hibernating_stock_LS_SA_2 = [hibernating_stock1970_LS_SA_2[i] + hibernating_stock2009_LS_SA_2[i] + hibernating_stock2050_LS_SA_2[i] for i in range (len(timespan))]    

#calculating the recovered LS cables
recovered1970_LS_SA_2 = LS_DSM1970.o.copy() - inflow_rh1970_LS_SA_2.copy()
recovered2009_LS_SA_2 = LS_DSM2009.o.copy() - inflow_rh2009_LS_SA_2.copy()
recovered2050_LS_SA_2 = LSregionalDSM2050.o.copy() - inflow_rh2050_LS_SA_2.copy()

total_recovered_cables_LS_SA_2 = [recovered1970_LS_SA_2[i] + recovered2009_LS_SA_2[i] + recovered2050_LS_SA_2[i] for i in range(len(timespan))]



#%% material percentages and intensities for MS grid

#proportion aluminium and copper in the period 1933-1970
aluminium_share_1970_MS = 0.346
copper_share_1970_MS = 0.654

#proportion aluminium and copper in the period 1970-2009
aluminium_share_2009_MS = 0.928
copper_share_2009_MS = 0.072

#proportions aluminium and copper in the period 2009-2050
aluminium_share_2050_MS = 1
copper_share_2050_MS = 0

#the material intensities in ton/km 
copper_intensity_MS = mat_intens.loc[0, 'Copper']
aluminium_intensity_MS = mat_intens.loc[0, 'Aluminium']


#%% material percentages and intensities for LS grid

#proportion aluminium and copper in the period 1933-1970
aluminium_share_1970_LS = 0.04
copper_share_1970_LS = 0.96

#proportion aluminium and copper in the period 1970-2009
aluminium_share_2009_LS = 0.72
copper_share_2009_LS = 0.28

#proportions aluminium and copper in the period 2009-2050
aluminium_share_2050_LS = 1
copper_share_2050_LS = 0

#the material intensities in ton/km 
copper_intensity_LS = mat_intens.loc[1, 'Copper']
aluminium_intensity_LS = mat_intens.loc[1, 'Aluminium']




#%% material flows of the MS grid
total_aluminium_inflows_regional_MS = [(MS_DSM1970.i[i] * aluminium_share_1970_MS * aluminium_intensity_MS) + (MS_DSM2009.i[i]*aluminium_share_2009_MS * aluminium_intensity_MS) + 
                                       (MSregionalDSM2050.i[i]*aluminium_share_2050_MS * aluminium_intensity_MS) for i in range(len(MS_DSM1970.i))]
total_aluminium_inflows_national_MS = [(MS_DSM1970.i[i] * aluminium_share_1970_MS * aluminium_intensity_MS) + (MS_DSM2009.i[i]*aluminium_share_2009_MS * aluminium_intensity_MS) + 
                                       (MSnationalDSM2050.i[i]*aluminium_share_2050_MS * aluminium_intensity_MS) for i in range(len(MS_DSM1970.i))]
total_aluminium_inflows_international_MS = [(MS_DSM1970.i[i] * aluminium_share_1970_MS * aluminium_intensity_MS) + (MS_DSM2009.i[i]*aluminium_share_2009_MS * aluminium_intensity_MS) + 
                                            (MSinternationalDSM2050.i[i]*aluminium_share_2050_MS * aluminium_intensity_MS) for i in range(len(MS_DSM1970.i))]
total_aluminium_inflows_generic_MS = [(MS_DSM1970.i[i] * aluminium_share_1970_MS * aluminium_intensity_MS) + (MS_DSM2009.i[i]*aluminium_share_2009_MS * aluminium_intensity_MS) + 
                                      (MSgenericDSM2050.i[i]*aluminium_share_2050_MS * aluminium_intensity_MS) for i in range(len(MS_DSM1970.i))]

total_copper_inflows_regional_MS = [(MS_DSM1970.i[i] * copper_share_1970_MS * copper_intensity_MS) + (MS_DSM2009.i[i]*copper_share_2009_MS * copper_intensity_MS) + 
                                    (MSregionalDSM2050.i[i]*copper_share_2050_MS * copper_intensity_MS) for i in range(len(MS_DSM1970.i))]
total_copper_inflows_national_MS = [(MS_DSM1970.i[i] * copper_share_1970_MS * copper_intensity_MS) + (MS_DSM2009.i[i]*copper_share_2009_MS * copper_intensity_MS) + 
                                    (MSnationalDSM2050.i[i]*copper_share_2050_MS * copper_intensity_MS) for i in range(len(MS_DSM1970.i))]
total_copper_inflows_international_MS = [(MS_DSM1970.i[i] * copper_share_1970_MS * copper_intensity_MS) + (MS_DSM2009.i[i]*copper_share_2009_MS * copper_intensity_MS) + 
                                         (MSinternationalDSM2050.i[i]*copper_share_2050_MS * copper_intensity_MS) for i in range(len(MS_DSM1970.i))]
total_copper_inflows_generic_MS = [(MS_DSM1970.i[i] * copper_share_1970_MS * copper_intensity_MS) + (MS_DSM2009.i[i]*copper_share_2009_MS * copper_intensity_MS) + 
                                   (MSgenericDSM2050.i[i]*copper_share_2050_MS * copper_intensity_MS) for i in range(len(MS_DSM1970.i))]

total_aluminium_outflow_MS = [(MS_DSM1970.o[i] * aluminium_share_1970_MS * aluminium_intensity_MS) + (MS_DSM2009.o[i]*aluminium_share_2009_MS * aluminium_intensity_MS) + 
                                       (MSregionalDSM2050.o[i]*aluminium_share_2050_MS * aluminium_intensity_MS) for i in range(len(MS_DSM1970.o))]
total_copper_outflow_MS = [(MS_DSM1970.o[i] * copper_share_1970_MS * copper_intensity_MS) + (MS_DSM2009.o[i]*copper_share_2009_MS * copper_intensity_MS) + 
                                    (MSregionalDSM2050.o[i]*copper_share_2050_MS * copper_intensity_MS) for i in range(len(MS_DSM1970.o))]

total_aluminium_recovered_MS = [(recovered1970_MS[i]*aluminium_share_1970_MS * aluminium_intensity_MS) + (recovered2009_MS[i]*aluminium_share_2009_MS * aluminium_intensity_MS) + 
                                (recovered2050_MS[i]*aluminium_share_2050_MS * aluminium_intensity_MS) for i in range(len(timespan))]
total_aluminium_recovered_MS_SA_1 = [(recovered1970_MS_SA_1[i]*aluminium_share_1970_MS * aluminium_intensity_MS) + (recovered2009_MS_SA_1[i]*aluminium_share_2009_MS * aluminium_intensity_MS) + 
                                (recovered2050_MS_SA_1[i]*aluminium_share_2050_MS * aluminium_intensity_MS) for i in range(len(timespan))]
total_aluminium_recovered_MS_SA_2 = [(recovered1970_MS_SA_2[i]*aluminium_share_1970_MS * aluminium_intensity_MS) + (recovered2009_MS_SA_2[i]*aluminium_share_2009_MS * aluminium_intensity_MS) + 
                                (recovered2050_MS_SA_2[i]*aluminium_share_2050_MS * aluminium_intensity_MS) for i in range(len(timespan))]

total_copper_recovered_MS = [(recovered1970_MS[i]*copper_share_1970_MS * copper_intensity_MS) + (recovered2009_MS[i]*copper_share_2009_MS * copper_intensity_MS) + 
                             (recovered2050_MS[i]*copper_share_2050_MS * copper_intensity_MS) for i in range(len(timespan))]
total_copper_recovered_MS_SA_1 = [(recovered1970_MS_SA_1[i]*copper_share_1970_MS * copper_intensity_MS) + (recovered2009_MS_SA_1[i]*copper_share_2009_MS * copper_intensity_MS) + 
                             (recovered2050_MS_SA_1[i]*copper_share_2050_MS * copper_intensity_MS) for i in range(len(timespan))]
total_copper_recovered_MS_SA_2 = [(recovered1970_MS_SA_2[i]*copper_share_1970_MS * copper_intensity_MS) + (recovered2009_MS_SA_2[i]*copper_share_2009_MS * copper_intensity_MS) + 
                             (recovered2050_MS_SA_2[i]*copper_share_2050_MS * copper_intensity_MS) for i in range(len(timespan))]





#%% material flows of the LS grid
total_aluminium_inflows_regional_LS = [(LS_DSM1970.i[i] * aluminium_share_1970_LS * aluminium_intensity_LS) + (LS_DSM2009.i[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + 
                                       (LSregionalDSM2050.i[i]*aluminium_share_2050_LS * aluminium_intensity_LS) for i in range(len(LS_DSM1970.i))]
total_aluminium_inflows_national_LS = [(LS_DSM1970.i[i] * aluminium_share_1970_LS * aluminium_intensity_LS) + (LS_DSM2009.i[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + 
                                       (LSnationalDSM2050.i[i]*aluminium_share_2050_LS * aluminium_intensity_LS) for i in range(len(LS_DSM1970.i))]
total_aluminium_inflows_international_LS = [(LS_DSM1970.i[i] * aluminium_share_1970_LS * aluminium_intensity_LS) + (LS_DSM2009.i[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + 
                                            (LSinternationalDSM2050.i[i]*aluminium_share_2050_LS * aluminium_intensity_LS) for i in range(len(LS_DSM1970.i))]
total_aluminium_inflows_generic_LS = [(LS_DSM1970.i[i] * aluminium_share_1970_LS * aluminium_intensity_LS) + (LS_DSM2009.i[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + 
                                      (LSgenericDSM2050.i[i]*aluminium_share_2050_LS * aluminium_intensity_LS) for i in range(len(LS_DSM1970.i))]

total_copper_inflows_regional_LS = [(LS_DSM1970.i[i] * copper_share_1970_LS * copper_intensity_LS) + (LS_DSM2009.i[i]*copper_share_2009_LS * copper_intensity_LS) + 
                                    (LSregionalDSM2050.i[i]*copper_share_2050_LS * copper_intensity_LS) for i in range(len(LS_DSM1970.i))]
total_copper_inflows_national_LS = [(LS_DSM1970.i[i] * copper_share_1970_LS * copper_intensity_LS) + (LS_DSM2009.i[i]*copper_share_2009_LS * copper_intensity_LS) + 
                                    (LSnationalDSM2050.i[i]*copper_share_2050_LS * copper_intensity_LS) for i in range(len(LS_DSM1970.i))]
total_copper_inflows_international_LS = [(LS_DSM1970.i[i] * copper_share_1970_LS * copper_intensity_LS) + (LS_DSM2009.i[i]*copper_share_2009_LS * copper_intensity_LS) + 
                                         (LSinternationalDSM2050.i[i]*copper_share_2050_LS * copper_intensity_LS) for i in range(len(LS_DSM1970.i))]
total_copper_inflows_generic_LS = [(LS_DSM1970.i[i] * copper_share_1970_LS * copper_intensity_LS) + (LS_DSM2009.i[i]*copper_share_2009_LS * copper_intensity_LS) + 
                                   (LSgenericDSM2050.i[i]*copper_share_2050_LS * copper_intensity_LS) for i in range(len(LS_DSM1970.i))]

total_aluminium_outflow_LS = [(LS_DSM1970.o[i] * aluminium_share_1970_LS * aluminium_intensity_LS) + (LS_DSM2009.o[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + 
                                       (LSregionalDSM2050.o[i]*aluminium_share_2050_LS * aluminium_intensity_LS) for i in range(len(LS_DSM1970.o))]
total_copper_outflow_LS = [(LS_DSM1970.o[i] * copper_share_1970_LS * copper_intensity_LS) + (LS_DSM2009.o[i]*copper_share_2009_LS * copper_intensity_LS) + 
                                    (LSregionalDSM2050.o[i]*copper_share_2050_LS * copper_intensity_LS) for i in range(len(LS_DSM1970.o))]

total_aluminium_recovered_LS = [(recovered1970_LS[i]*aluminium_share_1970_LS * aluminium_intensity_LS) + (recovered2009_LS[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + 
                                (recovered2050_LS[i]*aluminium_share_2050_LS * aluminium_intensity_LS) for i in range(len(timespan))]
total_aluminium_recovered_LS_SA_1 = [(recovered1970_LS_SA_1[i]*aluminium_share_1970_LS * aluminium_intensity_LS) + (recovered2009_LS_SA_1[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + 
                                (recovered2050_LS_SA_1[i]*aluminium_share_2050_LS * aluminium_intensity_LS) for i in range(len(timespan))]
total_aluminium_recovered_LS_SA_2 = [(recovered1970_LS_SA_2[i]*aluminium_share_1970_LS * aluminium_intensity_LS) + (recovered2009_LS_SA_2[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + 
                                (recovered2050_LS_SA_2[i]*aluminium_share_2050_LS * aluminium_intensity_LS) for i in range(len(timespan))]

total_copper_recovered_LS = [(recovered1970_LS[i]*copper_share_1970_LS * copper_intensity_LS) + (recovered2009_LS[i]*copper_share_2009_LS * copper_intensity_LS) + 
                             (recovered2009_LS[i]*copper_share_2009_LS * copper_intensity_LS) for i in range(len(timespan))]
total_copper_recovered_LS_SA_1 = [(recovered1970_LS_SA_1[i]*copper_share_1970_LS * copper_intensity_LS) + (recovered2009_LS_SA_1[i]*copper_share_2009_LS * copper_intensity_LS) + 
                             (recovered2009_LS_SA_1[i]*copper_share_2009_LS * copper_intensity_LS) for i in range(len(timespan))]
total_copper_recovered_LS_SA_2 = [(recovered1970_LS_SA_2[i]*copper_share_1970_LS) + (recovered2009_LS_SA_2[i]*copper_share_2009_LS * copper_intensity_LS) + 
                             (recovered2009_LS_SA_2[i]*copper_share_2009_LS * copper_intensity_LS) for i in range(len(timespan))]




#%% total material flows
total_aluminium_inflows_regional_MS_LS = [total_aluminium_inflows_regional_MS[i] + total_aluminium_inflows_regional_LS[i] for i in range(len(timespan))]
total_aluminium_inflows_national_MS_LS = [total_aluminium_inflows_national_MS[i] + total_aluminium_inflows_national_LS[i] for i in range(len(timespan))]
total_aluminium_inflows_international_MS_LS = [total_aluminium_inflows_international_MS[i] + total_aluminium_inflows_international_LS[i] for i in range(len(timespan))]
total_aluminium_inflows_generic_MS_LS = [total_aluminium_inflows_generic_MS[i] + total_aluminium_inflows_generic_LS[i] for i in range(len(timespan))]
        
total_copper_inflows_regional_MS_LS = [total_copper_inflows_regional_MS[i] + total_copper_inflows_regional_LS[i] for i in range(len(timespan))]
total_copper_inflows_national_MS_LS = [total_copper_inflows_national_MS[i] + total_copper_inflows_national_LS[i] for i in range(len(timespan))]
total_copper_inflows_international_MS_LS = [total_copper_inflows_international_MS[i] + total_copper_inflows_international_LS[i] for i in range(len(timespan))]
total_copper_inflows_generic_MS_LS = [total_copper_inflows_generic_MS[i] + total_copper_inflows_generic_LS[i] for i in range(len(timespan))]

total_aluminium_outflow_MS_LS = [total_aluminium_outflow_MS[i] + total_aluminium_outflow_LS[i] for i in range(len(timespan))]
total_copper_outflow_MS_LS = [total_copper_outflow_MS[i] + total_copper_outflow_LS[i] for i in range(len(timespan))]

total_aluminium_recovered_MS_LS = [total_aluminium_recovered_MS[i] + total_aluminium_recovered_LS[i] for i in range(len(timespan))]
total_aluminium_recovered_MS_LS_SA_1 = [total_aluminium_recovered_MS_SA_1[i] + total_aluminium_recovered_LS_SA_1[i] for i in range(len(timespan))]
total_aluminium_recovered_MS_LS_SA_2 = [total_aluminium_recovered_MS_SA_2[i] + total_aluminium_recovered_LS_SA_2[i] for i in range(len(timespan))]

total_copper_recovered_MS_LS = [total_copper_recovered_MS[i] + total_copper_recovered_LS[i] for i in range(len(timespan))]
total_copper_recovered_MS_LS_SA_1 = [total_copper_recovered_MS_SA_1[i] + total_copper_recovered_LS_SA_1[i] for i in range(len(timespan))]
total_copper_recovered_MS_LS_SA_2 = [total_copper_recovered_MS_SA_2[i] + total_copper_recovered_LS_SA_2[i] for i in range(len(timespan))]




#%% calculating the material hibernating stock

aluminium_hibernating_stock = [(hibernating_stock1970_MS[i]*aluminium_share_1970_MS * aluminium_intensity_MS) + (hibernating_stock2009_MS[i]*aluminium_share_2009_MS * aluminium_intensity_MS) +
                               (hibernating_stock2050_MS[i]*aluminium_share_2050_MS * aluminium_intensity_MS) + (hibernating_stock1970_LS[i]*aluminium_share_1970_LS * aluminium_intensity_LS) + 
                               (hibernating_stock2009_LS[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + (hibernating_stock2050_LS[i]*aluminium_share_2050_LS * aluminium_intensity_LS) 
                               for i in range(len(hibernating_stock1970_MS))]

aluminium_hibernating_stock_SA_1 = [(hibernating_stock1970_MS_SA_1[i]*aluminium_share_1970_MS * aluminium_intensity_MS) + (hibernating_stock2009_MS_SA_1[i]*aluminium_share_2009_MS * aluminium_intensity_MS) +
                               (hibernating_stock2050_MS_SA_1[i]*aluminium_share_2050_MS * aluminium_intensity_MS) + (hibernating_stock1970_LS_SA_1[i]*aluminium_share_1970_LS * aluminium_intensity_LS) + 
                               (hibernating_stock2009_LS_SA_1[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + (hibernating_stock2050_LS_SA_1[i]*aluminium_share_2050_LS * aluminium_intensity_LS) 
                               for i in range(len(hibernating_stock1970_MS))]

aluminium_hibernating_stock_SA_2 = [(hibernating_stock1970_MS_SA_2[i]*aluminium_share_1970_MS * aluminium_intensity_MS) + (hibernating_stock2009_MS_SA_2[i]*aluminium_share_2009_MS * aluminium_intensity_MS) +
                               (hibernating_stock2050_MS_SA_2[i]*aluminium_share_2050_MS * aluminium_intensity_MS) + (hibernating_stock1970_LS_SA_2[i]*aluminium_share_1970_LS * aluminium_intensity_LS) + 
                               (hibernating_stock2009_LS_SA_2[i]*aluminium_share_2009_LS * aluminium_intensity_LS) + (hibernating_stock2050_LS_SA_2[i]*aluminium_share_2050_LS * aluminium_intensity_LS) 
                               for i in range(len(hibernating_stock1970_MS))]


copper_hibernating_stock =[(hibernating_stock1970_MS[i]*copper_share_1970_MS * copper_intensity_MS) + (hibernating_stock2009_MS[i]*copper_share_2009_MS * copper_intensity_MS) + 
                           (hibernating_stock2050_MS[i]*copper_share_2050_MS * copper_intensity_MS) + (hibernating_stock1970_LS[i]*copper_share_1970_LS * copper_intensity_LS) + 
                           (hibernating_stock2009_LS[i]*copper_share_2009_LS * copper_intensity_LS) + (hibernating_stock2050_LS[i]*copper_share_2050_LS * copper_intensity_LS) 
                           for i in range(len(hibernating_stock1970_MS))]

copper_hibernating_stock_SA_1 =[(hibernating_stock1970_MS_SA_1[i]*copper_share_1970_MS * copper_intensity_MS) + (hibernating_stock2009_MS_SA_1[i]*copper_share_2009_MS * copper_intensity_MS) + 
                           (hibernating_stock2050_MS_SA_1[i]*copper_share_2050_MS * copper_intensity_MS) + (hibernating_stock1970_LS_SA_1[i]*copper_share_1970_LS * copper_intensity_LS) + 
                           (hibernating_stock2009_LS_SA_1[i]*copper_share_2009_LS * copper_intensity_LS) + (hibernating_stock2050_LS_SA_1[i]*copper_share_2050_LS * copper_intensity_LS) 
                           for i in range(len(hibernating_stock1970_MS))]

copper_hibernating_stock_SA_2 =[(hibernating_stock1970_MS_SA_2[i]*copper_share_1970_MS * copper_intensity_MS) + (hibernating_stock2009_MS_SA_2[i]*copper_share_2009_MS * copper_intensity_MS) + 
                           (hibernating_stock2050_MS_SA_2[i]*copper_share_2050_MS * copper_intensity_MS) + (hibernating_stock1970_LS_SA_2[i]*copper_share_1970_LS * copper_intensity_LS) + 
                           (hibernating_stock2009_LS_SA_2[i]*copper_share_2009_LS * copper_intensity_LS) + (hibernating_stock2050_LS_SA_2[i]*copper_share_2050_LS * copper_intensity_LS) 
                           for i in range(len(hibernating_stock1970_MS))]




#%% putting all data into excelsheet. Needed in order to combine the data of all different voltage levels.

#the timespan is the same for each scenario, so defining one variable for this
timespan = np.arange(1933, 2051, 1)

# creating dataframes to write to excel
MS_stocks = {'years': timespan,
             'regional_MS_stocks': MSregionalDSM.s,
             'national_MS_stocks': MSnationalDSM.s,
             'international_MS_stocks': MSinternationalDSM.s,
             'generic_MS_stocks': MSgenericDSM.s}
dfMSstocks = pd.DataFrame(MS_stocks, columns=['years', 'regional_MS_stocks', 'national_MS_stocks', 'international_MS_stocks', 'generic_MS_stocks'])


LS_stocks = {'years': timespan,
             'regional_LS_stocks': LSregionalDSM.s,
             'national_LS_stocks': LSnationalDSM.s,
             'international_LS_stocks': LSinternationalDSM.s,
             'generic_LS_stocks': LSgenericDSM.s}
dfLSstocks = pd.DataFrame(LS_stocks, columns=['years', 'regional_LS_stocks', 'national_LS_stocks', 'international_LS_stocks', 'generic_LS_stocks'])

aluminium = {'years': timespan,
             'regional_MS_LS': total_aluminium_inflows_regional_MS_LS,
             'national_MS_LS': total_aluminium_inflows_national_MS_LS,
             'international_MS_LS': total_aluminium_inflows_national_MS_LS,
             'generic_MS_LS': total_aluminium_inflows_national_MS_LS,
             'outflow_MS_LS': total_aluminium_outflow_MS_LS,
             'hibernating_stock_MS_LS': aluminium_hibernating_stock,
             'hibernating_stock_MS_LS_SA_1': aluminium_hibernating_stock_SA_1,
             'hibernating_stock_MS_LS_SA_2': aluminium_hibernating_stock_SA_2,
             'recovered_MS_LS': total_aluminium_recovered_MS_LS,
             'recovered_MS_LS_SA_1': total_aluminium_recovered_MS_LS_SA_1,
             'recovered_MS_LS_SA_2': total_aluminium_recovered_MS_LS_SA_2}
dfaluminium=pd.DataFrame(aluminium, columns=['years','regional_MS_LS', 'national_MS_LS', 'international_MS_LS', 'generic_MS_LS', 'outflow_MS_LS', 'hibernating_stock_MS_LS', 'hibernating_stock_MS_LS_SA_1', 'hibernating_stock_MS_LS_SA_2', 'recovered_MS_LS', 'recovered_MS_LS_SA_1', 'recovered_MS_LS_SA_2'])

copper = {'years': timespan,
          'regional_MS_LS': total_copper_inflows_regional_MS_LS,
          'national_MS_LS': total_copper_inflows_national_MS_LS,
          'international_MS_LS': total_copper_inflows_national_MS_LS,
          'generic_MS_LS': total_copper_inflows_national_MS_LS,
          'outflow_MS_LS': total_copper_outflow_MS_LS,
          'hibernating_stock_MS_LS': copper_hibernating_stock,
          'hibernating_stock_MS_LS_SA_1': copper_hibernating_stock_SA_1,
          'hibernating_stock_MS_LS_SA_2': copper_hibernating_stock_SA_2,
          'recovered_MS_LS': total_copper_recovered_MS_LS,
          'recovered_MS_LS_SA_1': total_copper_recovered_MS_LS_SA_1,
          'recovered_MS_LS_SA_2': total_copper_recovered_MS_LS_SA_2}
dfcopper=pd.DataFrame(copper, columns=['years', 'regional_MS_LS', 'national_MS_LS', 'international_MS_LS', 'generic_MS_LS', 'outflow_MS_LS', 'hibernating_stock_MS_LS', 'hibernating_stock_MS_LS_SA_1', 'hibernating_stock_MS_LS_SA_2', 'recovered_MS_LS', 'recovered_MS_LS_SA_1', 'recovered_MS_LS_SA_2'])


#writing the dataframes to excel
with pd.ExcelWriter('MS_LS_result_data.xlsx') as writer:
    dfaluminium.to_excel(writer, sheet_name='MS_LS_aluminium', index=False)
    dfcopper.to_excel(writer, sheet_name='MS_LS_copper', index=False)
    dfMSstocks.to_excel(writer, sheet_name='MS_stocks', index=False)
    dfLSstocks.to_excel(writer, sheet_name='LS_stocks', index=False)





