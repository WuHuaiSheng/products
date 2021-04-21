products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    #p = [name, price]
    products.append([name, price])

print(products) 
print(products[0][1])

for p in products:
	print(p[0], '的價格是', p[1], '元') 
sum = 0
p = int(p)
with open ('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '元' + '\n')
		sum = sum + p[1]
print(sum)
