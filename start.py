#! /usr/bin/Python
#coding:utf-8
import sys
import os
import subprocess
import commands
reload(sys)
sys.setdefaultencoding('utf-8')


path = os.getcwd() + os.sep + 'src' + os.sep
# print(path)
dirPath = os.getcwd() + os.sep + 'out' + os.sep
if not os.path.exists(dirPath):
	os.mkdir(dirPath)

for file in os.listdir(path):
	if not file.startswith('.') and os.path.isfile(os.path.join(path, file)) and file.endswith('.png'):
		targetFile = path + file
		cmd = './pngquant --quality=65-80 ' + targetFile + ' -o ' + dirPath + file
		# print(cmd)
		a,b = commands.getstatusoutput(cmd)

