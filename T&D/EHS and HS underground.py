'''
created by Judith van der Horst
EHS and HS combined underground cables
'''

# Import libraries
import numpy as np
from dynamic_stock_model_odym import DynamicStockModel #imports the Open Dynamic Material Systems Model (ODYM)

#packages voor exceldata
import pandas as pd


#%%
#storing the path to the data
data_path = 'Datasheet_EHS_HS.xlsx'

#reading the excel datafile and defining the historic stock
dfhistoric = pd.read_excel (data_path, sheet_name='aggregated_underground')
dffuture = pd.read_excel (data_path, sheet_name='future_underground')
dfhistoricmaterial = pd.read_excel (data_path, sheet_name='historic_inflows_underground') 
dffuturematerial = pd.read_excel (data_path, sheet_name='future_inflows_underground')
mat_intens = pd.read_excel (data_path, sheet_name= 'material_intensities')





#%% defining the EHS stocks
historicstockEHS = dfhistoric['stock EHS [km]'].tolist()

#defining stock of the regional scenario
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
intfstockHS = dffuture['HS international'].tolist()
for i in intfstockHS:
    internationalstockHS.append(i)

#defining stock of the generic scenario
genericstockHS = historicstockHS.copy()
genfstockHS = dffuture['HS generic'].tolist()
for i in genfstockHS:
    genericstockHS.append(i)




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





#%%calculating the HS DSM's for all 4 scenarios

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




#%% material separated inflows

#EHS
expansion_until_2016_EHS = dfhistoricmaterial['1933-2016 inflow EHS'].tolist()
expansion_until_2019_EHS = dfhistoricmaterial['2016-2019 inflow EHS'].tolist()

regional_expansion_2050_EHS = dffuturematerial['regional inflow EHS'].tolist()
national_expansion_2050_EHS = dffuturematerial['national inflow EHS'].tolist()
international_expansion_2050_EHS = dffuturematerial['international inflow EHS'].tolist()
generic_expansion_2050_EHS = dffuturematerial['generic inflow EHS'].tolist()


#HS
expansion_until_2009_HS = dfhistoricmaterial['1933-2010 inflow HS'].tolist()
expansion_until_2019_HS = dfhistoricmaterial['2010-2019 inflow HS'].tolist()

regional_expansion_2050_HS = dffuturematerial['regional inflow HS'].tolist()
national_expansion_2050_HS = dffuturematerial['national inflow HS'].tolist()
international_expansion_2050_HS = dffuturematerial['international inflow HS'].tolist()
generic_expansion_2050_HS = dffuturematerial['generic inflow HS'].tolist()




#%% calculating the EHS DSM material sorted for the regional scenario (periods 1933-2016 and 2016-2019 are the same for each scenario)

#1933-2016
EHS_DSM2016 = DynamicStockModel(t = timespan, i = expansion_until_2016_EHS, 
                               lt = lifetime_distribution)

Stock_by_cohort_2016_EHS = EHS_DSM2016.compute_s_c_inflow_driven()
S_2016_EHS   = EHS_DSM2016.compute_stock_total()
O_C_2016_EHS = EHS_DSM2016.compute_o_c_from_s_c()
O_2016_EHS   = EHS_DSM2016.compute_outflow_total()
DS_2016_EHS  = EHS_DSM2016.compute_stock_change()

#calculating the outflow between 1970 and 2019
outflow_2016_2019_EHS = []

for i in range(118):
    if i < 83:
        outflow_2016_2019_EHS.append(0)
    if 83 <= i < 87:
        outflow_2016_2019_EHS.append(EHS_DSM2016.o[i])
    if 87 <= i < 118:
        outflow_2016_2019_EHS.append(0)
        


#2016-2019
inflow_until_2019_EHS = [expansion_until_2019_EHS[i]+outflow_2016_2019_EHS[i] for i in range(len(expansion_until_2019_EHS))]

#1970-2019
EHS_DSM2019 = DynamicStockModel(t = timespan, i = (inflow_until_2019_EHS), 
                               lt = lifetime_distribution)

Stock_by_cohort_2019_EHS = EHS_DSM2019.compute_s_c_inflow_driven()
S_2019_EHS   = EHS_DSM2019.compute_stock_total()
O_C_2019_EHS = EHS_DSM2019.compute_o_c_from_s_c()
O_2019_EHS   = EHS_DSM2019.compute_outflow_total()
DS_2019_EHS  = EHS_DSM2019.compute_stock_change()

#calculating the outflow between 2019 and 2050
outflow_2019_2050_EHS = []

for i in range(118):
    if i < 87:
        outflow_2019_2050_EHS.append(0)
    if 87 <= i < 118:
        outflow_2019_2050_EHS.append(EHS_DSM2019.o[i]+outflow_2016_2019_EHS[i])



#%% calculating the HS DSM material sorted 
        
#1933-2009
HS_DSM2009 = DynamicStockModel(t = timespan, i = expansion_until_2009_HS, 
                               lt = lifetime_distribution)

Stock_by_cohort_2009_HS = HS_DSM2009.compute_s_c_inflow_driven()
S_2009_HS   = HS_DSM2009.compute_stock_total()
O_C_2009_HS = HS_DSM2009.compute_o_c_from_s_c()
O_2009_HS   = HS_DSM2009.compute_outflow_total()
DS_2009_HS  = HS_DSM2009.compute_stock_change()

#calculating the outflow between 1970 and 2019
outflow_2009_2019_HS = []

for i in range(118):
    if i < 77:
        outflow_2009_2019_HS.append(0)
    if 77 <= i < 87:
        outflow_2009_2019_HS.append(HS_DSM2009.o[i])
    if 87 <= i < 118:
        outflow_2009_2019_HS.append(0)
        

#2009-2019
inflow_until_2019_HS = [expansion_until_2019_HS[i]+outflow_2009_2019_HS[i] for i in range(len(expansion_until_2019_HS))]

HS_DSM2019 = DynamicStockModel(t = timespan, i = (inflow_until_2019_HS), 
                               lt = lifetime_distribution)

Stock_by_cohort_2019_HS = HS_DSM2019.compute_s_c_inflow_driven()
S_2019_HS   = HS_DSM2019.compute_stock_total()
O_C_2019_HS = HS_DSM2019.compute_o_c_from_s_c()
O_2019_HS   = HS_DSM2019.compute_outflow_total()
DS_2019_HS  = HS_DSM2019.compute_stock_change()

