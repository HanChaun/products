products = []
while True:
	name = input('pls input product name:')
	if name == 'q':
		break
	price = input('pls input product price:')
	products.append([name, price])
print(products)

