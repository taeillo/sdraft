from flask import Flask, request, redirect, jsonify, render_template
import requests
import json
import pandas as pd


new_url =	"https://taeillo.com/cart.json"	 #"https://e9d392ea47c9a5cbf914426a4845082a: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@taeillo-online.myshopify.com/admin/api/2021-04/cart.js"
r = requests.get(new_url)

data = r.json()

'''

product_list = []

for item in data['products']:
	print(item['title'])

for item in data['products']:
	title = item['title']
	product_id = item['id']
	product_type = item['product_type']
	for image in item['images']:
			src = image['src']
	for variant in item['variants']:
		try:
			price = variant['price']

			variant_id = variant['product_id']
			variant_title = variant['title']

			product = {
				'Title':title,
				'Product_Id': product_id,
				'Product_Type':product_type,
				'Variant_Title':variant_title,
				'Variant_Id': variant_id,
				'Price':price,
				'Image':src,

			}

			product_list.append(product)

		except:
			variant['product_id'] = 'None'




#print(product_list)
df = pd.DataFrame(product_list)
df.to_csv('shopify.csv', index=False)
print("Successful!!!")
print(df)

print(data)
'''
reference = str(data['token'])
prices = str(data['original_total_price'])
prices = prices[:-2]
note = str(data['items'])





url = "https://paywithspectaapi.sterling.ng/api/Purchase/CreatePaymentUrl"

old_payload = {  "callBackUrl": "https://www.taeillo.com",    "reference": reference,   "merchantId": "117143",  "description": note,   "amount": prices}

payload = str(old_payload)


headers = {
  'x-ApiKey': 'TEST_API_KEY',
  'content-type': 'application/json'
}



response = requests.request("POST", url, headers=headers, data=payload)

url_x = response.json()
#print(url_x)
url_x = str(url_x['result'])



app = Flask(__name__) 

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template('index.html')
    #return redirect(url_x, code=302)

@app.route('/order', methods=['POST','GET'])
def order():
	return redirect(url_x, code=302)
   



if __name__ == "__main__":
    app.run(debug=True, port=8080)
