
import os
import random
from re import findall
from sys import path
import requests
from bs4 import BeautifulSoup

os.getcwd()


#? Algebra 1
khan_algebra1 = requests.get('https://www.khanacademy.org/math/algebra').text
algebra1_page = BeautifulSoup(khan_algebra1, 'lxml')


#? Algebra 2
khan_algebra2 = requests.get('https://www.khanacademy.org/math/algebra2').text
algebra2_page = BeautifulSoup(khan_algebra2, 'lxml')


main = algebra1_page.find('div', class_ = "_lhvgag5")
for base in main:
    # you are inside the main div file now
    
    for topic in main.find_all('div', class_ = "_12yy6f6l"):
        
        title = topic.find('h3', class_ = "_k50sd54").text
        print(title)
        print()
        
        # lesson_section = topic.find('div', class_ = "_14kisdro")
        # print(lesson_section.text)
        
        for span in topic.find_all('span', class_ = "_twomc80"):
            lesson = span.find('a', class_ = "_dwmetq").text
            flesson = lesson[:lesson.rfind(":")]
            
            print(flesson)
        
        # for span in lesson_section.find_all('span', class_ = "_twomc80"):
        #     lesson = span.find('a', class_ = "_dwmetq").text
        #     print(lesson)
        
        print()
        print()
    
    
main = algebra2_page.find('div', class_ = "_lhvgag5")
for base in main:
    # you are inside the main div file now
    
    for topic in main.find_all('div', class_ = "_12yy6f6l"):
        
        title = topic.find('h3', class_ = "_k50sd54").text
        print(title)
        print()
        
        # lesson_section = topic.find('div', class_ = "_14kisdro")
        # print(lesson_section.text)
        
        for span in topic.find_all('span', class_ = "_twomc80"):
            lesson = span.find('a', class_ = "_dwmetq").text
            flesson = lesson[:lesson.rfind(":")]
            
            print(flesson)
        
        # for span in lesson_section.find_all('span', class_ = "_twomc80"):
        #     lesson = span.find('a', class_ = "_dwmetq").text
        #     print(lesson)
        
        print()
        print()
    
    



#_______________________________






def khan_(input = "default"):
    
    site_name = input
    first_part_site = site_name[:site_name.rindex(f"/")]
    file_path = site_name[site_name.rindex(f"/"):]
    
    request_site = requests.get(f'{input}').text
    site = BeautifulSoup(request_site, 'lxml')
    
    #? New section
    
    main = site.find('div', class_ = "_lhvgag5")
    
    for base in main:
        # you are inside the main div file now
        
        for topic in main.find_all('div', class_ = "_12yy6f6l"):
            
            title = topic.find('h3', class_ = "_k50sd54").text
            print(title)
            print()
            
            # lesson_section = topic.find('div', class_ = "_14kisdro")
            # print(lesson_section.text)
            
            for span in topic.find_all('span', class_ = "_twomc80"):
                lesson = span.find('a', class_ = "_dwmetq").text
                flesson = lesson[:lesson.rfind(":")]
                
                print(flesson)
            
            # for span in lesson_section.find_all('span', class_ = "_twomc80"):
            #     lesson = span.find('a', class_ = "_dwmetq").text
            #     print(lesson)
            
            print()
            print()



notion_math = requests.get('https://www.notion.so/adf44ccdd7c14c7bb7b6c73ed5d3c334?v=c30f8d70789a416b9dc232f1fe0456a7').text
notion = BeautifulSoup(notion_math, 'lxml')


print(notion.prettify())

row_of_cells = notion.find_all('div', class_ = "notion-selectable notion-page-block notion-collection-item")

# divide that row of cells

task_cell = row_of_cells.find_all('div')
span_cell = task_cell.find_all('span').text


        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
url = "www.example.com"
new_url = url[:url.rfind(".")]
print(new_url)
    
    
    
    # for b in page.find('h3', class_ = "_k50sd54").text:
    #     print(b)
        
    # for c in page.find('a', class_ = "_dwmetq").text:
    #     print(c)
        
        
        
    # section_title = page.find_all('h3', class_ = "_k50sd54").text
    # print(section_title)
    
    
    
    
    
    #insert another for loop for scraping lesson names:
     
        # lesson_link = page.find_all('a', class_ = "_dwmetq")
