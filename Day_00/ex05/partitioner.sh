#!/bin/sh

IN=../ex03/hh_positions.csv
OUT=hh_positions_
HEADER=$(head -n 1 $IN)

tail -n +2 $IN |
awk -F '",' ' 
  { date = substr($2,2,10) }
  !(date in outfile) { outfile[date] = "'$OUT'" (date) ".csv";
  printf "\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"\n", '$HEADER' >  outfile[date]}
  { print > outfile[date] }
'