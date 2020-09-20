from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google_auth_oauthlib import flow


class GoogleDocReferenceDivStyleGuide:
    def __init__(self,url):
        self.url = url
        
    
    def justReference(self, variable):
        dictionary = variable
        self.URLtoGoogleDocJSONtoText()
        self.cleaningText()
        self.referenceStyleGuide(dictionary)
        
        
    def docIDfromURL(self):
        print('getting document ID ...')
        self.url =  self.url.replace('https://docs.google.com/document/d/','')
        self.url =  self.url.replace('/edit','')
        self.url = self.url.replace('?usp=sharing','')
        print('document id: {}'.format( self.url))
        return  self.url
    
    
    def Authenticate(self):
        extracted_text = []
        print("authenticating ...")
        appflow = flow.InstalledAppFlow.from_client_secrets_file(r"C:\Users\Ethan Coston\Desktop\client_secret_883115423488-r97oa086lvgqembkqmkr34u04iqlso5a.apps.googleusercontent.com.json",scopes=["https://www.googleapis.com/auth/drive.readonly"]
        )
        launch_browser=True
        if launch_browser==False:
            appflow.run_local_server()
        else:
            appflow.run_console()
        credential = appflow.credentials
        print("authentication complete\r\n\r\n")
        print("beginning google doc extract ...")
        service = build('docs', 'v1', credentials=credential)
        document = service.documents().get(documentId=self.url).execute()
        extracted_json = json.dumps(document, indent=4, sort_keys=True)
        print("extraction complete\r\n\r\n\r\n")
        return extracted_json
    
    
    def URLtoGoogleDocJSONtoText(self):
        
        self.docIDfromURL()
        text = self.Authenticate()
        print('Exporting text from Google Doc ...')
        article_as_dict = json.loads(text)
        text_as_dict = article_as_dict['body']['content']
        len(text_as_dict)
        text_as_list = []
        counter = 1
        while counter <= (len(text_as_dict)-1):
            if "paragraph" in text_as_dict[counter]:
                paragr = text_as_dict[counter]['paragraph']['elements']
                if len(paragr) == 1:
                    text_as_list.append(paragr[0]['textRun']['content'])
                else:
                    counter2 = 0
                    while counter2 <= (len(paragr)-1):
                        if "textRun" in paragr[counter2]:
                            text_as_list.append(paragr[counter2]['textRun']['content'])
                        counter2 = counter2 + 1
            counter = counter + 1
        text_as_str = ''
        for x in text_as_list:
             text_as_str += x
        print('Export complete\r\n\r\n')
        self.text = text_as_str
        return self.text
    
    
    def ScrapeAndReference(self):
        
        dictionary = self.StyleGuideScraper()
        self.URLtoGoogleDocJSONtoText()
        self.cleaningText()
        self.referenceStyleGuide(dictionary)
        
        
    def StyleGuideScraper(self):
        print('scraping ...')
        params3 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
        style_guide = requests.get('https://www.diversitystyleguide.com/',headers=params3)
        style_guide
        html_soup = BeautifulSoup(style_guide.text, 'html.parser')
        glossary = html_soup.find('ul', attrs={"class": "glossaryList"})
        dictionary = {}
        for lst in glossary.findAll("li"):
            tx_nme = lst.find('a')
            if '"' in tx_nme.get_text()[0]:
                txt_def = str(tx_nme.get_text()[1:-1])
            else:
                txt_def = str(tx_nme.get_text())
            defin = lst.find('div', attrs={"class": "glossary_itemdesc"})
            dictionary[txt_def] = defin.text
        print('Completed scrape\r\n\r\n')
        dictionary = self.cleanScrapedStyleguide(dictionary)
        return dictionary
        
        
    def cleanScrapedStyleguide(self,var):
        print('cleaning scraped text ...')
        dictionary = var
        for x in dictionary:
            split = dictionary[x].splitlines()
            for y in split:
                if type(y) == list:
                    while("" in split) : 
                        split.remove("")
                    while('\xa0' in split):
                        split.remove('\xa0')
                    while('\xa0' in split):
                        split.remove('\xa0a')
            while("" in split) : 
                split.remove("")
            while('\xa0' in split):
                split.remove('\xa0')
            while('\xa0' in split):
                split.remove('\xa0a')
            while('\x0b' in split):
                split.remove('\x0b')
            split = '\r\n\r\n'.join(split)+'\r\n\r\n\r\n'
            dictionary[x] = split
        print('cleaned\r\n\r\n')
        return dictionary


    def cleaningText(self):
        print('cleaning Google Doc text ...')
        self.commas()
        self.periods()
        self.quotes()
        print('cleaned\r\n\r\n')
        return ('cleaned')
        
        
    def commas(self):
        if ',' in self.text:
            self.text = self.text.replace(',','')
        else:
            return('no commas')
        print('removed commas')
        
        
    def periods(self):
        if '.' in self.text:
            self.text = self.text.replace('.','')
        else:
            return('no periods')
        print('removed periods')
        
        
    def quotes(self):
        self.text = self.text.replace('”','')
        self.text = self.text.replace('“','')
        print('removed quotes')
    
        
    def referenceStyleGuide(self, var):
        dictionary = var
        print('beginning reference ...\r\n\r\n\r\n')
        for x in dictionary:
            if ' '+x+' ' in self.text:
                location = self.text.find(x)
                print('Location: {}\r\n\r\n{}: {}'.format(location,x,dictionary[x]))
        print('reference complete')
        return('completed\r\n\r\n')
