# ERA5_Jon

Get site-level meteorology from ERA5. 

``` sites.csv``` has the site information

```grab_data.py``` is a python script that extracts the met data for each site

```check_coordinates.py``` checks whether the extracted data match the coordinates in the csv. E.g. run

```python check_coordinates.py --var 'tp' --site 'AT-Neu'```

to check whether coordinates for total precipitation in AT-Neu are ok 

```merge_data.sh``` merges the data per site along the time axis and cleans up 
