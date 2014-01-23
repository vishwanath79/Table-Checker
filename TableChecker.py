import urllib2
from bs4 import BeautifulSoup
#table = ['10k_user','419_vol_sigs','aim_sigs_manysn']
table = ['table1','table2']
ip = raw_input("Enter IP/Domain ")
#ip = '149.130.13.236'
for i in table:
    mysite = urllib2.urlopen("http://url"+ ip +"&table_name=" + i+ "&submit_button=Check+Presence").read()
#content = mysite.readlines()
#length = len(content) 
#print length
    soup = BeautifulSoup(mysite)
#print soup.prettify()
    c = soup.findAll('h3')
    print c 