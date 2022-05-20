from recipe_scrapers import scrape_me
import json

recipeURL = ""

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'POST':
        
        body = json.loads(event['body'])
        
        if body['recipeURL'] == '':
            return {
                'statusCode' : 400,
                'Error' : 'I need a recipe URL, chef!'
            }
        else: 
            recipeURL = body['recipeURL']

    else: 
        return {
            'statusCode': 405,
            'Error': 'Wrong Method, Ya Idiot Sandwich!' 
        }
        
    return {
        'statusCode' : 200,
        'Recipe' : json.dumps(scrapeRecipe(recipeURL,))
    }
    
def scrapeRecipe(recipeURL):
    scraper = scrape_me(recipeURL)

    title = scraper.title()
    ingredients = scraper.ingredients()
    instructions = scraper.instructions()
    host = scraper.host()

    recipe = {
            'title':title,
            'ingredients' : ingredients,
            'instructions' : instructions.replace("\n", " "),
            'host' : host,
    }
    
    return recipe
    