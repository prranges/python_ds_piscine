import subprocess
import os


if __name__ == '__main__':

    try:
        if os.environ['VIRTUAL_ENV'][-8:] == 'prranges':
            subprocess.call('pip install beautifulsoup4 pytest', shell=True)
            subprocess.call('pip freeze > requirements.txt', shell=True)
            subprocess.call('zip prranges.zip -r prranges', shell=True)
    except KeyError:
        print('Wrong enviroment.')