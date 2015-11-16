from splinter import Browser
import sys
import os
import time
import poplib
from email import parser

receptor = sys.argv[1]
ligand = sys.argv[2]
email = sys.argv[3]
cluspro_usr = sys.argv[4]
cluspro_pwd = sys.argv[5]
lig_name = ligand.split('\\')[-1]
rec_name = receptor.split('\\')[-1]
lig_name = lig_name.split(r'.')[0]
rec_name = rec_name.split(r'.')[0]

def cluspro_run(receptor, ligand, rec_name, lig_name):
    with Browser() as browser:
        # Visit URL
        url = "http://cluspro.bu.edu/login.php"
        browser.visit(url)
        browser.fill('username', cluspro_usr)
        browser.fill('password', cluspro_pwd)
        # Find and click the 'search' button
        button = browser.find_by_value('Login')
        # Interact with elements
        button.click()
        button = browser.find_by_id('showrecfile')
        button.click()
        button = browser.find_by_id('showligfile')
        button.click()
        browser.attach_file('rec', receptor)
        browser.attach_file('lig', ligand)
        browser.fill('jobname', str(lig_name) + "_" + str(rec_name))
        button = browser.find_by_value('Dock')
        button.click()

def zdock_run(receptor, ligand, email):
    with Browser() as browser:
        # Visit URL
        url = "http://zdock.umassmed.edu/"
        browser.visit(url)
        # Find and click the 'search' button
        browser.select('pdb1select', 'file')
        browser.select('pdb2select', 'file')
        browser.attach_file('inputfile1', receptor)
        browser.attach_file('inputfile2', ligand)
        browser.fill('useremail', email)
        browser.check('skipselect')
        button = browser.find_by_value('Submit')
        button.click()
        time.sleep(30)

def GRAMM_run(receptor, ligand, email):
    with Browser() as browser:
        # Visit URL
        url = "http://vakser.compbio.ku.edu/resources/gramm/grammx/"
        browser.visit(url)
        # Find and click the 'search' button
        browser.attach_file('receptor_pdb', receptor)
        browser.attach_file('ligand_pdb', ligand)
        browser.fill('email_address', email)
        button = browser.find_by_value('Submit')
        button.click()
        time.sleep(30)

def PatchDock_run(receptor, ligand, email):
    with Browser() as browser:
        # Visit URL
        url = "http://bioinfo3d.cs.tau.ac.il/PatchDock/"
        browser.visit(url)
        # Find and click the 'search' button
        browser.attach_file('recfile', receptor)
        browser.attach_file('ligfile', ligand)
        browser.fill('email', email)
        button = browser.find_by_value('Submit Form')
        button.click()
        time.sleep(30)

def swissdock_run(receptor, ligand, rec_name, lig_name):
    with Browser() as browser:
        # Visit URL
        url = "http://www.swissdock.ch/docking"
        browser.visit(url)
        # Find and click the 'search' button
        button = browser.find_by_id('link_target_upload')
        button.click()
        button1 = browser.find_by_id('link_ligand_upload')
        botton1.click()
        browser.find_by_id('DockingTargetUpload').attach_file(receptor)
        browser.find_by_id('DockingLigandUpload').attach_file(ligand)
        browser.find_by_id('DockingJobName').fill(str(lig_name) + "_" + str(rec_name))
        browser.find_by_id('DockingEmail').fill(email)
        button = browser.find_by_value('Start Docking')
        button.click()
        time.sleep(30)

def get_results():
    i = 0
    while i <= 5:
        pop_conn = poplib.POP3_SSL('smtp.gmail.com')
        pop_conn.user('bornea27@gmail.com')
        pop_conn.pass_('rangers12')
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        messages = ["\n".join(mssg[1]) for mssg in messages]
        #Parse message intom an email object:
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        for message in messages:
            if "ClusPro job finished" in message['subject']:
                print "Job Finished"
                i = i+6
                pop_conn.quit()
            else:
                pop_conn.quit()
                time.sleep(300)
        

cluspro_run(receptor, ligand, rec_name, lig_name)
zdock_run(receptor, ligand, email)
GRAMM_run(receptor, ligand, email)
PatchDock_run(receptor, ligand, email)
#swissdock_run(receptor, ligand, rec_name, lig_name)
#get_results()