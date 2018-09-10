import os #operating system
#Read File
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if 'Products,Price' in line:
				continue
				name, price = line.strip().split(',')
				products.append([name, price])
		return products
#User input
def user_input(products):
	while True:
		name = raw_input('pls input product name:')
		if name == 'q':
			break
		price = raw_input('pls input product price:')
		products.append([name, price])
	print(products)
	return products
#Print Buy record
def print_products(products):
	for p in products:
		print(p[0], 'price is', p[1])
#Write File
def write_file(filename, products):
	with open(filename,'w') as f:
		f.write('Products,Price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah! find the file!')
		products = read_file(filename)
	else:
		print('Not found!')
		
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()


