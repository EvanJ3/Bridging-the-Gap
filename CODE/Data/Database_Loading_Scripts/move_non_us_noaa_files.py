import os

# https://www.ncdc.noaa.gov/cdo-web/datasets
# this is a simple script used to move non-US NOAA monthly summary station files to a "to_delete" directory for easy deletion

base_dir = "/Volumes/Apollo/Monthly_Weather/"
file_list = os.listdir(base_dir)
file_list.remove("to_delete")

for file in file_list:

    if file[:2] != 'US':
        os.rename(base_dir + file, base_dir + "to_delete/" + file)