""" converting pdf to docx using pdf2docx Library """

from pdf2docx import Converter
import os
import shutil
import mammoth
from bs4 import BeautifulSoup
source_folder = '/home/akira/projects/PDF_parser/'
pdf_file = source_folder + 'dyp_resumes/'
docx_file = source_folder + 'docs/'
html_file = source_folder + 'html/'
txt_file = source_folder + 'txt/'
f=os.listdir(pdf_file)
for i in f:
	t = i.split('.')
	if(t[1] == "pdf" ):
		cv = Converter(pdf_file+i)
		cv.convert(pdf_file+t[0]+'.docx')
		cv.close()
"""Moving docs to doc folder"""
for file_name in os.listdir(pdf_file):
	print(file_name)
	source = pdf_file + file_name
	destination = docx_file + file_name
	temp = os.path.splitext(file_name)
	print(temp)
	if temp[1] == '.docx':
		if os.path.isfile(source):
			shutil.move(source, destination)
			#print('Moved:', file_name)	
			
"""Docx to HTML"""
list = os.listdir(docx_file)
for file in list:
	t = file.split(".")
	if(t[1] == "docx"):
		result = mammoth.convert_to_html(docx_file + file)
		html = result.value
		f = open(html_file + t[0]+'.html', 'w' )
		f.write(html)
		f.close()

"""HTML to TXT"""
list = os.listdir(html_file)
print(list)
for file in list:
	t = file.split(".")
	if(t[1] == "html"):
		#print('html is found')
		with open(html_file + file, "r") as fp:
			doc = BeautifulSoup(fp, "html.parser")
		with open(t[0]+'.txt', 'w') as txt:
			for i in doc.find_all('p'):
				txt.write(i.get_text())
				txt.write('\n')
		txt.close()
"""Moving txt to txt folder"""
for file_name in os.listdir(source_folder):
	print(file_name)
	source = source_folder + file_name
	destination = txt_file + file_name
	temp = os.path.splitext(file_name)
	print(temp)
	if temp[1] == '.txt':
		if os.path.isfile(source):
			shutil.move(source, destination)
			print('Moved:', file_name)

