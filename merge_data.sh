#! /bin/bash

### Merge all data
for d in */ ; do
    cdo -L -b F64 mergetime "$d"* "$d"2t_era5-land_oper_sfc_1973-2022.nc
done

### Clean up: Only keep merged file
for d in */ ; do
    find . ! -name '"$d"2t_era5-land_oper_sfc_1973-2022.nc' -type f -exec rm -f {} +
done
