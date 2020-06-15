from bs4 import BeautifulSoup
import requests

def amazon(data):
    removed = ["amazon","ara"]
    new_data = []
    for splitted in data:
        if splitted not in removed:
            new_data.append(splitted)
    
    data ="".join(new_data)

    searched = "https://www.amazon.com.tr/s?k="+data+"&__mk_tr_TR=ÅMÅŽÕÑ&ref=nb_sb_noss_2"
    
    
    amazon = requests.get(searched).text
    
    bf = BeautifulSoup(amazon,'lxml')
    
    #phone=bf.find('div', class_='a-section a-spacing-none a-spacing-top-small')
    #
    #head =phone.h2.a.text
    #print(head)
    #price = bf.find('span',class_='a-price-whole').text
    #print(price)
    #
    price_tag = []
    name =[]
    
    for search_rs in bf.find_all('div', class_='a-section a-spacing-medium'):
    
        result = search_rs.find('a', class_='a-link-normal a-text-normal').text
        print(result)
    
        try:
        
            price = search_rs.find('span', class_='a-offscreen').text
            print(price)
    
        except AttributeError:
            print("değeri yok")
    
        
        clean = price.split('₺')
        price ="".join(clean)
        name.append(result)
        price_tag.append(price)
        


    for x in range(len(price_tag)):
        print("fiyatı:",price_tag[x])
        print("ismi:",name[x])
    
    
    
    #bu modül daha geliştirilicek
    