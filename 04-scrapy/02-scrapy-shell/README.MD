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
```

