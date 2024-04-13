from django.views import generic
from django.shortcuts import render, get_object_or_404
from collections import OrderedDict


from .models import Weapon


def index_view(request, game_slug):
    game_id = convert_game_id(game_slug)

    categories = Weapon.objects.values_list('category', flat=True).distinct()

    # Sort the categories
    categories = sorted(categories)

    weapons_by_category = OrderedDict()

    for category in categories:
        weapons = Weapon.objects.filter(game_id=game_id, category=category).order_by('name')
        weapons_by_category[category] = list(weapons)

    weapon_list = Weapon.objects.filter(game_id=game_id).order_by('name')
    return render(request, "weapons/index.html",
                  {"weapon_list": weapon_list, "game_slug": game_slug, "game_id": game_id, "weapons_by_category": weapons_by_category})


def weapon_detail(request, game_slug, weapon_id):
    weapon = get_object_or_404(Weapon, id=weapon_id)
    updated_name = weapon.name.replace(' ', '_').replace("'", '_')
    context = {
        "weapon": weapon,
        "updated_weapon_name": updated_name
    }
    return render(request, "weapons/detail.html", context)


def convert_game_id(game_id):
    if game_id == 'elden_ring':
        game_id = 'Elden Ring'
    return game_id
