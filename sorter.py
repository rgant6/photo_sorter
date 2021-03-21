import os
import shutil
import glob
import os.path
from os import path
import datetime
from stat import *

def main():
	if(input("\nDoes your file path contain multiple folders of pictures?:\ny/n: ").lower() == 'y'):
		
		extractor(True)
		# if(str(path.exists(input("Enter the base directory for the photo sorter: ")))):
	global pathSet 
	pathSet = input("\nEnter the base directory for the photo sorter: ")
	sorter()

def extractor(firstTime):
	global pathSet 
	pathSet = input("\nEnter the base directory for the photo sorter: ")
	if(str(path.exists(pathSet))):
		dirFinder(pathSet)

	else:
		print("Incorrect File Path")
		extractor(firstTime)

def dirFinder(pathInput):
	# create a list of file and sub directories 
	# names in the given directory 
	listOfFile = os.listdir(pathInput)
	print("List: ",listOfFile)
	# Iterate over all the entries
	for entry in listOfFile:
		# Create full path
		fullPath = os.path.join(pathInput, entry)
		# If entry is a directory then get the list of files in this directory 
		if os.path.isdir(fullPath) and not(entry == ".DS_Store"):
			dirFinder(fullPath)
		elif entry == ".DS_Store":
			pass
		else:
			try:
				shutil.move(fullPath, pathSet)
			except:
				pass
			# print(os.path.join(directory, filename))

def sorter():

	filepaths = [os.path.join(pathSet, file) for file in os.listdir(pathSet)]
	file_statuses = [(os.stat(filepath), filepath) for filepath in filepaths]
	files = ((status[stat.ST_CTIME], filepath) for status, filepath in file_statuses if stat.S_ISREG(status[stat.ST_MODE]))
	
	for creation_time, filepath in sorted(files):
		creation_date = time.ctime(creation_time)
		year = datetime.date.creation_date.year
		print("year: ",year)

if __name__== "__main__":
   main()