#calculating the outflow between 2019 and 2050
outflow_2019_2050_HS = []

for i in range(118):
    if i < 87:
        outflow_2019_2050_HS.append(0)
    if 87 <= i < 118:
        outflow_2019_2050_HS.append(HS_DSM2019.o[i]+outflow_2009_2019_HS[i])



#%% the flows of the 2019-2050 stock EHS

# regional
inflow_regional_EHS = [regional_expansion_2050_EHS[i]+outflow_2019_2050_EHS[i] for i in range(len(regional_expansion_2050_EHS))]

EHSregionalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_regional_EHS), 
                                      lt = lifetime_distribution)

Stock_by_cohort_reg2050_EHS = EHSregionalDSM2050.compute_s_c_inflow_driven()
S_reg2050_EHS   = EHSregionalDSM2050.compute_stock_total()
O_C_reg2050_EHS = EHSregionalDSM2050.compute_o_c_from_s_c()
O_reg2050_EHS   = EHSregionalDSM2050.compute_outflow_total()
DS_reg2050_EHS  = EHSregionalDSM2050.compute_stock_change()


# national
inflow_national_EHS = [national_expansion_2050_EHS[i]+outflow_2019_2050_EHS[i] for i in range(len(national_expansion_2050_EHS))]

EHSnationalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_national_EHS), 
                                      lt = lifetime_distribution)

Stock_by_cohort_nat2050_EHS = EHSnationalDSM2050.compute_s_c_inflow_driven()
S_nat2050_EHS   = EHSnationalDSM2050.compute_stock_total()
O_C_nat2050_EHS = EHSnationalDSM2050.compute_o_c_from_s_c()
O_nat2050_EHS   = EHSnationalDSM2050.compute_outflow_total()
DS_nat2050_EHS  = EHSnationalDSM2050.compute_stock_change()


# international
inflow_international_EHS = [international_expansion_2050_EHS[i]+outflow_2019_2050_EHS[i] for i in range(len(international_expansion_2050_EHS))]
#2019-2050
EHSinternationalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_international_EHS), 
                                           lt = lifetime_distribution)

Stock_by_cohort_int2050_EHS = EHSinternationalDSM2050.compute_s_c_inflow_driven()
S_int2050_EHS   = EHSinternationalDSM2050.compute_stock_total()
O_C_int2050_EHS = EHSinternationalDSM2050.compute_o_c_from_s_c()
O_int2050_EHS   = EHSinternationalDSM2050.compute_outflow_total()
DS_int2050_EHS  = EHSinternationalDSM2050.compute_stock_change()


# generic
inflow_generic_EHS = [generic_expansion_2050_EHS[i]+outflow_2019_2050_EHS[i] for i in range(len(generic_expansion_2050_EHS))]
#2019-2050
EHSgenericDSM2050 = DynamicStockModel(t = timespan, i = (inflow_generic_EHS), 
                                     lt = lifetime_distribution)

Stock_by_cohort_gen2050_EHS = EHSgenericDSM2050.compute_s_c_inflow_driven()
S_gen2050_EHS   = EHSgenericDSM2050.compute_stock_total()
O_C_gen2050_EHS = EHSgenericDSM2050.compute_o_c_from_s_c()
O_gen2050_EHS   = EHSgenericDSM2050.compute_outflow_total()
DS_gen2050_EHS  = EHSgenericDSM2050.compute_stock_change()




#%% the flows of the 2019-2050 stock LS
        
# regional
inflow_regional_HS = [regional_expansion_2050_HS[i]+outflow_2019_2050_HS[i] for i in range(len(regional_expansion_2050_HS))]

HSregionalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_regional_HS), 
                                      lt = lifetime_distribution)

Stock_by_cohort_reg2050_HS = HSregionalDSM2050.compute_s_c_inflow_driven()
S_reg2050_HS   = HSregionalDSM2050.compute_stock_total()
O_C_reg2050_HS = HSregionalDSM2050.compute_o_c_from_s_c()
O_reg2050_HS   = HSregionalDSM2050.compute_outflow_total()
DS_reg2050_HS  = HSregionalDSM2050.compute_stock_change()


# national
inflow_national_HS = [national_expansion_2050_HS[i]+outflow_2019_2050_HS[i] for i in range(len(national_expansion_2050_HS))]

HSnationalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_national_HS), 
                                      lt = lifetime_distribution)

Stock_by_cohort_nat2050_HS = HSnationalDSM2050.compute_s_c_inflow_driven()
S_nat2050_HS   = HSnationalDSM2050.compute_stock_total()
O_C_nat2050_HS = HSnationalDSM2050.compute_o_c_from_s_c()
O_nat2050_HS   = HSnationalDSM2050.compute_outflow_total()
DS_nat2050_HS  = HSnationalDSM2050.compute_stock_change()


# international 
inflow_international_HS = [international_expansion_2050_HS[i]+outflow_2019_2050_HS[i] for i in range(len(international_expansion_2050_HS))]

HSinternationalDSM2050 = DynamicStockModel(t = timespan, i = (inflow_international_HS), 
                                           lt = lifetime_distribution)

Stock_by_cohort_int2050_HS = HSinternationalDSM2050.compute_s_c_inflow_driven()
S_int2050_HS   = HSinternationalDSM2050.compute_stock_total()
O_C_int2050_HS = HSinternationalDSM2050.compute_o_c_from_s_c()
O_int2050_HS   = HSinternationalDSM2050.compute_outflow_total()
DS_int2050_HS  = HSinternationalDSM2050.compute_stock_change()


# generic
inflow_generic_HS = [generic_expansion_2050_HS[i]+outflow_2019_2050_HS[i] for i in range(len(generic_expansion_2050_HS))]
#2019-2050
HSgenericDSM2050 = DynamicStockModel(t = timespan, i = (inflow_generic_HS), 
                                     lt = lifetime_distribution)

Stock_by_cohort_gen2050_HS = HSgenericDSM2050.compute_s_c_inflow_driven()
S_gen2050_HS   = HSgenericDSM2050.compute_stock_total()
O_C_gen2050_HS = HSgenericDSM2050.compute_o_c_from_s_c()
O_gen2050_HS   = HSgenericDSM2050.compute_outflow_total()
DS_gen2050_HS  = HSgenericDSM2050.compute_stock_change()





#%% hibernating stocks EHS

