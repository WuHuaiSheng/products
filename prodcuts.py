#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 跳到下一回(不執行7,8行的意思)
		name, price = line.strip().split(',') # split切割完直接丟給name & price
		products.append([name, price])
print(products)
#讓使用者輸入
sum = 0
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    price = int(price)
    #p = [name, price]
    products.append([name, price])
print(products) 
#印出購買紀錄
for p in products:
	print(p[0], '的價格是', p[1], '元') 
#寫入檔案
with open ('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		sum = sum + int(p[1])
		f.write(p[0] + ',' + str(p[1]) +'\n')
print('目前花費總和: ', sum, '元')


