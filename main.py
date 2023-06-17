from urllib import response
# https://jsonplaceholder.typicode.com/  strona do zapytan
import requests  # jak nie ma biblioteki instalujemy

response = requests.get('https://jsonplaceholder.typicode.com/posts/10')

if (response.status_code != requests.codes.ok):#obsluga statusu np gdyby wyjsc poza zakres
   print("Wystąpil jakis problem")
else:
    print(response.json())
#-----------------------------
requestBody = {
    'title': 'Tytul',
    'body': 'Tresc posta ',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts',json=requestBody)
if (response.status_code != requests.codes.created):#obsluga statusu np gdyby wyjsc poza zakres
   print("Wystąpil jakis problem")
else:
    print(response.json())