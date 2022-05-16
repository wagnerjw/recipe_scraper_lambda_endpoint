import json
from recipe_scrapers import scrape_me

def lambda_handler(event, context):
    body = json.loads(event['body'])

    if 'recipeURL' not in body:
        return {
            'error': 'You must provide a url string'
        }

    if not is_string(body['recipeURL']):
        return {
            'error': 'Please enter a valid recipe URL'
        }

    recipeURL = body['recipeURL']

    scraper = scrape_me(recipeURL)

    title = scraper.title()
    total_time = scraper.total_time()
    ingredients = scraper.ingredients()
    instructions = scraper.instructions()
    yields = scraper.yields()
    image = scraper.image()
    host = scraper.host()
    nutrients = scraper.nutrients()

    return {
            'title' : title,
            'ingredients' : ingredients,
            'instructions' : instructions.replace("\n", " "),
            'yield' : yields,
            'image' : image,
            'host' : host,
            'nutrients' : nutrients,
    }

def is_string(value):
    """"Checks if value is an string."""
    return isinstance(value, str)