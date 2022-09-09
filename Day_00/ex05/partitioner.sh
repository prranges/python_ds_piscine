#!/bin/sh

IN=../ex03/hh_positions.csv
OUT=hh_positions_
HEADER=(head -n 1 $IN)

# splitCsv() {
#     HEADER=$(head -1 $IN)
    
#     tail -n +2 $IN | split -l 2 - $OUT
#     n=1
#     for i in $OUT*; do
#         (echo $HEADER && cat $i) > hh_positions_${n}.csv && rm $i
#         ((n++))
#     done
# }
# splitCsv $IN

tail -n +2 $IN |
awk -F '",' ' 
  { date = substr($2,2,10) }
  !(date in outfile) { outfile[date] = "'$OUT'" (++numout) ".csv" }
#   { print > outfile[date] }
'

# awk -F '",' '/0/ { print substr($2,2,10) }' $IN > 1.ccc