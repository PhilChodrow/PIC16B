import pandas as pd
import numpy as np
import os 
# ---------
# clean and store raw temp data
# ---------

path = "datasets/noaa-ghcn/ghcnm.tavg.v4.0.1.20210218.qcf.dat"

colnames = ["ID", "Year", "Element"]

colspecs = [(0,11),(11, 15),(15, 19)]

headers = ["VALUE", "DMFLAG", "QCFLAG", "DSFLAG"]

i = 19
j = 24

for month in range(12):
    for header in headers:
        colnames.append(f"{header}{month+1}")

    spacer = 19 + month*8
    colspecs.append((spacer, spacer + 5))
    colspecs.append((spacer + 5, spacer + 6))
    colspecs.append((spacer + 6, spacer + 7))
    colspecs.append((spacer + 7, spacer + 8))

df = pd.read_fwf(path, 
                 colspecs = colspecs,
                 names = colnames)


keepnames = [name for name in df.columns if (name in ["ID", "Year"]) or "VALUE" in name]
df = df[keepnames]
df = df[df["Year"] > 1900]

df.replace(-9999, np.nan)

import os
if not os.path.exists('datasets/noaa-ghcn/decades'):
    os.makedirs('datasets/noaa-ghcn/decades')

for i in range(12):
    begin = 1901 + i*10
    end   = begin + 9
    sub = df[(df["Year"] >= begin) & (df["Year"] <= end)]
    path = f"datasets/noaa-ghcn/decades/{begin}-{end}.csv"
    sub.to_csv(path, index = False)


# ---------
# clean and store metadata
# ---------

path = "datasets/noaa-ghcn/ghcnm.tavg.v4.0.1.20210218.qcf.inv"
colspecs = [(0, 11), (12, 20), (21, 30), (31, 37), (38, 68)]
colnames = ["ID", "LATITUDE", "LONGITUDE", "STNELEV", "NAME"]

df = pd.read_fwf(path, 
                 colspecs = colspecs,
                 names = colnames)

df.to_csv("datasets/noaa-ghcn/station-metadata.csv", )