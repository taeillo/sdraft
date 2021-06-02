from flask import Flask, request, redirect, jsonify, render_template
import requests
import json
import pandas as pd
import random
import string

'''
cart = [['Product Name','Price','Color','Item Count']]


cart_df = pd.DataFrame(data = cart[1:], columns=cart[0])
cart_df['Total'] = cart_df['Price'] * cart_df['Item Count']

print(list(cart_df['Product Name']))

name_product = list(cart_df['Product Name'])
color_product = list(cart_df['Color'])
total_price = sum(list(cart_df['Total']))
item_count = list(cart_df['Item Count'])



def addCart(name,price,color,item):
	cart_df.append([name,price,color,item])

def removeCart(name):
	if name in list(cart_df['Product Name']):
		cart_df.drop(name, axis=0, inplace=True)

def clearCart():
	for i in range(cart_df.count()['Product Name']):
		cart_df.drop(labels=i, axis=0, inplace=True)


'''

product_list = {
	'jumi':{
		'price': 99999,'color':['Default'], 'src': 'jumi bed.jpg'
	},
	'jumi prime':{
		'price': 59999,'color':['Default'], 'src': 'jumi prime bed.jpg'
	},
	'ada':{
		'price': 150000,'color':['grey','yellow','blue','green','beige'], 'src': 'ada 2.jpg'
	},
	'amakisi duo wardrobe':{
		'price': 150000,'color':['default'], 'src': 'wardrobe.jpg'
	},
	'amakisi single wardrobe':{
		'price': 89999,'color':['default'], 'src': 'wardrobe.jpg'
	},
	'seyi 6-seater':{
		'price': 349999,'color':['default'], 'src': 'seyi-6-seater-sofa-sofas-28998819217568.jpg'
	},
	'alausa':{
		'price': 249999,'color':['grey','yellow','blue','green','beige'], 'src': 'alausa.jpg'
	},
	'amakisi':{
		'price': 34999,'color':['black','white'], 'src': 'amakisi table.jpg'
	},
	'amakisi drawer':{
		'price': 44999,'color':['black','white'], 'src': 'amakisi table with drawer.jpg'
	},
	'femi':{
		'price': 44999,'color':['grey','yellow','blue','green','beige'], 'src': 'femi.jpg'
	},
	'segun':{
		'price': 39999,'color':['default'], 'src': 'segun.jpg'
	},
	'amakisi duo':{
		'price': 89999,'color':['default'], 'src': 'amakisi duo.jpg'
	},
	'amakisi prime':{
		'price': 49999,'color':['default'], 'src': 'amakisi-prime-sofas-29001262006432.jpg'
	},
	'bosun':{
		'price': 90000,'color':['default'], 'src': 'bosun.jpg'
	},
	'amakisi vip':{
		'price': 69999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
	'amakisi table with Chair':{
		'price': 59999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
	'kemi combo':{
		'price': 279999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
	'segun combo':{
		'price': 54999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
	'alausa combo':{
		'price': 3499999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
}

#print('jumi price is: ', product_list['jumi']['price'])


app = Flask(__name__) 

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template('index.html')
    #return redirect(url_x, code=302)

@app.route('/paywithspecta', methods=['POST','GET'])
def order():
	product_list = {
	'jumi':{
		'price': 99999,'color':['Default'], 'src': 'jumi bed.jpg'
	},
	'jumi prime':{
		'price': 59999,'color':['Default'], 'src': 'jumi prime bed.jpg'
	},
	'ada':{
		'price': 150000,'color':['grey','yellow','blue','green','beige'], 'src': 'ada 2.jpg'
	},
	'amakisi duo wardrobe':{
		'price': 150000,'color':['default'], 'src': 'wardrobe.jpg'
	},
	'amakisi single wardrobe':{
		'price': 89999,'color':['default'], 'src': 'wardrobe.jpg'
	},
	'seyi 6-seater':{
		'price': 349999,'color':['default'], 'src': 'seyi-6-seater-sofa-sofas-28998819217568.jpg'
	},
	'alausa':{
		'price': 249999,'color':['grey','yellow','blue','green','beige'], 'src': 'alausa.jpg'
	},
	'amakisi':{
		'price': 34999,'color':['black','white'], 'src': 'amakisi table.jpg'
	},
	'amakisi drawer':{
		'price': 44999,'color':['black','white'], 'src': 'amakisi table with drawer.jpg'
	},
	'femi':{
		'price': 44999,'color':['grey','yellow','blue','green','beige'], 'src': 'femi.jpg'
	},
	'segun':{
		'price': 39999,'color':['default'], 'src': 'segun.jpg'
	},
	'amakisi duo':{
		'price': 89999,'color':['default'], 'src': 'amakisi duo.jpg'
	},
	'amakisi prime':{
		'price': 49999,'color':['default'], 'src': 'amakisi-prime-sofas-29001262006432.jpg'
	},
	'bosun':{
		'price': 90000,'color':['default'], 'src': 'bosun.jpg'
	},
	'amakisi vip':{
		'price': 69999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
	'amakisi table with Chair':{
		'price': 59999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
	'kemi combo':{
		'price': 279999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
	'segun combo':{
		'price': 54999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},
	'alausa combo':{
		'price': 3499999,'color':['default'], 'src': 'amakisi vip table.jpg'
	},

	}

	if request.method =="POST":
		req = request.form
		# printing digits
		preference = string.digits
		print ( ''.join(random.choice(preference) for i in range(10)) )
		preference = str(preference)

		price = int(req.get('quantity'))

		

		firstname = str(req.get('firstname'))
		lastname = str(req.get('lastname'))
		address = str(req.get('address'))
		emailaddress = str(req.get('emailaddress'))
		number = str(req.get('number'))
		quantity = str(req.get('quantity'))
		productname = str(req.get('proname'))
		#print('Product name: ',productname)
		note = str(req.get('note'))
		total_price = product_list[productname]['price'] * price
		total_price = str(total_price)

		description = f'Name of Customer: {firstname} {lastname} Shipping Address: {address} Email: {emailaddress} Phone Number: {number} Product Name: {productname} Number of items: {quantity} Note: {note}'

		url = "https://paywithspectaapi.sterling.ng/api/Purchase/CreatePaymentUrl"

		old_payload = {  "callBackUrl": "https://www.taeillo.com",    "reference": preference,   "merchantId": "117143",  "description": description,   "amount": total_price}

		payload = str(old_payload)


		headers = {
		  'x-ApiKey': 'TEST_API_KEY',
		  'content-type': 'application/json'
		}



		response = requests.request("POST", url, headers=headers, data=payload)

		url_x = response.json()
		print(url_x)
		#url_x = str(url_x['result'])
		return redirect(url_x['result'])

	
	return redirect(url_x['result'])
@app.route('/cart', methods=['POST','GET'])


def cart():
    return render_template('cart.html',product_list=product_list)























if __name__ == "__main__":
    app.run(debug=True, port=8080)
