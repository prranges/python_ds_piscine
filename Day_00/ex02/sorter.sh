#!/bin/sh

(head -n 1 ../ex01/hh.csv && tail -n 20 ../ex01/hh.csv | sort -k2 -k1 -t,) > hh_sorted.csv