#!/bin/sh

IN=../ex03/hh_positions.csv
OUT=hh_uniq_positions.csv

echo '"name","count"' > $OUT

((printf '"Junior",' && grep -c Junior $IN) &&
(printf '"Middle",' && grep -c Middle $IN) &&
(printf '"Senior",' && grep -c Senior $IN)) | sort -k2nr -t, >> $OUT
