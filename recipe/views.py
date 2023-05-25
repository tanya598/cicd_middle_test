
from django.shortcuts import render
from .models import Recipe, Category
from random import sample

def main(request):
    random_recipes = sample(list(Recipe.objects.all()), 10)
    context = {
        'recipes': random_recipes
    }
    return render(request, 'main.html', context)

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    recipes = category.recipes.all()
    context = {
        'category': category,
        'recipes': recipes
    }
    return render(request, 'category_detail.html', context)
