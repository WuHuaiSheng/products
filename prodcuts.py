products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    #p = [name, price]
    products.append([name, price])

print(products) #印出大清單
print(products[0][1])

for p in products:
	print(p[0], '的價格是', p[1], '元') #印出小清單
