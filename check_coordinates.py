import numpy as np
import pandas as pd
import xarray as xr

### Generate years and months
years = np.arange(1973,2022,1).astype(str)
months = np.arange(1,13,1).astype(str)
for i in range(0,10):
    months[i] = months[i].zfill(2)

### Lopp through years and months    
for year in years:
    for month in months:
        ### Open file
        ds = xr.open_dataset('AT-Neu/tp_era5-land_oper_sfc_'+year+month+'.nc')
        ### Check if right latitude
        if ds.latitude.values != 47.099998474121094:
            print('wrong latitude')
         ### Check if right longitude
        if ds.longitude.values != 11.300000190734863:
            print('wrong longitude')
        ### Check if right year
        for i in range(0,len(ds.time.dt.year.values)):
            if str(ds.time.dt.year.values[i]) != year:
                print('wrong year')
