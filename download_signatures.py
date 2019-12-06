# Script to download data from https://filesignatures.net
# This is the fastest way known to me for getting a verbose list of file signatures
from bs4 import BeautifulSoup as bs
import requests
import sys
import csv
import os

def download_signatures(outpath):
	total = 0
	count = 0
	temp_file = 'temp.txt'
	try:
		os.remove(outpath)
		os.remove(temp_file)
	except:
		pass
	print('Downloading signatures from https://filesignatures.net')
	for num in range(1,30):
		page_num = str(num)
		page_url = 'https://filesignatures.net/index.php?page=all&currentpage='+page_num+'&order=SIGNATURE&alpha=All'
		#GET request page
		page = requests.get(page_url).text
		soup = bs(page, 'lxml')
		table = soup.find('table', id='innerTable')
		rows = table.findAll('tr')
		del rows[0]#Delete the useless empty td at the first
		if len(rows)<30:
			if count != 0:
				print('reached end')
				break
			count+=1
		total += len(rows)
		with open(temp_file, 'a') as extfile:
			for row in rows:
				for td in row.findAll('td'):
					data = td.findNext(text=True)
					if data != '\n':
						extfile.write(data+', ')
				extfile.write('\n')
	print('total rows counted ',total)
	string = ''
	with open(temp_file, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',');
		for row in reader:
			row[0] = row[0].lower()
			row[1] = row[1].strip().replace(' ','').lower()
			row[2] = row[2].strip().lower()
			del row[3]
			string += str(row)+',\n'
	with open(outpath, 'a') as writefile:
		writefile.write('list = [\n')
		writefile.write(string)
		writefile.write(']')
	os.remove(temp_file)
try:
	download_signatures('signatures.py')
except:
	print('Network error')
