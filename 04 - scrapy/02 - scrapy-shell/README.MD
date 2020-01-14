# Scrapy
## Scrapy instalacion 

Ejecutar dentro del `Anaconda prommt`

```
$ pip install scrapy 
```

## Comandos Generales

Da `las características` para poder hacer web scraping o web crawling de ese computador
```
$ scrapy bench
```

Visualizar  `las configuraciones extra`
```
$ scrapy settings
```

Visualizar  `la version de scrapy`
```
$ scrapy version
```

### scrapy view `url`

`Visualizar  el contenido`  como lo ve scrapy
Si se ve el cotenido 
```
$ scrapy view https://www.pluralsight.com/authors
```

No se ve elcontenido 
```
$ scrapy view https://srienlinea.com
```

### scrapy shell `url`
Permite interactuar con la respuesta del scrapy
```
$ scrapy shell http://quotes.toscrape.com/
$response.css('.author::text')
$response.css('.author::text').extract()
$response.css('.author').extract()
$response.css('title::text' ).extract()
$response.css('title').extract()
$response.css('title')
$response.css('.row > div > div:nth-child(2) > .text::text').extract()

$response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$response.xpath('/html/head/title').extract()
$response.xpath('/html/body/div/div[2]/div[2]/h2/text()').extract()
$response.xpath("//div[@class='quote']").extract_first()
$response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$response.xpath("//div[@class='quote']/span/a/@href").extract_first()
```

## scrapy startproject 'nombre_proyecto'
```
$scrapy startproject arania_basica
```

