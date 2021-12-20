import xml.etree.ElementTree as ET
import requests
import pandas as pd

url="https://www.europarl.europa.eu/rss/doc/top-stories/en.xml"

def top_stories_csv(url):
    #using requests,get the text from the url using the get method of request
    top_stories=requests.get(url)
    #Parse the string using the fromstring method in the element tree package
    root = ET.fromstring(top_stories.text)
    stories_list=[]
    #loop over the element tree element called items and find all the titles and append to the stories empty list created above
    for item in root.iter('item'):
        stories=item.find('title')
        #Use string slicing to slice off 'Top story' from the list names
        stories_list.append(stories.text[11:])
    #create a field title for the header     
    field=['Top Stories']
    #using list values and field, create dictionary and using pandas method to convert into a dataframe
    dict = {'Top Stories': stories_list} 
    df=pd.DataFrame(dict)
    #save dataframe as a csv in current directory
    df.to_csv('top_stories')
    #return list for debug
    return stories_list

if __name__ == "__main__":
    top_stories_csv(url)  
