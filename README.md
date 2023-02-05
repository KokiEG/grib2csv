# grib2csv　気象庁提供のgrib2形式の大規模ファイルを任意の領域(shp)でclipした領域だけのデータをメモリ効率よくcsvファイルとして取り出すスクリプト
## 利用にはwgrid2をダウンロードする必要がある。公式サイト[Climate Prediction Center - wgrib2: grib2 utility](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/)からダウンロードしてインストールする必要がある。
## ①wgrid2.exeが存在するディレクトリの下に気象庁提供の土壌雨量指数などのデータが入っているバイナリファイルが入ったフォルダを置く
## ②grib2csv.pyを実行する。引数は path_shp, path_read, path_saveであり、それぞれ、クリップしたい領域のshpファイル、binファイルがあるフォルダのパス、csvを保存したいパスである。
