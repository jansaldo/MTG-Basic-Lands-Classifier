import os
import subprocess
from requests import get


def main():
    # Dropbox URL
    url = 'https://www.dropbox.com/s/d7i5tdnf8le44h1/model.zip?dl=1'

    # Download the file
    print('Downloading file...')
    downloaded_file = get(url)
    with open('../model.zip', 'wb') as out_file:
        out_file.write(downloaded_file.content)

    # Unzip
    subprocess.run('unzip -o ../model.zip -d ../', shell=True)
    
    # Remove zipfile
    print('Deleting file...')
    os.remove('../model.zip')
    print('Done!')


if __name__ == '__main__':
    main()
