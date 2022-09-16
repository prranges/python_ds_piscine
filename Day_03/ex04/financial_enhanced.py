# !prranges/bin/python3.10

import sys
import httpx
from bs4 import BeautifulSoup
import cProfile
import pstats

def beautiful(argv):
    if len(sys.argv) != 3:
        raise Exception("Argument error. Usage: ./financial.py '<ticker>' '<requested field>'")
    else:
        url = f'https://finance.yahoo.com/quote/{argv[1]}/financials'
        r = httpx.get(url, headers={'User-Agent': ''})
        soup = BeautifulSoup(r.text, 'html.parser')
        if soup.title.string == 'Symbol Lookup from Yahoo Finance':
            raise Exception('Wrong ticker')
        tags = soup.find_all(attrs={'data-test': 'fin-row'})
        breakdowns = [tag.find(class_='Va(m)').get_text() for tag in tags]
        if sys.argv[2] not in breakdowns:
            raise Exception('Not found breakdown')
        return tuple(t.get_text() for t in tags[breakdowns.index(sys.argv[2])].find_all('span'))
        
def main():
    try:
        print(beautiful(sys.argv))
    except Exception as e:
        print(e, file=sys.stderr)
    

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(5)
    

# ./financial.py 'MSFT' 'Total Revenue'
# ('Total Revenue', '134,249,000', '125,843,000', '110,360,000', '89,950,000', '85,320,000')
 