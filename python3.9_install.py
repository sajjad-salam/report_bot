import wget

# Specify the URL for downloading Python 3.9 for Windows
url = 'https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe'

# Specify the local path where the file will be saved
local_path = 'python-3.9.9-amd64.exe'

# Download Python 3.9 installer for Windows
wget.download(url, local_path)