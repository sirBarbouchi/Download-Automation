import shutil         
import glob
import zipfile
import os
from pathlib import Path
from datetime import datetime

def unzip(path):
    """
    this function searches all downloaded files (TAXRATES_ZIP5.zip), select the last downloaded, copy it to the directory of the program, and unzip it
    """
    list_of_files = glob.glob(path+'/*')
    latest_file = max(list_of_files, key=os.path.getmtime)
    today = str(datetime.today().strftime('%Y%m%d'))
    Path(r"./"+ today +" Downloaded_files/").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(latest_file, r"./"+ today +" Downloaded_files/"+latest_file.split('\\')[-1])
   
    with zipfile.ZipFile(r"./"+ today +" Downloaded_files/"+latest_file.split('\\')[-1]) as zip_ref:
        zip_ref.extractall(r"./"+ today +" Downloaded_files/")
