import numpy as np
import pandas as pd
import xarray as xr

'''
Checks if right coordinates and years were extracted. Latitudes and longitudes
were selected based on nearest match so I rounded values because they will not
exactly match
'''

def check_coordinates(var,site):
    ### Generate years
    years = np.arange(1973,2023,1).astype(str)
    
    ### Generatre months
    months = np.arange(1,13,1).astype(str)
    for i in range(0,10):
        months[i] = months[i].zfill(2)
    
    ### Read in site information
    df = pd.read_csv('sites.csv')
    
    ### Select site
    df = df[(df['Site'] == site)]
    
    ### Select values for latitude and longitude
    latitude = df['latitude'].values.tolist()[0]
    longitude = df['longitude'].values.tolist()[0]
    
    for year in years:
        for month in months:
            ### Open site data
            ds = xr.open_dataset(var+'/'+site+'/'+var+'_era5-land_oper_sfc_'+
                                 year+month+'.nc')

            ### Check if latitude in site data matches latitude in original csv
            if round(ds.latitude.values.tolist(),1) != round(latitude,1):
                print('wrong latitude')

            ### Check if longitude in site data matches longitude in original csv
            if round(ds.longitude.values.tolist(),1) != round(longitude,1):
                print('wrong longitude')

            ### Check if year in site data is correct
            for i in range(0,len(ds.time.dt.year.values)):
                if str(ds.time.dt.year.values[i]) != year:
                    print('wrong year')

### E.g. check if total precipitation in AT-Neu is ok. Returns nothing if ok           
check_coordinates('tp','AT-Neu')            
