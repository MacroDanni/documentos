import json
from urllib import response
import requests
from fastapi import FastAPI


app = FastAPI()

client_api   = "https://api.copomex.com/"
#token="token=99b91a25-18cd-4c7d-a1d4-fb7c7e97605a"
token="token=pruebas"

class Punto:
 
    def get_cp_municipio():
      info_clave="query/get_cp_por_municipio/Puebla?"
      url=client_api+info_clave+token
      data = requests.get(url)
      array_munisipios=[]
      data = data.json()
      for element in data['response']['cp']:
        array_munisipios.append((element,element))
      return array_munisipios



    def get_colonia_por_cp():
        info_clave="query/get_colonia_por_cp/72000?"
        url=client_api+info_clave+token
        data = requests.get(url)
        array_munisipios=[]
        data = data.json()
        for element in data['response']['colonia']:
          array_munisipios.append((element,element))
        return array_munisipios

 

