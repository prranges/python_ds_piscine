#!prranges/bin/python3.10

import sys
import pytest

import requests
from bs4 import BeautifulSoup

def soup(ticker, bd):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials'
    r = requests.get(url, headers={'User-Agent': ''})
    soup = BeautifulSoup(r.text, 'html.parser')
    if soup.title.string == 'Symbol Lookup from Yahoo Finance':
        raise ValueError('Wrong ticker')
    tags = soup.find_all(attrs={'data-test': 'fin-row'})
    breakdowns = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if bd not in breakdowns:
        raise ValueError('Not found breakdown')
    return tuple(t.get_text() for t in tags[breakdowns.index(bd)].find_all('span'))

def beautiful(argv):
    if len(argv) != 3 or isinstance(argv, list) == False:
        raise Exception("Argument error. Usage: ./financial.py '<ticker>' '<requested field>'")
    else:
        return soup(argv[1], argv[2])

def test_invalid_ticker():
    with pytest.raises(ValueError, match='Wrong ticker'):
        soup('QWERTY', 'Total Revenue')

def test_valid_ticker():
    soup('MSFT', 'Total Revenue')[0] == 'Total Revenue'

def test_invalid_breakdown():
    with pytest.raises(ValueError, match='Not found breakdown'):
        soup('MSFT', 'Total qwerty')

def test_return_type():
    assert isinstance(soup('MSFT', 'Total Revenue'), tuple)

def test_no_args():
    with pytest.raises(Exception, match="Argument error. Usage: ./financial.py '<ticker>' '<requested field>'"):
        beautiful('')

def test_args_wrong_format():
    with pytest.raises(Exception, match="Argument error. Usage: ./financial.py '<ticker>' '<requested field>'"):
        beautiful(('financial_test.py', 'MSFT', 'Total Revenue'))

def test_args_right_format():
    beautiful(['financial_test.py', 'MSFT', 'Total Revenue']) == "('Total Revenue', '198,270,000', '198,270,000', '168,088,000', '143,015,000', '125,843,000')"


if __name__ == '__main__':
    try:
        print(beautiful(sys.argv))
    except Exception as e:
        print(e, file=sys.stderr)

# ./financial.py 'MSFT' 'Total Revenue'
# ('Total Revenue', '134,249,000', '125,843,000', '110,360,000', '89,950,000', '85,320,000')
 