# calculating hibernating EHS stock from the 1933-2016 period
inflow_rh2016_EHS=EHS_DSM2016.o.copy()*hibernation_percentage

new2016_EHS = []
hibernating_stock2016_EHS = []

for i in range(len(inflow_rh2016_EHS)):    
    new2016_EHS.append(inflow_rh2016_EHS[i])
    hibernating_stock2016_EHS.append(sum(new2016_EHS))
    
# calculating hibernating EHS stock from the 2016-2019 period
inflow_rh2019_EHS=EHS_DSM2019.o.copy()*hibernation_percentage

new2019_EHS = []
hibernating_stock2019_EHS = []

for i in range(len(inflow_rh2019_EHS)):    
    new2019_EHS.append(inflow_rh2019_EHS[i])
    hibernating_stock2019_EHS.append(sum(new2019_EHS))


#calculating hibernating EHS stock from the 2019-2050 period
inflow_rh2050_EHS = EHSregionalDSM2050.o.copy()*hibernation_percentage

new2050_EHS = []
hibernating_stock2050_EHS = []

for i in range(len(inflow_rh2050_EHS)):
    new2050_EHS.append(inflow_rh2050_EHS[i])
    hibernating_stock2050_EHS.append(sum(new2050_EHS))


# total hibernating stock
total_hibernating_stock_EHS = [hibernating_stock2016_EHS[i] + hibernating_stock2019_EHS[i] + hibernating_stock2050_EHS[i] for i in range(len(timespan))] 

#calculating the recovered MS cables
recovered2016_EHS = EHS_DSM2016.o.copy() - inflow_rh2016_EHS.copy()
recovered2019_EHS = EHS_DSM2019.o.copy() - inflow_rh2019_EHS.copy()
recovered2050_EHS = EHSregionalDSM2050.o.copy() - inflow_rh2050_EHS.copy()

total_recovered_cables_EHS = [recovered2016_EHS[i] + recovered2019_EHS[i] + recovered2050_EHS[i] for i in range(len(timespan))]



#%% hibernating stocks EHS sensitivity analysis 1

# calculating hibernating EHS stock from the 1933-2016 period
inflow_rh2016_EHS_SA_1=EHS_DSM2016.o.copy()*hibernation_percentage_SA_1

new2016_EHS_SA_1 = []
hibernating_stock2016_EHS_SA_1 = []

for i in range(len(inflow_rh2016_EHS_SA_1)):    
    new2016_EHS_SA_1.append(inflow_rh2016_EHS_SA_1[i])
    hibernating_stock2016_EHS_SA_1.append(sum(new2016_EHS_SA_1))
    
# calculating hibernating EHS stock from the 2016-2019 period
inflow_rh2019_EHS_SA_1=EHS_DSM2019.o.copy()*hibernation_percentage_SA_1

new2019_EHS_SA_1 = []
hibernating_stock2019_EHS_SA_1 = []

for i in range(len(inflow_rh2019_EHS_SA_1)):    
    new2019_EHS_SA_1.append(inflow_rh2019_EHS_SA_1[i])
    hibernating_stock2019_EHS_SA_1.append(sum(new2019_EHS_SA_1))


#calculating hibernating EHS stock from the 2019-2050 period
inflow_rh2050_EHS_SA_1 = EHSregionalDSM2050.o.copy()*hibernation_percentage_SA_1

new2050_EHS_SA_1 = []
hibernating_stock2050_EHS_SA_1 = []

for i in range(len(inflow_rh2050_EHS_SA_1)):
    new2050_EHS_SA_1.append(inflow_rh2050_EHS_SA_1[i])
    hibernating_stock2050_EHS_SA_1.append(sum(new2050_EHS_SA_1))


# total hibernating stock
total_hibernating_stock_EHS_SA_1 = [hibernating_stock2016_EHS_SA_1[i] + hibernating_stock2019_EHS_SA_1[i] + hibernating_stock2050_EHS_SA_1[i] for i in range(len(timespan))] 

#calculating the recovered MS cables
recovered2016_EHS_SA_1 = EHS_DSM2016.o.copy() - inflow_rh2016_EHS_SA_1.copy()
recovered2019_EHS_SA_1 = EHS_DSM2019.o.copy() - inflow_rh2019_EHS_SA_1.copy()
recovered2050_EHS_SA_1 = EHSregionalDSM2050.o.copy() - inflow_rh2050_EHS_SA_1.copy()

total_recovered_cables_EHS_SA_1 = [recovered2016_EHS_SA_1[i] + recovered2019_EHS_SA_1[i] + recovered2050_EHS_SA_1[i] for i in range(len(timespan))]



#%% hibernating stocks EHS sensitivity analysis 2

# calculating hibernating EHS stock from the 1933-2016 period
inflow_rh2016_EHS_SA_2=EHS_DSM2016.o.copy()*hibernation_percentage_SA_2

new2016_EHS_SA_2 = []
hibernating_stock2016_EHS_SA_2 = []

for i in range(len(inflow_rh2016_EHS_SA_2)):    
    new2016_EHS_SA_2.append(inflow_rh2016_EHS_SA_2[i])
    hibernating_stock2016_EHS_SA_2.append(sum(new2016_EHS_SA_2))
    
# calculating hibernating EHS stock from the 2016-2019 period
inflow_rh2019_EHS_SA_2=EHS_DSM2019.o.copy()*hibernation_percentage_SA_2

new2019_EHS_SA_2 = []
hibernating_stock2019_EHS_SA_2 = []

for i in range(len(inflow_rh2019_EHS_SA_2)):    
    new2019_EHS_SA_2.append(inflow_rh2019_EHS_SA_2[i])
    hibernating_stock2019_EHS_SA_2.append(sum(new2019_EHS_SA_2))


#calculating hibernating EHS stock from the 2019-2050 period
inflow_rh2050_EHS_SA_2 = EHSregionalDSM2050.o.copy()*hibernation_percentage_SA_2

new2050_EHS_SA_2 = []
hibernating_stock2050_EHS_SA_2 = []

for i in range(len(inflow_rh2050_EHS_SA_2)):
    new2050_EHS_SA_2.append(inflow_rh2050_EHS_SA_2[i])
    hibernating_stock2050_EHS_SA_2.append(sum(new2050_EHS_SA_2))


# total hibernating stock
total_hibernating_stock_EHS_SA_2 = [hibernating_stock2016_EHS_SA_2[i] + hibernating_stock2019_EHS_SA_2[i] + hibernating_stock2050_EHS_SA_2[i] for i in range(len(timespan))] 

