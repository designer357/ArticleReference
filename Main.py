__author__ = 'chengmin'

import subprocess
import os
path="/ArticleReference/2014.pdf"
#process = subprocess.Popen(["pdftotext", path])
#ret=subprocess.call(["pdftotext","-layout","enc","UTF-8","~/PycharmProjects/ArticleReference/2014.pdf","~/PycharmProjects/ArticleReference/2014.txt"])
process=subprocess.Popen(["/usr/local/bin/pdftotext","-layout","-enc","UTF-8","2014.pdf"])

f_out=open("reference.dat","w")
f_inlist=filter(lambda str:".txt" in str,os.listdir(os.getcwd()))
for eachfile in f_inlist:
    with open(eachfile) as f_in:
        f=f_in.readlines()
        A= "".join(f[f.index("References\n"):len(f)-1])
        f_out.write(A)
        print A





