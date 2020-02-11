import scrapy 

def archivo(titulos,rating,duracion,director,ingresos,year):
    import csv
    with open('movies.csv','a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')

        data = list(zip(titulos,rating,duracion,director,ingresos,year))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)

class IntroSpider(scrapy.Spider):
    name = 'movies_spider' 
    urls = [
        'https://www.imdb.com/list/ls026612019/',
        'https://www.imdb.com/list/ls042050393/'
    ]

    def start_requests (self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):

        etiqueta_contenedora = response.css('div.lister-item')

        titulos = etiqueta_contenedora.css('h3.lister-item-header>a::text').extract() 
        print(titulos)

        rating = etiqueta_contenedora.css('div.ipl-rating-star.small > span.ipl-rating-star__rating::text').extract() 
        print(rating)

        duracion = etiqueta_contenedora.css('span.runtime::text').extract()  
        print(duracion)

        director = etiqueta_contenedora.css('p.text-muted.text-small > a:first-child::text').extract()
        print(director)

        ingresos = etiqueta_contenedora.css('p.text-muted.text-small > span:nth-child(5)::attr(data-value)').extract()
        print(ingresos)

        year = etiqueta_contenedora.css('span.lister-item-year.text-muted.unbold::text').extract()  
        print(year)


        archivo(titulos,rating,duracion,director,ingresos,year)