from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import requests
import json
import tweepy
import re

app_id = ''
app_key = ''

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
REGEX = r'\b\w+\b'

def helloview(request, word):
    # TODO: replace with your own app_id and app_key

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    tweet = api.search(q=str(word), lang=str(request.GET.get('language', '')), count=1, tweet_mode='extended')
    print(tweet)

    data = tweet[0]._json['full_text']
    lista_palavras = re.findall(REGEX, data)
    print(tweet[0]._json['user']['screen_name'])
    print(lista_palavras)
    language = str(request.GET.get('language', ''))
    word_id = str(word)

    # print(language)
    definicoes = []
    for palavra in lista_palavras:
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + palavra.lower()

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
        definicoes.append(aux)
        definicoes.append('\n')
    # aux =
    # print("code {}\n".format(r.status_code))
    # print("text \n" + r.text)
    # print("json \n" + json.dumps(r.json()))
    # return HttpResponse('Definicao de '+str(word)+': '+aux)
    return HttpResponse(definicoes)
