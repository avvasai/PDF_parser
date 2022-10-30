from bs4 import BeautifulSoup
text_list = []
with open("/home/akira/projects/PDF_parser/html/Aakriti_s Resume.html", "r") as fp:
    doc = BeautifulSoup(fp, "html.parser")
val = len(doc.find_all('p'))
with open('temp.txt', 'w') as txt:
    for i in doc.find_all('p'):
            txt.write(i.get_text())
            txt.write('\n')
txt.close()
#val = len()
'''
with open('temp.txt','w') as txt:
    txt.write(doc.p.get_text())
    txt.write(doc.p.next.get_text())
    txt.close()
'''