#calculating the recovered MS cables
recovered2016_EHS_SA_2 = EHS_DSM2016.o.copy() - inflow_rh2016_EHS_SA_2.copy()
recovered2019_EHS_SA_2 = EHS_DSM2019.o.copy() - inflow_rh2019_EHS_SA_2.copy()
recovered2050_EHS_SA_2 = EHSregionalDSM2050.o.copy() - inflow_rh2050_EHS_SA_2.copy()

total_recovered_cables_EHS_SA_2 = [recovered2016_EHS_SA_2[i] + recovered2019_EHS_SA_2[i] + recovered2050_EHS_SA_2[i] for i in range(len(timespan))]




#%% hibernating stocks HS

# calculating hibernating HS stock from the 1933-2009 period
inflow_rh2009_HS=HS_DSM2009.o.copy()*hibernation_percentage

new2009_HS = []
hibernating_stock2009_HS = []

for i in range(len(inflow_rh2009_HS)):    
    new2009_HS.append(inflow_rh2009_HS[i])
    hibernating_stock2009_HS.append(sum(new2009_HS))


# calculating hibernating LS stock from the 2009-2019 period
inflow_rh2019_HS=HS_DSM2019.o.copy()*hibernation_percentage

new2019_HS = []
hibernating_stock2019_HS = []

for i in range(len(inflow_rh2019_HS)):    
    new2019_HS.append(inflow_rh2019_HS[i])
    hibernating_stock2019_HS.append(sum(new2019_HS))

# calculating hibernating LS stock from the 2019-2050 period
inflow_rh2050_HS=HSregionalDSM2050.o.copy()*hibernation_percentage

new2050_HS = []
hibernating_stock2050_HS = []

for i in range(len(inflow_rh2050_HS)):    
    new2050_HS.append(inflow_rh2050_HS[i])
    hibernating_stock2050_HS.append(sum(new2050_HS))


#total hibernating stock 
total_hibernating_stock_HS = [hibernating_stock2009_HS[i] + hibernating_stock2019_HS[i] + hibernating_stock2050_HS[i] for i in range (len(timespan))]    

#calculating the recovered LS cables
recovered2009_HS = HS_DSM2009.o.copy() - inflow_rh2009_HS.copy()
recovered2019_HS = HS_DSM2019.o.copy() - inflow_rh2019_HS.copy()
recovered2050_HS = HSregionalDSM2050.o.copy() - inflow_rh2050_HS.copy()

total_recovered_cables_HS = [recovered2009_HS[i] + recovered2019_HS[i] + recovered2050_HS[i] for i in range(len(timespan))]




#%% hibernating stocks HS sensitivity analysis 1

# calculating hibernating HS stock from the 1933-2009 period
inflow_rh2009_HS_SA_1=HS_DSM2009.o.copy()*hibernation_percentage_SA_1

new2009_HS_SA_1 = []
hibernating_stock2009_HS_SA_1 = []

for i in range(len(inflow_rh2009_HS_SA_1)):    
    new2009_HS_SA_1.append(inflow_rh2009_HS_SA_1[i])
    hibernating_stock2009_HS_SA_1.append(sum(new2009_HS_SA_1))


# calculating hibernating LS stock from the 2009-2019 period
inflow_rh2019_HS_SA_1=HS_DSM2019.o.copy()*hibernation_percentage_SA_1

new2019_HS_SA_1 = []
hibernating_stock2019_HS_SA_1 = []

for i in range(len(inflow_rh2019_HS_SA_1)):    
    new2019_HS_SA_1.append(inflow_rh2019_HS_SA_1[i])
    hibernating_stock2019_HS_SA_1.append(sum(new2019_HS_SA_1))

# calculating hibernating LS stock from the 2019-2050 period
inflow_rh2050_HS_SA_1=HSregionalDSM2050.o.copy()*hibernation_percentage_SA_1

new2050_HS_SA_1 = []
hibernating_stock2050_HS_SA_1 = []

for i in range(len(inflow_rh2050_HS_SA_1)):    
    new2050_HS_SA_1.append(inflow_rh2050_HS_SA_1[i])
    hibernating_stock2050_HS_SA_1.append(sum(new2050_HS_SA_1))


#total hibernating stock 
total_hibernating_stock_HS_SA_1 = [hibernating_stock2009_HS_SA_1[i] + hibernating_stock2019_HS_SA_1[i] + hibernating_stock2050_HS_SA_1[i] for i in range (len(timespan))]    

#calculating the recovered LS cables
recovered2009_HS_SA_1 = HS_DSM2009.o.copy() - inflow_rh2009_HS_SA_1.copy()
recovered2019_HS_SA_1 = HS_DSM2019.o.copy() - inflow_rh2019_HS_SA_1.copy()
recovered2050_HS_SA_1 = HSregionalDSM2050.o.copy() - inflow_rh2050_HS_SA_1.copy()

total_recovered_cables_HS_SA_1 = [recovered2009_HS_SA_1[i] + recovered2019_HS_SA_1[i] + recovered2050_HS_SA_1[i] for i in range(len(timespan))]




#%% hibernating stocks HS sensitivity analysis 2

# calculating hibernating HS stock from the 1933-2009 period
inflow_rh2009_HS_SA_2=HS_DSM2009.o.copy()*hibernation_percentage_SA_2

new2009_HS_SA_2 = []
hibernating_stock2009_HS_SA_2 = []

for i in range(len(inflow_rh2009_HS_SA_2)):    
    new2009_HS_SA_2.append(inflow_rh2009_HS_SA_2[i])
    hibernating_stock2009_HS_SA_2.append(sum(new2009_HS_SA_2))


# calculating hibernating LS stock from the 2009-2019 period
inflow_rh2019_HS_SA_2=HS_DSM2019.o.copy()*hibernation_percentage_SA_2

new2019_HS_SA_2 = []
hibernating_stock2019_HS_SA_2 = []

for i in range(len(inflow_rh2019_HS_SA_2)):    
    new2019_HS_SA_2.append(inflow_rh2019_HS_SA_2[i])
    hibernating_stock2019_HS_SA_2.append(sum(new2019_HS_SA_2))

# calculating hibernating LS stock from the 2019-2050 period
inflow_rh2050_HS_SA_2=HSregionalDSM2050.o.copy()*hibernation_percentage_SA_2

