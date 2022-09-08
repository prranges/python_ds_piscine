#!/bin/sh

head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv
awk -F  '",' '/0/ { 
    if (tolower($3) ~ "junior" )
        print $1 "\"", $2, "\"Junior\"", $4
    else if (tolower($3) ~ "middle" )
        print $1 "\"", $2,  "\"Middle\"", $4
    else if (tolower($3) ~ "senior" )
        print $1 "\"", $2,  "\"Senior\"", $4
    else if (tolower($3) ~ "junior" && tolower($3) ~ "senior" )
        print "\"Junior/Senior\"", $4
    else if (tolower($3) ~ "junior" && tolower($3) ~ "middle" )
        print $1 "\"", $2, "\"Junior/Middle\"", $4
    else if (tolower($3) ~ "middle" && tolower($3) ~ "senior" )
        print $1 "\"", $2, "\"Middle/Senior\"", $4
    else if (tolower($3) ~ "junior" && tolower($3) ~ "middle" && tolower($3) ~ "senior" )
        print $1 "\"", $2, "\"Junior/Middle/Senior\"", $4
    else
        print $1 "\"", $2, "\"-\"", $4
    }'  ../ex02/hh_sorted.csv | tr ' ' , >> hh_positions.csv