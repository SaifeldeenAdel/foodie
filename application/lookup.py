import requests
import json
import urllib.parse


def lookup(query):
    list=[]
    response = requests.get(f"https://api.edamam.com/search?q=<{query}>&app_id=0ff1d262&app_key=c84fc9e6ae74acd249affc2099c6c059")
    response.raise_for_status()

    recipe = response.json()
    for i in range(len(recipe['hits'])):
        list.append({'name': recipe['hits'][i]['recipe']['label'],
                     'uri': recipe['hits'][i]['recipe']['uri'],
                     'url': recipe['hits'][i]['recipe']['url'],
                     'image': recipe['hits'][i]['recipe']['image'],
                     'ingredients': recipe['hits'][i]['recipe']['ingredientLines']})
    return list

def recipe_encode(recipe_uri):
    response = requests.get(f"https://api.edamam.com/search?r={urllib.parse.quote_plus(recipe_uri, safe='')}&app_id=0ff1d262&app_key=c84fc9e6ae74acd249affc2099c6c059")
    recipe = response.json()
    return {
        'uri': recipe[0]['uri'],
        'name': recipe[0]['label'],
        'image': recipe[0]['image'],
        'url': recipe[0]['url'],
        'ingredients': recipe[0]['ingredientLines'],
        'yield': recipe[0]['yield'],
        'calories': recipe[0]['calories']

    }

