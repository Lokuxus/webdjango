from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import requests
import json



def helloview(request, word):
    # TODO: replace with your own app_id and app_key
    app_id = 'c03ae10f'
    app_key = '092d39a73cc7d1ee1248d57e7c65ce2d'

    language = str(request.GET.get('language',''))
    word_id = str(word)

    # print(language)

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    if r.status_code == 200:
        dados = r.json()
        aux = dados['results']
        # print("text \n" + r.text)
        if len(aux) > 0:
            try:
                aux = aux[0]['lexicalEntries']
                aux = aux[0]['entries']
                aux = aux[0]['senses']
                aux = aux[0]['definitions']
                aux = aux[0]
            except:
                aux = aux[0]['crossReferenceMarkers']
                aux = aux[0]
        else:
             aux = 'Word not found'
    else:
        aux = 'Word not found'
    #aux =
    #print("code {}\n".format(r.status_code))
    # print("text \n" + r.text)
    #print("json \n" + json.dumps(r.json()))
    return HttpResponse('Definicao de '+str(word)+': '+aux)