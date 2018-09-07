# Telugu-Newspaper-Article-Dataset
This Project scrapes articles from archives of Telugu newspaper website Andhra Jyoti.A set of queries is created and corresponding ground truth answers were retrieved by a combination of 2 popular ranking functions namely bm25 and tf-idf.

## Dataset
Complete Dataset can be downloaded from [here](https://drive.google.com/file/d/1IbqM335M7imzG-2ZV0d8-JbRqCnyAii3/view?usp=sharing) .

---

## Requirements
* Python3
* Pip3 
* Telugu Language should be enabled in Language settings of your machine,to be able to see telugu text.

## Execution Steps
Open the terminal and change current working directory to the location where you want the dataset to be stored.
```
python makedirs.py 
pip3 install bs4
pip3 install requests
python3 scrapeTelugu.py
```
You should now be seeing text files getting created in subfolders of the directory `telugudata`. 
