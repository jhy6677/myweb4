import requests
import base64
from pprint import pprint

APPCODE = 'f239ccawf37f287418a90e2f922649273c4'

url = 'http://ali-checkcode.showapi.com/checkcode'
img_data = open('code.png','rb').read()

form ={}

form['convert_to_jpg'] = '0'
form['img_base64'] = base64.b64encode(img_data)
form['typeId'] = '3040'

headers={'Authorization':'APPCODE'+APPCODE}
response = requests.post(url,headers=headers,data=form)
pprint(response.json())
