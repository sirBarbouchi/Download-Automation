import sys, subprocess
from data_transformation import transformation
from download_files import download
from unzip_file import unzip
from pathlib import Path

if __name__ == '__main__':
    path = str(Path.home() / "Downloads")
    # read and run "requirements.txt" file
    #subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "-r", "requirements.txt"])
    download()
    unzip(path)
    transformation()