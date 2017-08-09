import config
class Crawler():
    def __init__(self):
        pass

    def crawl(self,platform):
        from selenium import webdriver
        from pyvirtualdisplay import Display
        import requests
        from bs4 import BeautifulSoup
        display = Display(visible=0, size=(800, 600))
        display.start()
        if(platform == "thebetterindia"):
            all_urls = []
            try:
                try:
                    driver = webdriver.Chrome(config.DRIVER_PATH)
                except:
                    pass
                #not used driver though yet.....Might use in scheduling
                for num in range(330):
                    url = 'http://www.thebetterindia.com/page/' + str(num) +'/'
                    r = requests.get(url)
                    data = r.content.decode(encoding='UTF-8')
                    soup = BeautifulSoup(data,'lxml')
                    tmp1 = soup.find_all("h3",{'class':'g1-gamma g1-gamma-1st entry-title'})
                    # tmp2 = tmp1[0].find_all('a',{"href":"s-result-item celwidget"})
                    for li in tmp1:
                        u = li.find('a')['href']
                        all_urls.append(u)
            except Exception as e:
                print(e)
            finally:
                try:
                    driver.quit()
                    display.stop()
                except:
                    pass
                return all_urls
        else:
            print("platform name does not match \n")

        def __str__(self):
            return str(self.name)
if __name__ == '__main__':
    obj = Crawler()
    a = obj.crawl('thebetterindia')
    print(a)
