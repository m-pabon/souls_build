from django.shortcuts import render

from games.models import Game


def index(request):
    games = Game.objects.all()
    games_pairs = [games[i:i + 2] for i in range(0, len(games), 2)]
    return render(request, "souls_build/index.html", {"games_pairs": games_pairs})
