import json
from recipe_scrapers import scrape_me

recipeURL = input("Enter Recipe URL Here:... ")

scraper = scrape_me(recipeURL)

title = scraper.title()
total_time = scraper.total_time()
ingredients = scraper.ingredients()
instructions = scraper.instructions()
yields = scraper.yields()
image = scraper.image()
host = scraper.host()
nutrients = scraper.nutrients()

recipeComponents ={
  'title' : title,
  'ingredients' : ingredients,
  'instructions' : instructions.replace("\n", " "),
  'yield' : yields,
  'image' : image,
  'host' : host,
  'nutrients' : nutrients,
}

json_object = json.dumps(recipeComponents, indent = 4)

print(json_object)


