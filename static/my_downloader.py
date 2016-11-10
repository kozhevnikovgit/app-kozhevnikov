# coding: utf-8
import urllib
import tarfile
import zipfile
import shutil
import console
import os

name = 'favicon.ico'

def download():
		print 'Downloading'
		url = 'http://iconbird.com/ico/download.php?id=44063&s=128'
		urllib.urlretrieve(url, name)
		print 'Download Complete'

def extract():
		print 'Extracting...'
		t = tarfile.open(name)
		t.extractall()
		print 'Package extracted'
		
download()
#extract()
