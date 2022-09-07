import xarray as xr
import pandas as pd
import numpy as np

### ERA5-land is stored in zz93
pathwayIN = '/g/data/zz93/era5-land/reanalysis/'

### Information for site names, latitude and longitude
df_sites = pd.read_csv('sites.csv')

### Read in file
def readin_file(var,year,month):

    ### Very clunky sorry
    if month in ('01','03','05','07','08','10','12'):
        suffix = '31.nc'
    elif month in ('04','06','09','11'):
        suffix = '30.nc'
    elif month == '02':
        if year in ('1976', '1980', '1984', '1988', '1992', '1996', '2000',
                    '2004', '2008', '2012', '2016', '2020'):
            suffix = '29.nc'
        else:
            suffix = '28.nc'

    ### Filename
    fileIN = pathwayIN+var+'/'+year+'/'+var+'_era5-land_oper_sfc_'+year+month+'01-'+year+month+suffix
 
    ### Read in as xarray dataset. 
    ### Files have scale and offset factors: set mask_and_scale = True
    ds = xr.open_dataset(fileIN, mask_and_scale = True)

    return(ds)

def grab_site_data(var,year,month):

    ### Read in file
    ds = readin_file(var,year,month)

    ### Loop through all sites and write to separate netCDF
    for site,lat,lon in zip(df_sites.Site,df_sites.latitude,df_sites.longitude):
        ds_site = ds.sel(latitude=lat,longitude=lon,method='nearest')
        fileOUT = var+'/'+site+'/'+var+'_era5-land_oper_sfc_'+year+month+'.nc'
        
        ### variable name in file name doesn't match variable name in netCDF file 
        ### for temperature
        if var == 'tp':
            file_var = 'tp'
        elif var == '2t':
            file_var = 't2m'
            
        ds_site.to_netcdf(fileOUT,
                          encoding = {'time': {'dtype': 'double'},
                                      'latitude': {'dtype': 'double'},
                                      'longitude': {'dtype': 'double'},
                                      file_var: {'dtype': 'float32'}})

### Years
years = np.arange(1973,2022,1).astype(str)

### Months
months = np.arange(1,13,1).astype(str)

### Add leading zero
for i in range(0,10):
    months[i] = months[i].zfill(2)

'''
Either define variable, or add loop over variables
2t = 2m temperature
tp = total precipitation
'''

var = '2t'

### Loop through years and months
for year in years:
    for month in months:
        grab_site_data(var,year,month)
