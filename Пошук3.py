from bs4 import BeautifulSoup
import requests
import webbrowser

class News():
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
                    news = (f'<br>{temes_link.text} <br><a href="{url2}{temes_sublink}">Переглянути</a><br>')
                    #print(news)
                    page.append(news)
            
            way +=1
            step += 30
        return (page)
    #====================
    def MyView(self):
        for monitor in self.MonitorPage:
            try:
                self.show = monitor()        
                for new in self.show: self.view += new
            except:
                self.view += f'<br/><font style="font-size:20pt; color:red">{monitor} - 404 (Erorr)</font>'        
                        
     #===================                   
    def __init__(self, whatWeSearch = ' ',popular = 0):
        self.iside = 5
        #self.MonitorPage = [self.RivneRadioTrekNews,self.SarnynewsCity,self.RivnePost,self.OgoNews]
        self.MonitorPage = [self.RivneRadioTrekNews]
        self.whatWeSearch_title = whatWeSearch.title()
        self.whatWeSearch_lower = whatWeSearch.lower()
        self.whatWeSearch_upper = whatWeSearch.upper()
        self.view = ''
        self.MyView()
        f = open('News.html','w',encoding="utf-8")
        message = f'<html><head><title>{self.whatWeSearch_title}</title></head><body style = "font-size:16px">{self.view}</body></html>'
        f.write(message)
        f.close()
        webbrowser.open_new_tab('News.html')


SearchWord = input('Що шукаємо: ')
if SearchWord == '':
    news = News()
    
else:
    news = News(SearchWord,1)
    
input('Вийти')