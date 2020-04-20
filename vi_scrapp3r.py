#!/bin/python

import requests
import urllib
import os 
import sys

sys.tracebacklimit = 0

#Cool banner <3

print(""" __      ___    _____                           ____       
 \ \    / (_)  / ____|                         |___ \      
  \ \  / / _  | (___   ___ _ __ __ _ _ __  _ __  __) |_ __ 
   \ \/ / | |  \___ \ / __| '__/ _` | '_ \| '_ \|__ <| '__|
    \  /  | |  ____) | (__| | | (_| | |_) | |_) ___) | |   
     \/   |_| |_____/ \___|_|  \__,_| .__/| .__|____/|_|   
                                    | |   | |              
                                    |_|   |_|              

""" + 'Usage: Scrap.py <GR_Number>\n')



#label: run
def get():
	gr_num = sys.argv[1]
	url = "https://vierp.s3.ap-south-1.amazonaws.com/cloud/studentprofile/icard/photo/"+gr_num+"photo.jpg"
	r = requests.get(url)
	#print(r.url)
	if(r.status_code == 200):
		print ('  \033[1;32m[+]\033[0m Student Photo Exist !\n')
		image = urllib.request.urlopen(url)
		
		DIR = ("Images")
		CHECK_FOLDER = os.path.isdir(DIR)

		if not CHECK_FOLDER:
			os.mkdir("Images")
			output = open("Images/"+gr_num+".jpg","wb")
			output.write(image.read())
			output.close()
		else:
			output = open("Images/"+gr_num+".jpg","wb")
			print ('  \033[1;32m[+]\033[0m Downloading Photo ->\n')
			output.write(image.read())
			output.close()
			print ("  \033[1;32m[+]\033[0m Saved "+gr_num+".jpg Into Images Dir\n")
	else:
		print(' \033[1;31m[-]\033[1;m Photo Not Uploaded By User !!\n')

get()
