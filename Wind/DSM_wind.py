# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:27:55 2021

@author: jvano
"""
#%% 1. Data import

#Import Python libraries
import pandas as pd
import matplotlib.dates as date
import numpy as np
import matplotlib.pyplot as plt
from dynamic_stock_model_odym import DynamicStockModel
import pickle                                                                   
# Import windstats data
df_windstats = pd.read_excel (r'Input_data_wind.xlsx', sheet_name = 'Historic')      
# Rewrite column names to make them readable
df_windstats.columns = ['Project ID', 'Asset ID', 'Project', 'Locatie', 'Merk',
                        'Type', 'Capacity', 'Aep MWh', 'Ashoogte',
                        'Rotordiameter', 'Gemeente', 'Provincie', 'LAT', 'LON',
                        'Startdatum', 'Einddatum' ]
# Remove quotes in each cell
for i, col in enumerate(df_windstats.columns):
    df_windstats.iloc[:, i] = df_windstats.iloc[:, i].str.replace("'", '')   
# Delete unused columns     
for x in ['Asset ID', 'Project' ,'Aep MWh', 'Gemeente', 'LAT','LON',\
'Einddatum']:
    df_windstats = df_windstats.drop(x, axis=1)   
# Select year from date and convert to float                              
df_windstats['Startdatum']=df_windstats['Startdatum'].astype(str).str[6:].\
astype(np.int64)                                                             
# Convert to float and unit MW   
df_windstats['Rated_capacity']=df_windstats['Capacity'].astype(np.float)/1000  
df_windstats['Capacity']=df_windstats['Capacity'].astype(np.float)/1000   
# Convert to float
df_windstats['Ashoogte']=df_windstats['Ashoogte'].astype(np.float)   
df_windstats['Rotordiameter']=df_windstats['Rotordiameter'].astype(np.float)
# Sort by date    
df_installed=df_windstats.sort_values('Startdatum')                             
df_installed=df_windstats.sort_values('Startdatum')                             
# Fill empty lines with 0's to prevent NaN errors 
df_0 = pd.DataFrame({'Project ID':38*[0],'Merk':38*[0],'Type':38*[0],'Capacity' 
:38*[0],'Ashoogte':38*[0],'Rotordiameter':38*[0],'Provincie':38*[0],\
'Startdatum': list(range(1982,2020,1))})
# Create dataframe with offshore/onshore installations
offshore = df_installed[df_installed['Provincie'].str.match('Offshore')]        
onshore = df_installed[~df_installed['Provincie'].str.match('Offshore')] 
# Compensate for historic data discrepancy  
onshore['Capacity']=onshore['Capacity']/0.71
# Import scenario data
future_onshore = pd.read_excel (r'Input_data_wind.xlsx', sheet_name = 'Onshore')     
future_offshore = pd.read_excel (r'Input_data_wind.xlsx', sheet_name = 'Offshore')  
# warning disabled, values checked
pd.options.mode.chained_assignment = None

print(onshore)



#%% 2. Future inflows

# Group onshore inflows per year (decreases runtime)
on_hist = onshore.groupby(['Startdatum']).agg({'Startdatum':'first', 'Capacity'\
:'sum', 'Ashoogte':'mean', 'Rated_capacity':'mean'})                                  
off_hist = offshore.groupby(['Startdatum']).agg({'Startdatum':'first',\
'Capacity':'sum', 'Ashoogte':'mean', 'Rated_capacity':'mean'})                     
# Create empty list to save DSM loop results
historic = []                        
# Run DSM to obtain stocks from offshore and onshore historic inflows                                           
for a,n in zip([off_hist, on_hist],['offshore', 'onshore']):
  # Lifetime is determined in the Stock Analysis chapter                    
  Lifetime = {'Type': 'Normal', 'Mean':np.array([18]), 'StdDev':np.array([5.3])}
  # Create variable name 
  name = '{0}_DSM'.format(a)     
  # Run DSM                                               
  name = DynamicStockModel(t = a['Startdatum'].values.tolist(),                 
                           i = a['Capacity'].values.tolist(), lt = Lifetime)
  CheckStr = name.dimension_check()
  Stock_by_cohort_cap = name.compute_s_c_inflow_driven()                            
  S_cap  = name.compute_stock_total()
  O_C_cap = name.compute_o_c_from_s_c()
  O_cap   = name.compute_outflow_total()
  DS_cap  = name.compute_stock_change()
  # Save time DSM to list                                 
  historic.append(name.t)     
  # Save stock DSM to list                                                  
  historic.append(name.s)   
# Create empty dataframe for future scenarios                                                  
df_scenarios = pd.DataFrame({})     
# Create empty list to save DSM looop results                                           
future = []
# Loop to join historic and future time and stocks for the scenarios                                                                     
for scenario in ['Low','Mid','High']:                                           
  full_offshore_t = list(historic[0])+future_offshore['Year'].values.tolist()   
  full_offshore = list(historic[1])+future_offshore[scenario].values.tolist()   
  full_onshore_t = list(historic[2])+future_onshore['Year'].values.tolist()     
  full_onshore = list(historic[3])+future_onshore[scenario].values.tolist()
  # Add time to dataframe onshore/offshore     
  onshore_scen_df = pd.DataFrame({'Time': on_hist['Startdatum'].values.\
  tolist()})                                                                    
  offshore_scen_df = pd.DataFrame({'Time': off_hist['Startdatum'].values.\
  tolist()})                                                                    
  for a,b,n in zip([full_offshore_t, full_onshore_t],[full_offshore,\
  full_onshore],['full_offshore', 'full_onshore']):                             
    name=n
    # Run DSM to obtain inflows from offshore and onshore stocks
    name = DynamicStockModel(t =a, s = b, lt = {'Type': 'Normal', 'Mean':\
    np.array([22]), 'StdDev': np.array([4]) })
    CheckStr = name.dimension_check()
    s_c, o_c, I = name.compute_stock_driven_model()
    O   = name.compute_outflow_total()
    DS  = name.compute_stock_change()
    # Save timeand inflow DSM to list
    future.append(name.t)                                                       
    future.append(name.i)      
    # Print progress inflow calculations                                 
    print('done - {0}'.format(n)+' - {0}'.format(scenario))
# Save scenario lists to dataframe low/mid/high scenario                     
df_low = pd.DataFrame({'time':future[0][-31:], 'offshore':future[1][-31:],\
'onshore':future[3][-31:]})                                                     
df_mid = pd.DataFrame({'time':future[0][-31:], 'offshore':future[5][-31:],\
'onshore':future[7][-31:]})                                                     
df_high = pd.DataFrame({'time':future[0][-31:], 'offshore':future[9][-31:],\
'onshore':future[11][-31:]})      


#%% 3. Material compositions

# Supplement with 0's to prevent NaN errors
offshore = pd.concat([df_0, offshore], ignore_index=True, sort=True)            
onshore = pd.concat([df_0, onshore], ignore_index=True, sort=True)              
# Obtain dataframe for material compositions from Input data file
Mat_comp = pd.read_excel (r'Input_data_wind.xlsx', sheet_name = 'Mat_comp')
# Index dataframe by component
Mat_comp = Mat_comp.set_index('Component')                                      
# Obtain dataframe for chosen variables (used for sensitivity checks) from Input data file
Sensitivity = pd.read_excel (r'Input_data_wind.xlsx', sheet_name= 'Default')  
# Index dataframe by Variable       
Sensitivity = Sensitivity.set_index('Variables')                                
# Loop over the three scenarios                             
for scenario, name in zip([df_low, df_mid, df_high],['low','mid','high']):
  # Create columns for variables in future offshore dataframe      
  future_offshore = pd.DataFrame({'Ashoogte': 31*[0],'Capacity': scenario\
  ['offshore'], 'Merk' : 31*[0],'Project ID': 31*[0],'Provincie': 31*[0],\
  'Rotordiameter': 31*[0],'Startdatum':scenario['time'],'Type': 31*[0], \
  'Generator_type': 31*[0], 'tower_type' : 31*[0],'blade_mass': 31*[0], \
  'blade_CF': 31*[0],'blade_GF': 31*[0], 'gearbox': 31*[0]})                    
  # Create columns for variables in future offshore dataframe
  future_onshore = pd.DataFrame({'Ashoogte': 31*[0],'Capacity': scenario\
  ['onshore'], 'Merk' : 31*[0],'Project ID': 31*[0],'Provincie': 31*[0],\
  'Rotordiameter': 31*[0],'Startdatum':scenario['time'],'Type': 31*[0], \
  'Generator_type': 31*[0], 'tower_type' : 31*[0],'blade_mass': 31*[0], \
  'blade_CF': 31*[0],'blade_GF': 31*[0], 'gearbox': 31*[0]})                    
  # Create empty list to store loop values
  l=[]                       
  # Loop over offshore and onshore (within scenario loop)                                                   
  for t,n,f in zip([offshore, onshore],['Offshore', 'Onshore'],[future_offshore\
  , future_onshore]):              
  # Set conditions for historic generator type based on technology analysis                                             
    conditions_generator = [
    (t['Merk'] ==  'Enercon'),
    (t['Merk'] == 'Vestas')  &(t['Capacity']>= 3   )&(t['Rotordiameter']>= 112), 
    (t['Merk'] == 'Lagerwey')&(t['Capacity']>= 0.75)&(t['Capacity'] < 4)       ,
    (t['Merk'] == 'Lagerwey')&(t['Capacity']>= 4   )                           ,
    (t['Merk'] == 'Siemens') &(t['Capacity']>= 3)   &(t['Rotordiameter'] > 101),
    (t['Merk'] == 'GE Wind') &(t['Capacity']>= 4   )                           ]
    # List for historic generator types based on conditions
    Generator_type = ['EESG', 'MSPMG', 'EESG','DDPMG','DDPMG', 'DDPMG']         
    # Set condition for historic tower type based on manufacturer
    conditions_tower = [(t['Merk'] ==  'Enercon')]    
    # List for historic tower type based on conditions                          
    tower_type = ['concrete']                                                   
    # Set conditions for historic blade mass based on technology analysis
    conditions_blade_mass =[(t['Capacity'] < 1), 
                            (t['Capacity'] >= 1) & (t['Capacity'] < 1.5),
                            (t['Capacity'] >= 1.5)  & (t['Capacity'] < 2.5),
                            (t['Capacity'] >= 2.5)  & (t['Capacity'] < 5),
                            (t['Capacity'] >= 6)]                              
    # List for historic blade mass based on conditions
    blade_mass = [8.43, 12.37, 13.34, 13.41, 12.58]                             
    # Set conditions for historic blade fibre use based on technology analysis
    conditions_blade_type = [(t['Capacity'] >= 2) & (t['Startdatum'] >= 2010)]
    # List for historic blade fibre use based on conditions 
    blade_CF = [0.06]                                                           
    blade_GF = [0.544]                                                          
    # Assign generator types
    t = t.assign(Generator_type = np.select(conditions_generator, \
    Generator_type, default = 'AG'))    
    # With assigned generator types, create conditions gearbox and generator use (Yes/No = 1/0)                                        
    conditions_drivetrain =[(t['Generator_type'] == 'AG'), (t['Generator_type']\
    == 'MSPMG'),(t['Generator_type'] == 'HSPMG'),(t['Generator_type'] == \
    'DDPMG'), (t['Generator_type'] == 'EESG')]                                  
    gearbox = [1,1,1,0,0]
    AG =      [1,0,0,0,0]
    MSPMG =   [0,1,0,0,0]
    HSPMG =   [0,0,1,0,0]
    DDPMG =   [0,0,0,1,0]
    EESG =    [0,0,0,0,1]
    # Assign tower type
    t = t.assign(tower_type = np.select(conditions_tower, tower_type, default =\
    'steel'))      
    # Assign blade mass                                                             
    t = t.assign(blade_mass = np.select(conditions_blade_mass, blade_mass,\
    default = 12))      
    # Assign blade CF content                                                          
    t = t.assign(blade_CF = np.select(conditions_blade_type, blade_CF, default\
    = 0))           
    # Assign blade GF conent                                                            
    t = t.assign(blade_GF = np.select(conditions_blade_type, blade_GF, default\
    = 0.604))                
    # Assign gearbox use                                                   
    t = t.assign(gearbox = np.select(conditions_drivetrain, gearbox, default =\
    0))              
    # Assign asynchronous generator use                                                           
    t = t.assign(AG = np.select(conditions_drivetrain, AG, default = 0))      
    # Assign medium speed permanent magnet generator use  
    t = t.assign(MSPMG = np.select(conditions_drivetrain, MSPMG, default = 0))
    # Assign high speed permanent magnet generator use  
    t = t.assign(HSPMG = np.select(conditions_drivetrain, HSPMG, default = 0))
    # Assign direct drive permanent magnet generator use  
    t = t.assign(DDPMG = np.select(conditions_drivetrain, DDPMG, default = 0))
    # Assign electrically excited generator use  
    t = t.assign(EESG = np.select(conditions_drivetrain, EESG, default = 0))    
    f['Provincie'] = n
    # Set conditions for future wind turbine type based on technology analysis
    conditions_dev = [
    (f['Startdatum']>=2020)&(f['Startdatum']< 2025)&(f['Provincie']=='Onshore'),
    (f['Startdatum']>=2025)&(f['Startdatum']< 2030)&(f['Provincie']=='Onshore'),
    (f['Startdatum']>=2030)&(f['Startdatum']< 2040)&(f['Provincie']=='Onshore'),
    (f['Startdatum']>=2040)&(f['Startdatum']<=2050)&(f['Provincie']=='Onshore'),
    (f['Startdatum']>=2020)&(f['Startdatum']< 2025)&(f['Provincie']=='Offshore'),
    (f['Startdatum']>=2025)&(f['Startdatum']< 2030)&(f['Provincie']=='Offshore'),
    (f['Startdatum']>=2030)&(f['Startdatum']< 2040)&(f['Provincie']=='Offshore'),
    (f['Startdatum']>=2040)&(f['Startdatum']<=2050)&(f['Provincie']=='Offshore')]
    # Generator share for each condition using market shares from input data
    AG_onshore    =    Sensitivity.loc['AG_onshore'].tolist()                   
    AG_offshore   =    Sensitivity.loc['AG_offshore'].tolist()                     
    HSPMG_onshore =    Sensitivity.loc['HSPMG_onshore'].tolist()
    HSPMG_offshore=    Sensitivity.loc['HSPMG_offshore'].tolist()
    MSPMG_onshore =    Sensitivity.loc['MSPMG_onshore'].tolist()
    MSPMG_offshore=    Sensitivity.loc['MSPMG_offshore'].tolist()
    DDPMG_onshore =    Sensitivity.loc['DDPMG_onshore'].tolist()
    DDPMG_offshore=    Sensitivity.loc['DDPMG_offshore'].tolist()
    EESG_onshore  =    Sensitivity.loc['EESG_onshore'].tolist()
    EESG_offshore =    Sensitivity.loc['EESG_offshore'].tolist()
    HTS_onshore   =    Sensitivity.loc['HTS_onshore'].tolist()
    HTS_offshore  =    Sensitivity.loc['HTS_offshore'].tolist()
    # Sum of geared drivetrain to determine total gearbox use onshore
    geared_onshore =  [a+b+c for a,b,c in zip(AG_onshore,HSPMG_onshore,\
    MSPMG_onshore)]     
    # Sum of geared drivetrain to determine total gearbox use offshore                                                        
    geared_offshore=  [a+b+c for a,b,c in zip(AG_offshore,HSPMG_offshore,\
    MSPMG_offshore)]       
    # Average hub height for each condition using market shares from input data - Sensitivity                                                     
    Ashoogte_onshore = Sensitivity.loc['Hubheight_onshore'].tolist()            
    Ashoogte_offshore = Sensitivity.loc['Hubheight_offshore'].tolist()
    # Blade mass for each condition using market shares from input data - Sensitivity
    blade_mass  =     Sensitivity.loc['Blade mass'].tolist()+Sensitivity.loc\
    ['Blade mass'].tolist()             
    # CF share in blades for each condition using market shares from input data - Sensitivity                                        
    blade_CF  =       Sensitivity.loc['Blade_CF'].tolist()+Sensitivity.loc\
    ['Blade_CF'].tolist()     
    # GF share in blades for each condition using market shares from input data - Sensitivity                                                  
    blade_GF  =       Sensitivity.loc['Blade_GF'].tolist()+Sensitivity.loc\
    ['Blade_GF'].tolist()                             
    # Tower type for each condition using market shares from input data - Sensitivity                          
    Tower_type_on=   Sensitivity.loc['Towertype_onshore'].tolist()              
    Tower_type_off =   Sensitivity.loc['Towertype_offshore'].tolist()           
    Composite_tower =  [0,0,1,1]

    # Assign Generator types
    f = f.assign(AG=np.select(conditions_dev,AG_onshore+AG_offshore,default= 0))
    f = f.assign(MSPMG = np.select(conditions_dev, MSPMG_onshore+MSPMG_offshore\
    , default = 0))
    f = f.assign(HSPMG = np.select(conditions_dev, HSPMG_onshore+HSPMG_offshore\
    , default = 0))
    f = f.assign(DDPMG = np.select(conditions_dev, DDPMG_onshore+DDPMG_offshore\
    , default = 0))
    f = f.assign(EESG = np.select(conditions_dev, EESG_onshore+EESG_offshore,\
    default = 0))
    f = f.assign(HTS = np.select(conditions_dev, HTS_onshore+HTS_offshore,\
    default = 0))
    # Assign avearge hub height
    f = f.assign(Ashoogte = np.select(conditions_dev, Ashoogte_onshore+\
    Ashoogte_offshore, default = 80))                
    # Assign blade mass                           
    f = f.assign(blade_mass=np.select(conditions_dev,blade_mass,default = 13)) 
    # Assign blade CF content 
    f = f.assign(blade_CF = np.select(conditions_dev, blade_CF, default = 0.06))
    # Assign blade GF content
    f = f.assign(blade_GF = np.select(conditions_dev, blade_GF,default = 0.544))
    # Assign tower type
    f = f.assign(Tower_share = np.select(conditions_dev, Tower_type_on+\
    Tower_type_off, default = 1))            
    #Composite tower                                   
    f = f.assign(TowerC_share = np.select(conditions_dev, 2*Composite_tower, \
    default = 0))               
     # Assign gearbox use                                                
    f = f.assign(gearbox = np.select(conditions_dev, geared_onshore+\
    geared_offshore, default = 0))        
    # Join historic and future dataframes                                     
    t = pd.concat([t,f],ignore_index=True, sort=True)      
    # Set conditions wind turbine type based on technology analysis for rated cap an lifetime                     
    conditions_dev = [
    (t['Startdatum']>=2020)&(t['Startdatum']< 2025)&(t['Provincie']=='Onshore'),
    (t['Startdatum']>=2025)&(t['Startdatum']< 2030)&(t['Provincie']=='Onshore'),
    (t['Startdatum']>=2030)&(t['Startdatum']< 2040)&(t['Provincie']=='Onshore'),
    (t['Startdatum']>=2040)&(t['Startdatum']<=2050)&(t['Provincie']=='Onshore'),
    (t['Startdatum']>=2020)&(t['Startdatum']< 2025)&(t['Provincie']=='Offshore'),
    (t['Startdatum']>=2025)&(t['Startdatum']< 2030)&(t['Provincie']=='Offshore'),
    (t['Startdatum']>=2030)&(t['Startdatum']< 2040)&(t['Provincie']=='Offshore'),
    (t['Startdatum']>=2040)&(t['Startdatum']<=2050)&(t['Provincie']=='Offshore')]
    # Average rated capacity for each condition from input data - Sensitivity
    rated_cap_on  = Sensitivity.loc['Rated_cap_onshore'].tolist()               
    rated_cap_off = Sensitivity.loc['Rated_cap_offshore'].tolist()  
    # Mean liftime for each condition from input data - Sensitivity            
    lt_onshore    = Sensitivity.loc['Lifetime_onshore'].tolist()                
    lt_offshore   = Sensitivity.loc['Lifetime_offshore'].tolist()    
    # Assign average rated capacity     
    t = t.assign(rated_cap = np.select(conditions_dev, rated_cap_on+\
    rated_cap_off, default = t["Capacity"]))  
    # Set conditions for number of turbines based on rated capacity and total insatlled capacity                                  
    conditions_number_t  = [
    (t['Startdatum']>= 2020) & (t['Provincie'] == 'Offshore'),
    (t['Startdatum']>= 2020) & (t['Provincie'] != 'Offshore'),
    (t['Startdatum']<= 2020)]                     
    # Calculate number of turbines                              
    number_t = [t['Capacity']/10,t["Capacity"]/5,1]             
    # Assign number of turbines                
    t=t.assign(number_t=np.select(conditions_number_t,number_t,default = 1))  
    # Assign lifetimes  
    t=t.assign(lt=np.select(conditions_dev,lt_onshore+lt_offshore,default = 18))
    # Calculations for material compositions based on previously determined wind turbine types
    # and equations described in report appendix: Material compositions 
    #### Material compositions                                                  
    ### Nacelle                                                                 
  #   Yaw system (linear, rated capacity)
    t['yaw_steel'] = Mat_comp.loc['Yaw_steel','P'] *t['Capacity']
    t['yaw_iron'] = Mat_comp.loc['Yaw_iron','P'] *t['Capacity']
    t['yaw_copper'] = Mat_comp.loc['Yaw_copper','P'] * t['Capacity']
  #   Mechanical brake

  #   Transformer (linear, rated capacity)
  #### disctinction transformer steel and iron ####
    t['transformer_iron'] = Mat_comp.loc['Transformer_iron','P']*t['Capacity']
    t['transformer_copper']=Mat_comp.loc['Transformer_copper','P']*t['Capacity']
    t['transformer_al'] = Mat_comp.loc['Transformer_al','P'] *t['Capacity']
  ##  Structure
  #   Bedplate (linear, rated capacity)
    t['bedplate_iron'] = Mat_comp.loc['Bedplate_iron','P'] *t['Capacity']
  #   Cover (linear, rated capacity)
    t['cover_GFRP'] = Mat_comp.loc['Cover_GFRP','P'] *t['Capacity']
    t['cover_GF'] = Mat_comp.loc['Cover_GF','P'] *t['Capacity']
    t['cover_resin'] = Mat_comp.loc['Cover_resin','P'] *t['Capacity']
    
  ##  Drivetrain
  #   Low speed shaft (linear, rated capacity)
    t['shaft_steel'] =Mat_comp.loc['Shaft_steel','P'] *t['Capacity']
  #   Generator (Non-linear, rated capacity)
    t['generator_cast_iron'] = t['number_t']*(t['AG']*(Mat_comp.loc['AG_iron',\
    'P2']*t['rated_cap']**2+Mat_comp.loc['AG_iron','P']*t['rated_cap'])+t[\
    'HSPMG']*(0.125*Mat_comp.loc['DDPMG_iron','P2']*t['rated_cap']**2+0.125*\
    Mat_comp.loc['DDPMG_iron','P'])+t['MSPMG']*(0.25*Mat_comp.loc['DDPMG_iron',\
    'P2']*t['rated_cap']**2+0.25*Mat_comp.loc['DDPMG_iron','P']*t['rated_cap'])\
    +t['DDPMG']*(Mat_comp.loc['DDPMG_iron','P2']*t['rated_cap']**2+Mat_comp.loc\
    ['DDPMG_iron','P']*t['rated_cap'])+t['EESG']*(Mat_comp.loc['EESG_iron','P2'\
    ]*t['rated_cap']**2+Mat_comp.loc['EESG_iron','P']*t['rated_cap']))
    
    t['generator_copper'] = t['number_t']*(t['AG']*(Mat_comp.loc['AG_copper',\
    'P']*t['rated_cap'])+t['HSPMG']*(0.125*Mat_comp.loc['DDPMG_copper','P2']*t[\
    'rated_cap']**2+0.125*Mat_comp.loc['DDPMG_copper','P'])+t['MSPMG']*(0.25*\
    Mat_comp.loc['DDPMG_copper','P2']*t['rated_cap']**2+0.25*Mat_comp.loc[\
    'DDPMG_copper','P']*t['rated_cap'])+t['DDPMG']*(Mat_comp.loc['DDPMG_copper'\
    ,'P2']*t['rated_cap']**2+Mat_comp.loc['DDPMG_copper','P']*t['rated_cap'])+\
    t['EESG']*(Mat_comp.loc['EESG_copper','P2']*t['rated_cap']**2+Mat_comp.loc[\
    'EESG_copper','P']*t['rated_cap']))
    
    t['generator_NdFeB'] = t['number_t']*(t['HSPMG']*(0.125*Mat_comp.loc[\
    'DDPMG_magnet','P2']*t['rated_cap']**2+0.125*Mat_comp.loc['DDPMG_magnet',\
    'P']*t['rated_cap'])+t['MSPMG']*(0.25*Mat_comp.loc['DDPMG_magnet','P2']*t[\
    'rated_cap']**2+0.25*Mat_comp.loc['DDPMG_magnet','P']*t['rated_cap'])+t[\
    'DDPMG']*(Mat_comp.loc['DDPMG_magnet','P2']*t['rated_cap']**2+Mat_comp.loc[\
    'DDPMG_magnet','P']*t['rated_cap']))   

    t['generator_Yt'] = t['HTS']*0.0003*t['Capacity']
  #   Gearbox
    t['gearbox_iron']=Mat_comp.loc['Gearbox_iron','P']*t['Capacity']*t['gearbox']
    t['gearbox_steel']=Mat_comp.loc['Gearbox_steel','P']*t['Capacity']*t['gearbox']

  ##  Rotor
  #   Pitch system (linear, rated capacity)
    t['pitch_steel'] = Mat_comp.loc['Pitch_steel','P'] *t['Capacity']
    t['pitch_iron'] = Mat_comp.loc['Pitch_iron','P'] *t['Capacity']
    t['pitch_copper'] = Mat_comp.loc['Pitch_copper','P'] *t['Capacity']
  #   Nose cone (linear, rated capacity)
    t['nose_cone_GFRP'] = Mat_comp.loc['Nosecone_GFRP','P'] *t['Capacity']
    t['nose_cone_GF'] =  Mat_comp.loc['Nosecone_GF','P']  *t['Capacity']
    t['nose_cone_resin'] =  Mat_comp.loc['Nosecone_resin','P']  *t['Capacity']
    t['nose_cone_steel'] =  Mat_comp.loc['Nosecone_steel','P']  *t['Capacity']    
  #   Hub (linear, rated capacity)
    t['hub_iron'] = t['number_t']* Mat_comp.loc['Hub_iron','P'] *t['rated_cap']
  #   Blades (linear, rated capacity)
    t['Blades'] = t['blade_mass']*t['Capacity']
    t['Blades_GF'] = t['blade_GF']* t['blade_mass']*t['Capacity']
    t['Blades_CF'] = t['blade_CF']* t['blade_mass']*t['Capacity']
    t['Blades_fibre'] = Mat_comp.loc['Blade_fibre','share']* t['Blades']
    t['Blades_resin'] = Mat_comp.loc['Blade_resin','share']* t['Blades']
    t['Blades_steel'] = Mat_comp.loc['Blade_steel','share']* t['Blades']
    t['Blades_copper'] = Mat_comp.loc['Blade_copper','share']* t['Blades']
    t['Blades_balsa'] = Mat_comp.loc['Blade_balsa','share']* t['Blades']
    t['Blades_PVC'] = Mat_comp.loc['Blade_PVC','share']* t['Blades']
    t['Blades_FRP'] = t['Blades_fibre']+t['Blades_resin']
  ### Tower (Non-linear (steel) and linear (hybrid), hub height)
    t.loc[t['tower_type'] ==  'steel', 'Tower_share'] = 1
    t.loc[t['tower_type'] ==  'concrete', 'Tower_share'] = 0
    t.loc[t['Provincie'] != 0, 'tower_steel'] = t['Tower_share']*(t['number_t']\
    *(Mat_comp.loc['Tower_steel','H2']*(t['Ashoogte'])**2+Mat_comp.loc[\
    'Tower_steel','H'] *t['Ashoogte'])+ Mat_comp.loc['Tower_steel','Offset'])+\
    (1-t['Tower_share'])*(t['number_t']*(Mat_comp.loc['Towerhybrid_steel','H']\
    *t['Ashoogte']))
    t['tower_concrete'] = (1-t['Tower_share'])*(t['number_t']*( Mat_comp.loc[\
    'Towerhybrid_concrete','H'] *t['Ashoogte']))
  # Power cable (linear, hub height)
    t['cable_copper']=t['number_t']*(Mat_comp.loc['Cable_copper','H']*\
    (t['Ashoogte']))
    t['cable_aluminium'] = t['number_t']*( Mat_comp.loc['Cable_alu','H']*\
    (t['Ashoogte']))
  ### Foundation
  ##  Onshore   (Concrete) (based on total wind turbine weight)
    t.loc[t['Provincie'] !=  'Offshore', 'foundation_concrete'] = t['number_t']\
    *t['Tower_share']*( Mat_comp.loc['Foundationsteeltower_concrete','share'] *\
    ( Mat_comp.loc['Foundationsteeltower_concrete','P'] *t['rated_cap']+(t[\
    'tower_steel']/t['number_t'])))+t['number_t']*(1-t['Tower_share'])*(\
    Mat_comp.loc['Foundationhybridtower_concrete','share']*(Mat_comp.loc[\
    'Foundationhybridtower_concrete','P']*t['rated_cap']+(t['tower_concrete']/t\
    ['number_t']))) 
    t.loc[t['Provincie'] !=  'Offshore', 'foundation_steel'] = t['number_t']*t[\
    'Tower_share']*( Mat_comp.loc['Foundationsteeltower_steel','share'] *(\
    Mat_comp.loc['Foundationsteeltower_steel','P'] *t['rated_cap']+(t[\
    'tower_steel']/t['number_t'])))+t['number_t']*(1-t['Tower_share'])*(\
    Mat_comp.loc['Foundationhybridtower_steel','share']*(Mat_comp.loc[\
    'Foundationhybridtower_steel','P']*t['rated_cap']+(t['tower_concrete']/t[\
    'number_t']))) 
  ##  Offshore  (Monopile)
  #   Monopile (MP) (average weight per turbine)
    t.loc[t['Provincie']=='Offshore','monopile_steel']=t['number_t']*\
    Mat_comp.loc['Monopile_steel','Per unit'] 
  #   Transition piece (TP) (average weight per turbine)
    t.loc[t['Provincie']=='Offshore','transitionpiece_steel']=t['number_t']*\
    Mat_comp.loc['Transitionpiece_steel','Per unit'] 

  # composite tower
    t['tower_composite']= t['TowerC_share']*(t['number_t']*(Mat_comp.loc\
    ['Tower_steel','H2']*(t['Ashoogte'])**2+Mat_comp.loc['Tower_steel','H']*\
    t['Ashoogte'])+ Mat_comp.loc['Tower_steel','Offset'])*0.5
  # Save offshore and onshore data to list
    l.append(t)                                                                 
  # Retrieve data from loop (saved in list)
  offshore_inflows = l[0]                                                      
  onshore_inflows = l[1]
  # Determine criteria for data aggregation, summing all material flows
  l = {
  'Startdatum':'first','Capacity':'sum','Provincie':'first','lt':'mean',       \
  'Ashoogte':'mean','number_t':'sum','rated_cap':'mean','Tower_share':'mean',  \
  'AG':'mean','HSPMG':'mean','MSPMG':'mean','DDPMG':'mean','EESG':'mean',      \
  'HTS':'mean','gearbox':'mean',                                               \
  'yaw_iron':'sum','yaw_steel':'sum','yaw_copper':'sum','pitch_steel':'sum',   \
  'pitch_iron':'sum','pitch_copper':'sum','transformer_iron':'sum',            \
  'transformer_copper':'sum','transformer_al':'sum','bedplate_iron':'sum',     \
  'cover_GFRP':'sum','cover_GF':'sum','cover_resin':'sum','shaft_steel':'sum', \
  'generator_cast_iron':'sum','generator_copper':'sum','generator_NdFeB':'sum',\
  'gearbox_iron':'sum','gearbox_steel':'sum','nose_cone_GFRP':'sum',           \
  'nose_cone_GF':'sum','nose_cone_resin':'sum','nose_cone_steel':'sum',        \
  'hub_iron':'sum','Blades':'sum','Blades_fibre':'sum','Blades_GF':'sum',      \
  'Blades_CF':'sum','Blades_resin':'sum','Blades_steel':'sum','Blades_FRP':'sum',\
  'Blades_copper':'sum', 'Blades_balsa':'sum','Blades_PVC':'sum',              \
  'tower_steel':'sum','tower_concrete':'sum','cable_copper':'sum',             \
  'cable_aluminium':'sum','foundation_concrete':'sum','foundation_steel':'sum',\
  'monopile_steel':'sum','transitionpiece_steel':'sum', 'generator_Yt' : 'sum',\
   'tower_composite':'sum'}                                                     

  # Aggregate data
  off_light = offshore_inflows.groupby(['Startdatum']).agg(l)                   
  on_light = onshore_inflows.groupby(['Startdatum']).agg(l) 
  # Create excel file for material inflows for each scenario
  with pd.ExcelWriter('Material_inflows-{0}-scenario.xlsx'.format(name))\
  as writer:                                                                    
    on_light.to_excel(writer, sheet_name='Onshore')
    off_light.to_excel(writer, sheet_name='Offshore')
 # Define single timeseries
Time = on_light['Startdatum'].values.tolist()   


#%% 4. Dynamic stock model

#Import scenario data
low_on  =pd.read_excel(r'Material_inflows-low-scenario.xlsx' ,sheet_name='Onshore') 
low_off =pd.read_excel(r'Material_inflows-low-scenario.xlsx' ,sheet_name='Offshore')
mid_on  =pd.read_excel(r'Material_inflows-mid-scenario.xlsx' ,sheet_name='Onshore')  
mid_off =pd.read_excel(r'Material_inflows-mid-scenario.xlsx' ,sheet_name='Offshore') 
high_on =pd.read_excel(r'Material_inflows-high-scenario.xlsx',sheet_name='Onshore')  
high_off=pd.read_excel(r'Material_inflows-high-scenario.xlsx',sheet_name='Offshore') 
print('Estimated runtime ~10 mins')
# Loop over scenarios
for inflow_on,inflow_off,excel in zip([low_on, mid_on, high_on],[low_off,\
mid_off, high_off],['low','mid','high']):                                       
  on_light = inflow_on # Name inflow data (varies per scenario)                                                         
  off_light = inflow_off
  # Create dataframe for onshore DSM results (indexed by time)
  onshore_DSM_df = pd.DataFrame({'Time': Time})
  # Determine which columns (materials and capacity) to use                                 
  keys = ['Capacity', 'number_t']+list(on_light.columns)[14:]    
  # For each material (and capacity) run DSM               
  for  a in keys:                                                               
    Lifetime={'Type':'Normal','Mean':on_light['lt'].values.tolist(),\
    'StdDev':np.array([4]) }
    name = '{0}_DSM'.format(a)
    name=DynamicStockModel(t=Time,i=on_light[a].values.tolist(),lt = Lifetime)
    CheckStr = name.dimension_check()
    Stock_by_cohort_cap = name.compute_s_c_inflow_driven()
    S_cap  = name.compute_stock_total()
    O_C_cap = name.compute_o_c_from_s_c()
    O_cap   = name.compute_outflow_total()
    DS_cap  = name.compute_stock_change()
    # Save stock, inflow, outflow results to onshore DSM dataframe
    onshore_DSM_df[a+'_stock']=name.s                                           
    onshore_DSM_df[a+' inflow']=name.i                                          
    onshore_DSM_df[a+' outflow']=name.o                                         
  # Create dataframe for offshore DSM results (indexed by time)
  offshore_DSM_df = pd.DataFrame({'Time': Time})              
  # Determine which columns (materials and capacity) to use                  
  keys = ['Capacity', 'number_t']+list(off_light.columns)[14:]   
  # For each material (and capacity) run DSM                           
  for  a in keys:                                                               
    Lifetime = {'Type': 'Normal', 'Mean': off_light['lt'].values.tolist(),\
    'StdDev': np.array([4]) }
    name = '{0}_DSM'.format(a)
    name=DynamicStockModel(t=Time,i=off_light[a].values.tolist(),lt = Lifetime)
    CheckStr = name.dimension_check()
    Stock_by_cohort_cap = name.compute_s_c_inflow_driven()
    S_cap  = name.compute_stock_total()
    O_C_cap = name.compute_o_c_from_s_c()
    O_cap   = name.compute_outflow_total()
    DS_cap  = name.compute_stock_change()
    # Save stock, inflow, outflow results to offshore DSM dataframe
    offshore_DSM_df[a+'_stock']=name.s                                          
    offshore_DSM_df[a+' inflow']=name.i                                         
    offshore_DSM_df[a+' outflow']=name.o                                        
  # Add results from onshore and offshore for total material flows
  total_DSM_df = onshore_DSM_df.add(offshore_DSM_df, fill_value=0)
  # Write data to Excel file for each scenario              
  with pd.ExcelWriter('in-out-stock-{0}-scenario.xlsx'.format(excel)) as writer:
    onshore_DSM_df.to_excel(writer, sheet_name='Onshore')
    offshore_DSM_df.to_excel(writer, sheet_name='Offshore')
    total_DSM_df.to_excel(writer, sheet_name='Total')
    # Print progress calculations (each scenario)
    print('{0} scenario finshed calculating'.format(excel))                                              
