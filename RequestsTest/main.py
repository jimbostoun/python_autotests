import requests
import json

token = 'c202e72f48271c7d0aca9d8c22a1af49'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Ромашка",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 5687,
    "name": "Клевер"
})

print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": "5687"
})

print(response_post.text) 