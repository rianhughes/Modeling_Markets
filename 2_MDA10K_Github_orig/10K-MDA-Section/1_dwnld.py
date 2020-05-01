import os
import re
import csv
import requests 
import urllib

# edgar/data/98246/0000098246-20-000058
# Want the Financial_Report.xlsx

filepath = "/home/rian/Desktop/1_Work/6_Jobs__Quant_RiskManagmemnt_DS/Modeling_the_Market/2_MDA10K_Github_orig/10K-MDA-Section/"

download_xlsx = os.path.join(filepath, "downloadlist_xlsx.txt")
download = os.path.join(filepath, "downloadlist.txt")

# remove new downloadlist_xlsx.txt file if it exists. Keep it fresh.
if os.path.exists(download_xlsx):
    os.remove(download_xlsx)

# Create a bunch of links to potential Financial_Report.xlsx files and save in download_xlsx
with open(download_xlsx,"a+") as newfile:
    g = open(download, "r")
    for line in g:
     substring = re.search("edgar/data/(.*?).txt", line).group(1)
     substring = substring.replace('-','')
     str2 = re.search("(.*?),", line).group(1)
     #print([ str2 ,"edgar/data/" + substring])
     newfile.write(str2 + "," +"edgar/data/" + substring + "/Financial_Report.xlsx" +"\n")
    g.close()

# download any of these download_xlsx files.
with open(download_xlsx, 'r') as txtfile:
    reader = csv.reader(txtfile, delimiter=',')
    for line in reader:
        FileNUM=line[0].strip()
        Filer=os.path.join(filepath, str(line[0].strip())+".txt")
        url = 'https://www.sec.gov/Archives/' + line[1].strip()
        #print(line[1].strip())
        urllib.urlretrieve(url, filepath + FileNUM + "_" + "Financial_Report.xlsx" )

