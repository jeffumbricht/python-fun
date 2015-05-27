#!/usr/bin/env python

from __future__ import with_statement
from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED
import argparse
import os
import time
import re

def main():
	
	print('\n\n  /\_/\\\n=( °w° )=\n  )   (  //\n (__ __)//\n\n')
	print('NOTES:')
	print('zips html, js, css, image types, xml, mp3, swf, and LMS file ext')
	print('does not zip files that start with _')
	print('does not zip files in folders inside graphics folder')
	print('example: trunk/content/graphics/FOLDER/asset.gif\n\n')
	
	# initiate parser and add args
	parser = argparse.ArgumentParser()

	parser.add_argument('-zv', '--ZipVersion', default='1', help='Zip version number. Default: 1')
	parser.add_argument('-bd', '--BaseDir', default='trunk', help='Base Directory. Default: trunk')
	parser.add_argument('-bn', '--BranchName', default='shell', help='Branch or Module Name. Default: shell')

	args = parser.parse_args()
	args_dict = vars(args)

	assert os.path.isdir(args_dict['BaseDir'])

	# get date
	mydate = time.strftime("%y%m%d")

	# grab the beta version from index
	archivename = args_dict['BranchName']+ '_' + mydate + '_v' + args_dict['ZipVersion'] + '.zip'

	# acceptable extentions
	ext = ['.html','.js','.css','.jpg','.jpeg','.gif','.png','.xml','.mp3','.swf','.au','.crs','.cst','.des']

	# regex to check for folder inside graphics folder
	graphicsdoubleregex = r'graphics\\.+\\'

	# start making a zip
	with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:
		for root, dirs, files in os.walk(args_dict['BaseDir']):
			
			#NOTE: ignore empty directories
			for fn in files:
				# get the absolute path
				absfn = os.path.join(root, fn)

				# Must end with OK ext and not start with _ and not be a folder inside graphics
				if (fn.endswith(tuple(ext)) 
					and not fn.startswith('_') 
					and not re.search(graphicsdoubleregex, absfn)):

					# feed to zip
					zfn = absfn[len(args_dict['BaseDir'])+len(os.sep)-1:] #XXX: relative path
					z.write(absfn, zfn)

	print('zip complete: ' + archivename);
	
if __name__ == '__main__':
	main()