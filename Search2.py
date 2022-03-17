from bs4 import BeautifulSoup
import requests
import webbrowser
import threading
class News():
    #=========================
    #
    def RivneRadioTrekNews(self):
        way = 0
        step = 0
        page = [f'<br/><font style="font-size:30pt">Знайшли <b>{self.whatWeSearch_title}</b> на radiotrek.rv.ua</font><br/>']
        url2 = "https://radiotrek.rv.ua"
        while way < self.iside:
            
            if way == 0:
                url1 = "https://radiotrek.rv.ua/region/rivne/"                
            else:
                url1 = f"https://radiotrek.rv.ua/region/rivne/?st={step}"
            page.append(f'<br/><font style="font-size:20pt"><a href = "{url1}">Сторінка {way}</a></font><br/>')
            request = requests.get(url1)
            soup = BeautifulSoup(request.text, "html.parser")
            teme = soup.find_all ("article")                        
            for temes in teme:               
                temes = temes.find("div")
                temes_link = temes.find("a")
                if temes is not None and self.whatWeSearch_title in str(temes) or self.whatWeSearch_lower in str(temes) or self.whatWeSearch_upper in str(temes):
                    temes_sublink = temes_link.get('href')
                    news = (f'{temes.text} \n {url2}{temes_sublink}')
                    print(news)
            
            way +=1
            step += 30
        return (page)
    
    def SarnynewsCity(self):
        way = 0
        step = 0
        page = [f'<br/><font style="font-size:30pt">Знайшли <b>{self.whatWeSearch_title}</b> на Sarnynews.city</font><br/>']
        url2 = "https://sarnynews.city"
        while way < self.iside:
            
            if way == 0:
                url1 = "https://sarnynews.city/articles/"                
            else:
                url1 = f"https://sarnynews.city/articles/all/{step}"
            page.append(f'<br/><font style="font-size:20pt"><a href = "{url1}">Сторінка {way}</a></font><br/>')
            request = requests.get(url1)
            soup = BeautifulSoup(request.text, "html.parser")
            teme = soup.find_all ("a", class_ = "title")
            #print(teme)
            for temes in teme:         
                if temes is not None and self.whatWeSearch_title in str(temes) or self.whatWeSearch_lower in str(temes) or self.whatWeSearch_upper in str(temes):
                    temes_sublink = temes.get('href')
                    news = (f'{temes.text} \n {url2}{temes_sublink}')
                    print(news)
            
            way +=1
            step += 2
        return (page)
    def RivnePost(self):
        way = 0
        step = 0
        page = [f'<br/><font style="font-size:30pt">Знайшли <b>{self.whatWeSearch_title}</b> на RivnePost</font><br/>']
        url2 = "https://rivnepost.rv.ua"
        while way < self.iside:
            
            if way == 0:
                url1 = "https://rivnepost.rv.ua/category/region"                
            else:
                url1 = f"https://rivnepost.rv.ua/category/region/{step}"
            page.append(f'<br/><font style="font-size:20pt"><a href = "{url1}">Сторінка {way}</a></font><br/>')
            request = requests.get(url1)
            soup = BeautifulSoup(request.text, "html.parser")
            teme = soup.find_all ("ul", class_ = "list-13")
            #print(teme)
            for temes in teme:               
                temes = temes.find("h3")
                temes_link = temes.find("a")
                if temes is not None and self.whatWeSearch_title in str(temes) or self.whatWeSearch_lower in str(temes) or self.whatWeSearch_upper in str(temes):
                    temes_sublink = temes_link.get('href')
                    news = (f'{temes.text} \n {url2}{temes_sublink}')
                    print(news)
            
            way +=1
            step += 14
        return (page)
    def OgoNews(self):
        way = 0
        step = 0
        page = [f'<br/><font style="font-size:30pt">Знайшли <b>{self.whatWeSearch_title}</b> на OgoNews</font><br/>']
        url2 = "https://ogo.ua"
        while way < self.iside:
            
            if way == 0:
                url1 = "https://ogo.ua/rubrics/view/region"                
            else:
                url1 = f"https://ogo.ua/rubrics/view/region/page:{step}"
            page.append(f'<br/><font style="font-size:20pt"><a href = "{url1}">Сторінка {way}</a></font><br/>')
            request = requests.get(url1)
            soup = BeautifulSoup(request.text, "html.parser")
            teme = soup.find_all ("li")
            #print(teme)
            for temes in teme:
                temes_link = temes.find("a")
                if temes is not None and self.whatWeSearch_title in str(temes) or self.whatWeSearch_lower in str(temes) or self.whatWeSearch_upper in str(temes):
                    temes_sublink = temes_link.get('href')
                    news = (f'{temes.text} \n {url2}{temes_sublink}')
                    print(news)
            
            way +=1
            step += 1
        return (page)
    #Стартуємо
    def searchPopular(self):
        
        print('зараз популярне:',self.view)
    def MyView(self):
        for monitor in self.MonitorPage:
            try:
                self.show = monitor()        
                for new in self.show: self.view += new
            except:
                self.view += f'<br/><font style="font-size:20pt; color:red">{monitor} - 404 (Erorr)</font>'        
                        
    def __init__(self, whatWeSearch = ' ',popular = 0):
        self.iside = 2
        self.MonitorPage = [self.RivneRadioTrekNews,self.SarnynewsCity,self.RivnePost,self.OgoNews]
        #self.MonitorPage = [self.OgoNews]
        self.whatWeSearch_title = whatWeSearch.title()
        self.whatWeSearch_lower = whatWeSearch.lower()
        self.whatWeSearch_upper = whatWeSearch.upper()
        self.view = ''
        self.MyView()
#News()
SearchWord = input('Що шукаємо: ')
if SearchWord == '':
    news = News()
else:
    news = News(SearchWord,1)
input('Вийти')

