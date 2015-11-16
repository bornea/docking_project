import poplib
from email import parser
from splinter import Browser
import sys
import os
import time
import urllib

number = 50 
self = poplib.POP3_SSL('pop.gmail.com')
self.user('recent:bornea27@gmail.com')
self.pass_('rangers12')
(num, size) = self.stat()

for i in range(num-5 ,num):          
	message = self.retr(i)
	for j in message:
		if r'Subject:' in str(j):
			if 'PatchDock results' in str(j):
				text = message[-2]
				item = text[-1]
				item = item.strip()
				with Browser() as browser:
					url = str(item)
					browser.visit(url)
					link = browser.find_link_by_partial_text('result.1.pdb')
					


