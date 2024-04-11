from django.shortcuts import render
from django.views import generic

from .models import Game


def index(request):
    games = Game.objects.all()
    # Pair up the games - convert the queryset into a list and then into pairs
    games_pairs = [games[i:i + 2] for i in range(0, len(games), 2)]
    return render(request, "games/index.html", {"games_pairs": games_pairs})


def game_detail(request, game_slug):
    return render(request, f"games/{game_slug}.html", {})
