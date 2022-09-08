#!/bin/sh

if [ $# -eq 1 ]
then
    curl -k -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text='"${1// /%20}"\&per_page\=20\&search_field\=name''  | jq '.' > hh.json
else
    echo "Enter: ./hh.sh 'data scientist'"
fi