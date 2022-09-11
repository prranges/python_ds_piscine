import sys

def find_stock(ticker):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    if ticker in STOCKS:
        for c in COMPANIES:
            if COMPANIES[c] == ticker: print(c, STOCKS[ticker])
    else:
        print('Unknown ticker')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_stock(sys.argv[1].upper())