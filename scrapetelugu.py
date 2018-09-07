import requests
from bs4 import BeautifulSoup
 
def news():
      
    for k in range(5000,1000000): 
        url='http://www.andhrajyothy.com/artical?SID='+str(k)
        resp=requests.get(url)
        if resp.status_code==200:
            print("Successfully opened the web page")
            print("The news are as follow :-\n")
            soup=BeautifulSoup(resp.text,'html.parser') 
            l=soup.find("span",{"id":"ContentPlaceHolder1_lblStoryDetails"})
            
            for i in l.findAll("div"):
                if i.text!="":
                    filestr="<DOC>"+"\n"+"<DOCNO>"+str(k)+"<DOCNO>"+"\n"+"<TEXT>"+"\n"+i.text+"\n"+"<TEXT>"+"\n"+"<DOC>"
            l1=soup.find("ul",{"class":"breadcrumb f-19"})
            l2=soup.find("span",{"class":"arial f-12"})
            for i in l2.findAll("span",{"id":"ContentPlaceHolder1_lblUpdatedDate"}):
                p=i.text
                year=p[6:10]
                print(year)
            for subnews in l1.findAll("a",{"id":"ContentPlaceHolder1_alnk1"}):
                p=subnews.text
                if p=="జాతీయం":
                    filename="telugudata/"+str(year)+"/nation/"+str(k)+".txt"
                if p=="నవ్య":
                    filename="telugudata/"+str(year)+"/navya/"+str(k)+".txt"
                if p=="ఆంధ్రప్రదేశ్":
                    filename="telugudata/"+str(year)+"/andhrapradesh/"+str(k)+".txt"
                if p=="తెలంగాణ":
                    filename="telugudata/"+str(year)+"/telangana/"+str(k)+".txt"  
                if p=="చిత్రజ్యోతి":
                    filename="telugudata/"+str(year)+"/entertainment/"+str(k)+".txt"
                f=open(filename,'w',encoding='utf-8')
                f.write(filestr)
                f.close()
                    
        else:
            print("Error")
         
news()
