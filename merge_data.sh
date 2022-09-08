#! /bin/bash

### Define variable
var='tp'

### Merge all data
for d in */ ; do
    cdo -L -b F64 mergetime "$d"* "$d"${var}_era5-land_oper_sfc_1973-2022.nc
done

### Clean up: Delete all files except merged 
find . \! -name ${var}'_era5-land_oper_sfc_1973-2022.nc' -delete
