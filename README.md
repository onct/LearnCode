# some code when learn programing language
python vue/node 
## something have done
1. requests BeautifulSoup
    1. one wenjuanwang task automatic(selenium 、katalon recoder)
    2. eastmoney stock info crawler(requests 、browser develop tools)
2. tesscract selenium
## something want to do
1. vue+node blog
2. douban movie info spider(scrapy)  
   
 https://movie.douban.com/top250
 next_url = response.xpath("//span[@class='next']/a/@href").get()
 movie_url = response.xpath("//div[@class='hd']/a/@href").getall()
 movie_name = response.xpath("//h1/span/text()").get()
 director = response.xpath("//span[@class='attrs']/a/text()").get()
 writer = response.xpath("//div[@id='info']/span[2]/span/a/text()").getall()
 actor = response.xpath("//div[@id='info']/span[3]/span/a/text()").getall()
 type = response.xpath("//div[@id='info']/span[@property='v:genre']/text()").getall()
 time = response.xpath("//span[@property='v:initialReleaseDate']/text()").get()
 runtime = response.xpath("//span[@property='v:runtime']/text()").get()
 grade= response.xpath("//strong/text()").get()
 summary = response.xpath("//span[@property='v:summary']/text()").get()
 comments?sort=new_score&status=P
 name= response.xpath("//span[@class='comment-info']/a/text()").getall()
 short = response.xpath("//span[@class='short']/text()").getall()