#!/bin/sh

IN=../ex03/hh_positions.csv
OUT=all_in_one.csv
HEADER=$(head -n 1 $IN)

(echo $HEADER && awk 'FNR>1' hh_*.csv) > $OUT