import requests
from bs4 import BeautifulSoup
import os 
def news():
      
      
    for k in range(100000,500000): 
        
        url='http://www.andhrajyothy.com/artical?SID='+str(k)
        resp=requests.get(url)
        if resp.status_code==200:
            soup=BeautifulSoup(resp.text,'html.parser') 
            filename=''
            remove=0
            loopvar=0
            filestr=''
            f=open('temp.txt','w',encoding='utf-8')
            l2=soup.find("span",{"class":"arial f-12"})
            l1=soup.find("ul",{"class":"breadcrumb f-19"})
            ll=soup.find("span",{"class":"f-24 ln-235"})
            forhead=ll.findAll("span",{"id":"ContentPlaceHolder1_lblStoryHeadLine"})
            for head in forhead:
                head=head.text
            for i in l2.findAll("span",{"id":"ContentPlaceHolder1_lblUpdatedDate"}):
                p1=i.text
                year=p1[6:10]
                date=p1.replace("-","")
                date=date[0:8]
            for subnews in l1.findAll("a",{"id":"ContentPlaceHolder1_alnk1"}):
                p=subnews.text
                if p=="జాతీయం":
                    filename="telugudata/"+str(year)+"/nation/1"+date+str(k)+".utf8"
                elif p=="నవ్య":
                    filename="telugudata/"+str(year)+"/navya/1"+date+str(k)+".utf8"
                elif p=="ఆంధ్రప్రదేశ్":
                    filename="telugudata/"+str(year)+"/andhrapradesh/1"+date+str(k)+".utf8"
                elif p=="తెలంగాణ":
                    filename="telugudata/"+str(year)+"/telangana/1"+date+str(k)+".utf8"  
                elif p=="చిత్రజ్యోతి":
                    filename="telugudata/"+str(year)+"/entertainment/1"+date+str(k)+".utf8"
                elif p=="బిజినెస్‌":
                    filename="telugudata/"+str(year)+"/business/1"+date+str(k)+".utf8"
                elif p=="ఎడిటోరియల్":
                    filename="telugudata/"+str(year)+"/editorial/1"+date+str(k)+".utf8"
                elif p=="క్రీడాజ్యోతి":
                    filename="telugudata/"+str(year)+"/sports/1"+date+str(k)+".utf8"
                elif p=="తాజావార్తలు":
                    filename="telugudata/"+str(year)+"/freshnews/1"+date+str(k)+".utf8"
                elif p=="ప్రత్యేకం":
                    filename="telugudata/"+str(year)+"/special/1"+date+str(k)+".utf8"
            print(filename)
            l=soup.find("span",{"id":"ContentPlaceHolder1_lblStoryDetails"})
            if filename!='' and year!='':
               f=open(filename,'w',encoding='utf-8')
               f.write("<DOC>"+"\n"+"<DOCNO>1"+date+str(k)+".utf8</DOCNO>"+"\n"+"<TEXT>"+"\n"+"\n"+p1+"\n"+"\n"+head+"\n"+"\n")
               for i in l.findAll("div"): 
                        loopvar=1
                        if i.text!="":
                            filestr=i.text
                            f.write(filestr)
               f1=open("removed.txt",'a+',encoding='utf-8')         
               if loopvar==0:
                   filestr=l.text
                   #os.remove(filename)
                   #f1.write(str(k)+"\n")
                   #print("removed")
                   f.write(filestr)
                   loopvar=0
                   
            f.write("\n"+"</TEXT>"+"\n"+"</DOC>")
            f.close()                     
        else:
            print("Error")
news()
