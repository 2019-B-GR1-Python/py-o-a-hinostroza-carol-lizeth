import scrapy 

def archivo(palabras):
    import csv
    with open('palabras_masbuscadas.csv','a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')

        data = list(zip(palabras))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)

class IntroSpider(scrapy.Spider):
    name = 'palabras_spider' 
    urls = [
        'https://www.imdb.com/list/ls026612019/'
        
    ]


    def start_requests (self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):

        etiqueta_contenedora = response.css('div.lister-item')

        palabras = etiqueta_contenedora.css('h3.lister-item-header>a::text').extract() 
        print(palabras)

        archivo(palabras)