new2050_HS_SA_2 = []
hibernating_stock2050_HS_SA_2 = []

for i in range(len(inflow_rh2050_HS_SA_2)):    
    new2050_HS_SA_2.append(inflow_rh2050_HS_SA_2[i])
    hibernating_stock2050_HS_SA_2.append(sum(new2050_HS_SA_2))


#total hibernating stock 
total_hibernating_stock_HS_SA_2 = [hibernating_stock2009_HS_SA_2[i] + hibernating_stock2019_HS_SA_2[i] + hibernating_stock2050_HS_SA_2[i] for i in range (len(timespan))]    

#calculating the recovered LS cables
recovered2009_HS_SA_2 = HS_DSM2009.o.copy() - inflow_rh2009_HS_SA_2.copy()
recovered2019_HS_SA_2 = HS_DSM2019.o.copy() - inflow_rh2019_HS_SA_2.copy()
recovered2050_HS_SA_2 = HSregionalDSM2050.o.copy() - inflow_rh2050_HS_SA_2.copy()

total_recovered_cables_HS_SA_2 = [recovered2009_HS_SA_2[i] + recovered2019_HS_SA_2[i] + recovered2050_HS_SA_2[i] for i in range(len(timespan))]




#%% material percentages and intensities 

#EHS
#proportion aluminium and copper in the period 1933-2016
aluminium_share_2016_EHS = 0
copper_share_2016_EHS = 1

#proportion aluminium and copper in the period 2017-2019
aluminium_share_2019_EHS = 1
copper_share_2019_EHS = 0

#proportions aluminium and copper in the period 2019-2050
aluminium_share_2050_EHS = 1
copper_share_2050_EHS = 0


#EHS
#proportion aluminium and copper in the period 1933-2009
aluminium_share_2009_HS = 0
copper_share_2009_HS = 1

#proportion aluminium and copper in the period 2010-2019
aluminium_share_2019_HS = 1
copper_share_2019_HS = 0

#proportions aluminium and copper in the period 2019-2050
aluminium_share_2050_HS = 1
copper_share_2050_HS = 0


#material intensities [ton/km]
copper_intensity = mat_intens.loc[2, '(E)HS underground']
aluminium_intensity = mat_intens.loc[0, '(E)HS underground']



#%% material flows of the EHS grid
total_aluminium_inflows_regional_EHS = [(EHS_DSM2016.i[i] * aluminium_share_2016_EHS * aluminium_intensity) + (EHS_DSM2019.i[i]*aluminium_share_2019_EHS * aluminium_intensity) + 
                                       (EHSregionalDSM2050.i[i]*aluminium_share_2050_EHS * aluminium_intensity) for i in range(len(EHS_DSM2016.i))]
total_aluminium_inflows_national_EHS = [(EHS_DSM2016.i[i] * aluminium_share_2016_EHS * aluminium_intensity) + (EHS_DSM2019.i[i]*aluminium_share_2019_EHS * aluminium_intensity) + 
                                       (EHSnationalDSM2050.i[i]*aluminium_share_2050_EHS * aluminium_intensity) for i in range(len(EHS_DSM2016.i))]
total_aluminium_inflows_international_EHS = [(EHS_DSM2016.i[i] * aluminium_share_2016_EHS * aluminium_intensity) + (EHS_DSM2019.i[i]*aluminium_share_2019_EHS * aluminium_intensity) + 
                                            (EHSinternationalDSM2050.i[i]*aluminium_share_2050_EHS * aluminium_intensity) for i in range(len(EHS_DSM2016.i))]
total_aluminium_inflows_generic_EHS = [(EHS_DSM2016.i[i] * aluminium_share_2016_EHS * aluminium_intensity) + (EHS_DSM2019.i[i]*aluminium_share_2019_EHS * aluminium_intensity) + 
                                      (EHSgenericDSM2050.i[i]*aluminium_share_2050_EHS * aluminium_intensity) for i in range(len(EHS_DSM2016.i))]

total_copper_inflows_regional_EHS = [(EHS_DSM2016.i[i] * copper_share_2016_EHS * copper_intensity) + (EHS_DSM2019.i[i]*copper_share_2019_EHS * copper_intensity) + 
                                    (EHSregionalDSM2050.i[i]*copper_share_2050_EHS * copper_intensity) for i in range(len(EHS_DSM2016.i))]
total_copper_inflows_national_EHS = [(EHS_DSM2016.i[i] * copper_share_2016_EHS * copper_intensity) + (EHS_DSM2019.i[i]*copper_share_2019_EHS * copper_intensity) + 
                                    (EHSnationalDSM2050.i[i]*copper_share_2050_EHS * copper_intensity) for i in range(len(EHS_DSM2016.i))]
total_copper_inflows_international_EHS = [(EHS_DSM2016.i[i] * copper_share_2016_EHS * copper_intensity) + (EHS_DSM2019.i[i]*copper_share_2019_EHS * copper_intensity) + 
                                         (EHSinternationalDSM2050.i[i]*copper_share_2050_EHS * copper_intensity) for i in range(len(EHS_DSM2016.i))]
total_copper_inflows_generic_EHS = [(EHS_DSM2016.i[i] * copper_share_2016_EHS * copper_intensity) + (EHS_DSM2019.i[i]*copper_share_2019_EHS * copper_intensity) + 
                                   (EHSgenericDSM2050.i[i]*copper_share_2050_EHS * copper_intensity) for i in range(len(EHS_DSM2016.i))]

total_aluminium_outflows_EHS = [(EHS_DSM2016.o[i] * aluminium_share_2016_EHS * aluminium_intensity) + (EHS_DSM2019.o[i]*aluminium_share_2019_EHS * aluminium_intensity) + 
                                       (EHSregionalDSM2050.o[i]*aluminium_share_2050_EHS * aluminium_intensity) for i in range(len(EHS_DSM2016.o))]
total_copper_outflows_EHS = [(EHS_DSM2016.o[i] * copper_share_2016_EHS * copper_intensity) + (EHS_DSM2019.o[i]*copper_share_2019_EHS * copper_intensity) + 
                                    (EHSregionalDSM2050.o[i]*copper_share_2050_EHS * copper_intensity) for i in range(len(EHS_DSM2016.o))]

