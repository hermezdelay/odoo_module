import datetime
import zeep
from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth
import pandas as pd
from base64 import b64encode
import array


def basic_auth(username, password):
  token = b64encode(
      ("%s:%s" % (username, password)).encode('utf-8')).decode('utf-8')
  #creds = (username + ":" + password)
  return token


wsdl = "https://armoires.zeendoc.com/tests_webservices/ws/3_0/wsdl.php?WSDL"
username = "tests_webservices@zeendoc.com"
password = "tests01"
UserId = "dce7e842799c87494481f8827c2876a0"


session = Session()
session.auth = HTTPBasicAuth(username, password)
client = Client(wsdl, transport=Transport(session=session))

Access_token = basic_auth(username, password)
print("token =" + Access_token)

print(
    client.service.login("tests_webservices@zeendoc.com", "", "tests01", Access_token))

id_armoire = 13547
Coll_Id = "coll_3"
Column_Name = "custom_n1"

id_item = {'id': 12}
Label_item = {'Label': 'Droits divers'}
List_Item1 = ['List_Item', [id_item, Label_item]]


print(List_Item1)

print(client.service.addItemsList(Coll_Id, Column_Name, List_Item1, Access_token))