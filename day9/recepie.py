from flask import Flask, render_template, request
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

def search_recipe(keyword):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meals = data.get('meals', [])
        return meals
    else:
        print("Error fetching recipe data.")
        return []

def display_recipe_details(recipe_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meal = data['meals'][0]
        return meal
    else:
        print("Error fetching recipe details.")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        recipes = search_recipe(keyword)
        return render_template('search_results.html', recipes=recipes)
    return render_template('index.html')

@app.route('/display_recipe/<recipe_id>', methods=['GET'])
def display_recipe(recipe_id):
    recipe = display_recipe_details(recipe_id)
    if recipe:
        return render_template('recipe_details.html', recipe=recipe)
    else:
        return "Recipe details not found."

if __name__ == "__main__":
    app.run(debug=True)