total_aluminium_recovered_EHS = [(recovered2016_EHS[i]*aluminium_share_2016_EHS * aluminium_intensity) + (recovered2019_EHS[i]*aluminium_share_2019_EHS * aluminium_intensity) + 
                                 (recovered2050_EHS[i]*aluminium_share_2050_EHS * aluminium_intensity) for i in range(len(timespan))]
total_aluminium_recovered_EHS_SA_1 = [(recovered2016_EHS_SA_1[i]*aluminium_share_2016_EHS * aluminium_intensity) + (recovered2019_EHS_SA_1[i]*aluminium_share_2019_EHS * aluminium_intensity) + 
                                 (recovered2050_EHS_SA_1[i]*aluminium_share_2050_EHS * aluminium_intensity) for i in range(len(timespan))]
total_aluminium_recovered_EHS_SA_2 = [(recovered2016_EHS_SA_2[i]*aluminium_share_2016_EHS * aluminium_intensity) + (recovered2019_EHS_SA_2[i]*aluminium_share_2019_EHS * aluminium_intensity) + 
                                 (recovered2050_EHS_SA_2[i]*aluminium_share_2050_EHS * aluminium_intensity) for i in range(len(timespan))]


total_copper_recovered_EHS = [(recovered2016_EHS[i]*copper_share_2016_EHS * copper_intensity) + (recovered2019_EHS[i]*copper_share_2019_EHS * copper_intensity) + 
                              (recovered2050_EHS[i]*copper_share_2050_EHS * copper_intensity) for i in range(len(timespan))]
total_copper_recovered_EHS_SA_1 = [(recovered2016_EHS_SA_1[i]*copper_share_2016_EHS * copper_intensity) + (recovered2019_EHS_SA_1[i]*copper_share_2019_EHS * copper_intensity) + 
                              (recovered2050_EHS_SA_1[i]*copper_share_2050_EHS * copper_intensity) for i in range(len(timespan))]
total_copper_recovered_EHS_SA_2 = [(recovered2016_EHS_SA_2[i]*copper_share_2016_EHS * copper_intensity) + (recovered2019_EHS_SA_2[i]*copper_share_2019_EHS * copper_intensity) + 
                              (recovered2050_EHS_SA_2[i]*copper_share_2050_EHS * copper_intensity) for i in range(len(timespan))]




