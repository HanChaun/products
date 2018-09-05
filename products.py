products = []
while True:
	name = raw_input('pls input product name:')
	if name == 'q':
		break
	price = raw_input('pls input product price:')
	products.append([name, price])
print(products)

for p in products:
	print(p)
	print(p[0], 'price is', p[0])

with open('products.csv','w') as f:
	f.write('Products,Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')