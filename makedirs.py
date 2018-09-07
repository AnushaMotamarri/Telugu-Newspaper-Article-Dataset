import os,sys
os.mkdir("telugudata")
a={"2015","2016","2017"}
for i in a:
	os.mkdir("telugudata/"+i)
b={"andhrapradesh","business","editorial","entertainment","freshnews","nation","navya","special","sports","telangana"}
for i in a:
	for j in b:
		os.mkdir("telugudata/"+i+"/"+j)
