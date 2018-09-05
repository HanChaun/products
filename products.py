products = []
while True:
	name = input('pls input product name:')
	if name == 'q':
		break
	price = input('pls input product price:')
	products.append([name, price])
print(products)

for p in products:
	print(p)
	print(p[0], 'price is', p[0])