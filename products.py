import os #operating system

#Read File
products = []
if os.path.isfile('products.csv'):
	print('yeah! find the file!')
	with open('products.csv', 'r') as f:
		for line in f:
			if 'Products,Price' in line:
				continue
				name, price = line.strip().split(',')
				products.append([name, price])
				print(products)
else:
	print('Not found!')
#User input
products = []
while True:
	name = raw_input('pls input product name:')
	if name == 'q':
		break
	price = raw_input('pls input product price:')
	products.append([name, price])
print(products)
#Print Buy record
for p in products:
	print(p)
	print(p[0], 'price is', p[1])
#Write File
with open('products.csv','w') as f:
	f.write('Products,Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')