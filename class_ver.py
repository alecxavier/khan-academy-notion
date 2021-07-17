
import os
from types import MethodType
import requests
from bs4 import BeautifulSoup
from requests.api import post



get = requests.get('https://httpbin.org/forms/post').text
par = BeautifulSoup(get, "lxml")

print(par.prettify())

form = par.find('form', MethodType=post)
input = form.find('input', name="custname")

requests.put('https://httpbin.org/forms/post', '')