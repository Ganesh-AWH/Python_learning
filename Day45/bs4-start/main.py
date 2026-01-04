from bs4 import  BeautifulSoup

with open(r"Day45\bs4-start\website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)    #full title
# print(soup.title.name)    #title name
# print(soup.title.string)    #title String
# print(soup.prettify()) #structuring the html texts
# print(soup.p) #prints first paragraph tag

#finding all paragraph, lists, anchor tags
all_anchor_tags = soup.find_all(name="a") #returns list all anchor tags
# print(all_anchor_tags)

#extracting only texts from all tags
for tag in all_anchor_tags:
    # print(tag.getText()) #used to extract text form the tag
    print(tag.get("href")) #used to extract attributes value