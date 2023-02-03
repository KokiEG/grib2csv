@echo off
set PATH=../wgrib2;%PATH%
set "tgtdate=%~1"

for %%f in ("..\%tgtdate%\*ANAL_grib2.bin") do (
    wgrib2 "%%f" -netcdf "..\%tgtdate%\%%~nf.nc"
)