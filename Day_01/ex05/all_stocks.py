import sys

def find_stock(arg):
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
    
    if arg.capitalize() in COMPANIES:
        print(f'{arg.capitalize()} stock price is {STOCKS[COMPANIES[arg.capitalize()]]}')
    elif arg.upper() in STOCKS:
        for c in COMPANIES:
            if COMPANIES[c] == arg.upper(): print(f'{arg.upper()} is a ticker symbol for {c}')
    else:
        print(f'{arg} is an unknown company or an unknown ticker symbol')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        arg_list = sys.argv[1].split(',')
        for arg in arg_list:
            if arg.strip() == "": exit()
        for arg in arg_list:
            find_stock(arg.strip())