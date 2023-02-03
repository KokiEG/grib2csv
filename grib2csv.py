import xarray as xr
import rioxarray
import pandas as pd
import geopandas as gpd
import glob
import numpy as np
from shapely import wkt
from shapely.geometry import mapping
import pandas as pd
import datetime as dt
import os
import sys

class Tenkai:
    def __init__(self, path_shp, path_read, path_save, date_list):
        self.path_shp = path_shp
        self.path_read = path_read
        self.path_save = path_save
        self.date_list = date_list

    def run(self):
        gdf = gpd.read_file(path_shp)
        for tgt_date in date_list:
            print('Now loding file：',tgt_date)
            ##任意の日付のファイル名の場所にあるbinファイルをncファイルに変換するバッチファイルを呼び出す
            cmd_file = "test_grib2nc.bat"   # .batファイルへのパス
            command = cmd_file + " " + tgt_date
            os.system(command)
            ##ncファイルが重いので一つ一つcsvファイルに変換した後にそのNCファイルを消す
            ##ncファイルを境界線でクリップした後csvファイルにする
            print('Now loding file：',tgt_date)
            fs = glob.glob(path_read+'{}/*.nc'.format(tgt_date))
            dss = []
            for f in fs:
                ds = xr.open_dataset(f)
                d = ds.rio.write_crs('epsg:6668', inplace=True)
                dsp = ds.rio.clip(gdf.geometry.apply(mapping))
                dss.append(dsp)
                ds.close()
            dsAll = xr.concat(dss, dim='time')
            s = dsAll.attrs
            s['crs'] = '+init=epsg:' + str(6668)
            dsAll.attrs = s
            time = dsAll['time'].values
            s = pd.Series(time)
            s = s.dt.tz_localize('UTC') 
            s = s.dt.tz_convert('Asia/Tokyo')
            s = s.dt.tz_localize(None)
            dsAll['time'] = s.values
            df = dsAll.to_dataframe()
            df.to_csv('path_save' + '{}.csv'.format(tgt_date))
            ##ここで読み込んでいたNCファイルを削除する
            for f in fs:
                os.remove(f)

if __name__ == '__main__':
    path_shp = sys.argv[1]
    path_read = sys.argv[2]
    path_save = sys.argv[3]
    date_list = sys.argv[4:]

    tenkai = Tenkai(path_shp, path_read, path_save, date_list)
    tenkai.run()
