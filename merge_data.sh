#! /bin/bash

for d in */ ; do
    cdo -L -b F64 mergetime "$d"* "$d"2t_era5-land_oper_sfc_1973-2022.nc
done