#%% material flows of the HS grid
total_aluminium_inflows_regional_HS = [(HS_DSM2009.i[i] * aluminium_share_2009_HS * aluminium_intensity) + (HS_DSM2019.i[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                                       (HSregionalDSM2050.i[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]
total_aluminium_inflows_national_HS = [(HS_DSM2009.i[i] * aluminium_share_2009_HS * aluminium_intensity) + (HS_DSM2019.i[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                                       (HSnationalDSM2050.i[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]
total_aluminium_inflows_international_HS = [(HS_DSM2009.i[i] * aluminium_share_2009_HS * aluminium_intensity) + (HS_DSM2019.i[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                                            (HSinternationalDSM2050.i[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]
total_aluminium_inflows_generic_HS = [(HS_DSM2009.i[i] * aluminium_share_2009_HS * aluminium_intensity) + (HS_DSM2019.i[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                                      (HSgenericDSM2050.i[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]


total_copper_inflows_regional_HS = [(HS_DSM2009.i[i] * copper_share_2009_HS * copper_intensity) + (HS_DSM2019.i[i]*copper_share_2019_HS * copper_intensity) + 
                                    (HSregionalDSM2050.i[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]
total_copper_inflows_national_HS = [(HS_DSM2009.i[i] * copper_share_2009_HS * copper_intensity) + (HS_DSM2019.i[i]*copper_share_2019_HS * copper_intensity) + 
                                    (HSnationalDSM2050.i[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]
total_copper_inflows_international_HS = [(HS_DSM2009.i[i] * copper_share_2009_HS * copper_intensity) + (HS_DSM2019.i[i]*copper_share_2019_HS * copper_intensity) + 
                                         (HSinternationalDSM2050.i[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]
total_copper_inflows_generic_HS = [(HS_DSM2009.i[i] * copper_share_2009_HS * copper_intensity) + (HS_DSM2019.i[i]*copper_share_2019_HS * copper_intensity) + 
                                   (HSgenericDSM2050.i[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]

total_aluminium_outflows_HS = [(HS_DSM2009.o[i] * aluminium_share_2009_HS * aluminium_intensity) + (HS_DSM2019.o[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                                       (HSregionalDSM2050.o[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]
total_copper_outflows_HS = [(HS_DSM2009.o[i] * copper_share_2009_HS * copper_intensity) + (HS_DSM2019.o[i]*copper_share_2019_HS * copper_intensity) + 
                                    (HSregionalDSM2050.o[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]

total_aluminium_recovered_HS = [(recovered2009_HS[i]*aluminium_share_2009_HS * aluminium_intensity) + (recovered2019_HS[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                                (recovered2050_HS[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]
total_aluminium_recovered_HS_SA_1 = [(recovered2009_HS_SA_1[i]*aluminium_share_2009_HS * aluminium_intensity) + (recovered2019_HS_SA_1[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                                (recovered2050_HS_SA_1[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]
total_aluminium_recovered_HS_SA_2 = [(recovered2009_HS_SA_2[i]*aluminium_share_2009_HS * aluminium_intensity) + (recovered2019_HS_SA_2[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                                (recovered2050_HS_SA_2[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]

total_copper_recovered_HS = [(recovered2009_HS[i]*copper_share_2009_HS * copper_intensity) + (recovered2019_HS[i]*copper_share_2019_HS * copper_intensity) + 
                             (recovered2050_HS[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]
total_copper_recovered_HS_SA_1 = [(recovered2009_HS_SA_1[i]*copper_share_2009_HS * copper_intensity) + (recovered2019_HS_SA_1[i]*copper_share_2019_HS * copper_intensity) + 
                             (recovered2050_HS_SA_1[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]
total_copper_recovered_HS_SA_2 = [(recovered2009_HS_SA_2[i]*copper_share_2009_HS * copper_intensity) + (recovered2019_HS_SA_2[i]*copper_share_2019_HS * copper_intensity) + 
                             (recovered2050_HS_SA_2[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]




#%% total material flows
total_aluminium_inflows_regional_EHS_HS = [total_aluminium_inflows_regional_EHS[i] + total_aluminium_inflows_regional_HS[i] for i in range(len(timespan))]
total_aluminium_inflows_national_EHS_HS = [total_aluminium_inflows_national_EHS[i] + total_aluminium_inflows_national_HS[i] for i in range(len(timespan))]
total_aluminium_inflows_international_EHS_HS = [total_aluminium_inflows_international_EHS[i] + total_aluminium_inflows_international_HS[i] for i in range(len(timespan))]
total_aluminium_inflows_generic_EHS_HS = [total_aluminium_inflows_generic_EHS[i] + total_aluminium_inflows_generic_HS[i] for i in range(len(timespan))]
        
total_copper_inflows_regional_EHS_HS = [total_copper_inflows_regional_EHS[i] + total_copper_inflows_regional_HS[i] for i in range(len(timespan))]
total_copper_inflows_national_EHS_HS = [total_copper_inflows_national_EHS[i] + total_copper_inflows_national_HS[i] for i in range(len(timespan))]
total_copper_inflows_international_EHS_HS = [total_copper_inflows_international_EHS[i] + total_copper_inflows_international_HS[i] for i in range(len(timespan))]
total_copper_inflows_generic_EHS_HS = [total_copper_inflows_generic_EHS[i] + total_copper_inflows_generic_HS[i] for i in range(len(timespan))]

total_aluminium_outflows_EHS_HS = [total_aluminium_outflows_EHS[i] + total_aluminium_outflows_HS[i] for i in range(len(timespan))]
total_copper_outflows_EHS_HS = [total_copper_outflows_EHS[i] + total_copper_outflows_HS[i] for i in range(len(timespan))]

total_aluminium_recovered_EHS_HS = [total_aluminium_recovered_EHS[i] + total_aluminium_recovered_HS[i] for i in range(len(timespan))]
total_aluminium_recovered_EHS_HS_SA_1 = [total_aluminium_recovered_EHS_SA_1[i] + total_aluminium_recovered_HS_SA_1[i] for i in range(len(timespan))]
total_aluminium_recovered_EHS_HS_SA_2 = [total_aluminium_recovered_EHS_SA_2[i] + total_aluminium_recovered_HS_SA_2[i] for i in range(len(timespan))]

total_copper_recovered_EHS_HS = [total_copper_recovered_EHS[i] + total_copper_recovered_HS[i] for i in range(len(timespan))]
total_copper_recovered_EHS_HS_SA_1 = [total_copper_recovered_EHS_SA_1[i] + total_copper_recovered_HS_SA_1[i] for i in range(len(timespan))]
total_copper_recovered_EHS_HS_SA_2 = [total_copper_recovered_EHS_SA_2[i] + total_copper_recovered_HS_SA_2[i] for i in range(len(timespan))]





#%% calculating the material hibernating stock

aluminium_hibernating_stock = [(hibernating_stock2016_EHS[i]*aluminium_share_2016_EHS * aluminium_intensity) +
                               (hibernating_stock2019_EHS[i]*aluminium_share_2019_EHS * aluminium_intensity) +
                               (hibernating_stock2050_EHS[i]*aluminium_share_2050_EHS * aluminium_intensity) +
                               (hibernating_stock2009_HS[i]*aluminium_share_2009_HS * aluminium_intensity) +
                               (hibernating_stock2019_HS[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                               (hibernating_stock2050_HS[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]

aluminium_hibernating_stock_SA_1 = [(hibernating_stock2016_EHS_SA_1[i]*aluminium_share_2016_EHS * aluminium_intensity) +
                               (hibernating_stock2019_EHS_SA_1[i]*aluminium_share_2019_EHS * aluminium_intensity) +
                               (hibernating_stock2050_EHS_SA_1[i]*aluminium_share_2050_EHS * aluminium_intensity) +
                               (hibernating_stock2009_HS_SA_1[i]*aluminium_share_2009_HS * aluminium_intensity) +
                               (hibernating_stock2019_HS_SA_1[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                               (hibernating_stock2050_HS_SA_1[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]

aluminium_hibernating_stock_SA_2 = [(hibernating_stock2016_EHS_SA_2[i]*aluminium_share_2016_EHS * aluminium_intensity) +
                               (hibernating_stock2019_EHS_SA_2[i]*aluminium_share_2019_EHS * aluminium_intensity) +
                               (hibernating_stock2050_EHS_SA_2[i]*aluminium_share_2050_EHS * aluminium_intensity) +
                               (hibernating_stock2009_HS_SA_2[i]*aluminium_share_2009_HS * aluminium_intensity) +
                               (hibernating_stock2019_HS_SA_2[i]*aluminium_share_2019_HS * aluminium_intensity) + 
                               (hibernating_stock2050_HS_SA_2[i]*aluminium_share_2050_HS * aluminium_intensity) for i in range(len(timespan))]


copper_hibernating_stock = [(hibernating_stock2016_EHS[i]*copper_share_2016_EHS * copper_intensity) + 
                           (hibernating_stock2019_EHS[i]*copper_share_2019_EHS * copper_intensity) + 
                           (hibernating_stock2050_EHS[i]*copper_share_2050_EHS * copper_intensity) +
                           (hibernating_stock2009_HS[i]*copper_share_2009_HS * copper_intensity) + 
                           (hibernating_stock2019_HS[i]*copper_share_2019_HS * copper_intensity) +
                           (hibernating_stock2050_HS[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]

copper_hibernating_stock_SA_1 = [(hibernating_stock2016_EHS_SA_1[i]*copper_share_2016_EHS * copper_intensity) + 
                           (hibernating_stock2019_EHS_SA_1[i]*copper_share_2019_EHS * copper_intensity) + 
                           (hibernating_stock2050_EHS_SA_1[i]*copper_share_2050_EHS * copper_intensity) +
                           (hibernating_stock2009_HS_SA_1[i]*copper_share_2009_HS * copper_intensity) + 
                           (hibernating_stock2019_HS_SA_1[i]*copper_share_2019_HS * copper_intensity) +
                           (hibernating_stock2050_HS_SA_1[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]

copper_hibernating_stock_SA_2 = [(hibernating_stock2016_EHS_SA_2[i]*copper_share_2016_EHS * copper_intensity) + 
                           (hibernating_stock2019_EHS_SA_2[i]*copper_share_2019_EHS * copper_intensity) + 
                           (hibernating_stock2050_EHS_SA_2[i]*copper_share_2050_EHS * copper_intensity) +
                           (hibernating_stock2009_HS_SA_2[i]*copper_share_2009_HS * copper_intensity) + 
                           (hibernating_stock2019_HS_SA_2[i]*copper_share_2019_HS * copper_intensity) +
                           (hibernating_stock2050_HS_SA_2[i]*copper_share_2050_HS * copper_intensity) for i in range(len(timespan))]




#%% putting all data into excelsheet. Needed in order to combine the data of all different voltage levels.

# creating dataframes to write to excel
EHS_stocks = {'years': timespan,
             'regional_EHS_stocks': EHSregionalDSM.s,
             'national_EHS_stocks': EHSnationalDSM.s,
             'international_EHS_stocks': EHSinternationalDSM.s,
             'generic_EHS_stocks': EHSgenericDSM.s}
dfEHSstocks = pd.DataFrame(EHS_stocks, columns=['years', 'regional_EHS_stocks', 'national_EHS_stocks', 'international_EHS_stocks', 'generic_EHS_stocks'])


HS_stocks = {'years': timespan,
             'regional_HS_stocks': HSregionalDSM.s,
             'national_HS_stocks': HSnationalDSM.s,
             'international_HS_stocks': HSinternationalDSM.s,
             'generic_HS_stocks': HSgenericDSM.s}
dfHSstocks = pd.DataFrame(HS_stocks, columns=['years', 'regional_HS_stocks', 'national_HS_stocks', 'international_HS_stocks', 'generic_HS_stocks'])

EHS_flows = {'years': timespan,
             'regional_EHS_inflows': EHSregionalDSM.i,
             'national_EHS_inflows': EHSnationalDSM.i,
             'international_EHS_inflows': EHSinternationalDSM.i,
             'generic_EHS_inflows': EHSgenericDSM.i,
             'EHS_outflows': EHSregionalDSM.o}
dfEHSflows = pd.DataFrame(EHS_flows, columns=['years','regional_EHS_inflows', 'national_EHS_inflows', 'international_EHS_inflows', 'generic_EHS_inflows', 'EHS_outflows'])

HS_flows = {'years': timespan,
            'regional_HS_inflows': HSregionalDSM.i,
            'national_HS_inflows': HSnationalDSM.i,
            'international_HS_inflows': HSinternationalDSM.i,
            'generic_HS_inflows': HSgenericDSM.i,
            'HS_outflows': HSregionalDSM.o}
dfHSflows =pd.DataFrame(HS_flows, columns=['years', 'regional_HS_inflows', 'national_HS_inflows', 'international_HS_inflows', 'generic_HS_inflows', 'HS_outflows']) 

aluminium = {'years': timespan,
             'regional_EHS_HS_underground': total_aluminium_inflows_regional_EHS_HS,
             'national_EHS_HS_underground': total_aluminium_inflows_national_EHS_HS,
             'international_EHS_HS_underground': total_aluminium_inflows_national_EHS_HS,
             'generic_EHS_HS_underground': total_aluminium_inflows_national_EHS_HS,
             'outflows_EHS_HS_underground': total_aluminium_outflows_EHS_HS,
             'hibernating_stock_EHS_HS_underground': aluminium_hibernating_stock,
             'hibernating_stock_EHS_HS_underground_SA_1': aluminium_hibernating_stock_SA_1,
             'hibernating_stock_EHS_HS_underground_SA_2': aluminium_hibernating_stock_SA_2,
             'recovered_EHS_HS_underground': total_aluminium_recovered_EHS_HS,
             'recovered_EHS_HS_underground_SA_1': total_aluminium_recovered_EHS_HS_SA_1,
             'recovered_EHS_HS_underground_SA_2': total_aluminium_recovered_EHS_HS_SA_2}
dfaluminium=pd.DataFrame(aluminium, columns=['years','regional_EHS_HS_underground', 'national_EHS_HS_underground', 'international_EHS_HS_underground', 'generic_EHS_HS_underground', 'outflows_EHS_HS_underground', 'hibernating_stock_EHS_HS_underground', 'hibernating_stock_EHS_HS_underground_SA_1', 'hibernating_stock_EHS_HS_underground_SA_2', 'recovered_EHS_HS_underground', 'recovered_EHS_HS_underground_SA_1', 'recovered_EHS_HS_underground_SA_2'])

copper = {'years': timespan,
          'regional_EHS_HS_underground': total_copper_inflows_regional_EHS_HS,
          'national_EHS_HS_underground': total_copper_inflows_national_EHS_HS,
          'international_EHS_HS_underground': total_copper_inflows_national_EHS_HS,
          'generic_EHS_HS_underground': total_copper_inflows_national_EHS_HS,
          'outflows_EHS_HS_underground': total_copper_outflows_EHS_HS,
          'hibernating_stock_EHS_HS_underground': copper_hibernating_stock,
          'hibernating_stock_EHS_HS_underground_SA_1': copper_hibernating_stock_SA_1,
          'hibernating_stock_EHS_HS_underground_SA_2': copper_hibernating_stock_SA_2,
          'recovered_EHS_HS_underground': total_copper_recovered_EHS_HS,
          'recovered_EHS_HS_underground_SA_1': total_copper_recovered_EHS_HS_SA_1,
          'recovered_EHS_HS_underground_SA_2': total_copper_recovered_EHS_HS_SA_2}
dfcopper=pd.DataFrame(copper, columns=['years', 'regional_EHS_HS_underground', 'national_EHS_HS_underground', 'international_EHS_HS_underground', 'generic_EHS_HS_underground', 'outflows_EHS_HS_underground', 'hibernating_stock_EHS_HS_underground', 'hibernating_stock_EHS_HS_underground_SA_1', 'hibernating_stock_EHS_HS_underground_SA_2', 'recovered_EHS_HS_underground', 'recovered_EHS_HS_underground_SA_1', 'recovered_EHS_HS_underground_SA_2'])


#writing the dataframes to excel
with pd.ExcelWriter('EHS_HS_underground_result_data.xlsx') as writer:
    dfaluminium.to_excel(writer, sheet_name='aluminium', index=False)
    dfcopper.to_excel(writer, sheet_name='copper', index=False)
    dfEHSstocks.to_excel(writer, sheet_name='EHS_stocks', index=False)
    dfHSstocks.to_excel(writer, sheet_name='HS_stocks', index=False)
    dfEHSflows.to_excel(writer, sheet_name='EHS_flows', index=False)
    dfHSflows.to_excel(writer, sheet_name='HS_flows', index=False)
    


