#!/usr/bin/env python
import os
import re
import argparse

def main():
	# parser = argparse.ArgumentParser()
	# parser.add_argument('-js', '--JavaScriptFolder', default='scripts', help='Name of JavaScript folder')

	# args = parser.parse_args()
	# args_dict = vars(args)

	# reportJsFiles(args_dict['JavaScriptFolder'])

	reportSassImports()

def reportSassImports():
	sassregex = r'_.+\.scss$'
	importregex = r'@import '
	sassfiles = []
	usedsassfiles = []

	# go through all _sass files names and see if there is a matching import in main.scss
	for root, dirs, files in os.walk('sass'):
		for file in files:
			if re.search(sassregex, file):
				# remove ext and _
				sassfiles.append(file)
				# print(file[1:-5])

	print("sassfiles len: " + str(len(sassfiles)))

	fopen = open("sass/main.scss")
	lines = fopen.read()
	# print(lines)
	print("------------Used Sass files")
	for sassfile in sassfiles:
		# '@import 'reset';
		if re.search(r'@import [\"\']' + re.escape(sassfile[1:-5]), lines):
			usedsassfiles.append(sassfile)
			print(sassfile)

	print("------------Unused Sass files")
	for sassfile in sassfiles:
		if sassfile not in usedsassfiles:
			print(sassfile)

def reportJsFiles(folder):
	print('going through dir : ' + folder)
	

	jsfiles = []
	usedfiles = []

	htmlfiles = []
	htmlregex = r'.\.html'

	# go through and get all the html file paths
	for root, dirs, files in os.walk('.'):
		for file in files:
			if re.search(htmlregex, file):
				htmlfiles.append(os.path.join(root, file))

	# get all the script files
	for root, dirs, files in os.walk(folder):
		for file in files:
			# print(file)
			jsfiles.append(file)

	# go over the html files
	# read file, go over js files and see if file matches
	# if yes, check for jsfile in used files list and add if needed
	print("-----USED")
	for htmlfile in htmlfiles:
		fopen = open(htmlfile, 'r')
		lines = fopen.read()
		for jsfile in jsfiles:
			if lines.find(jsfile) > 0:
				# print(jsfile + " in " + htmlfile)
				if jsfile not in usedfiles:
					usedfiles.append(jsfile)
					print(jsfile)

	# print all the js files that are not in used files
	print("-----UNUSED")
	for jsfile in jsfiles:
		if jsfile not in usedfiles:
			print(jsfile)


	

if __name__ == '__main__':
		main()