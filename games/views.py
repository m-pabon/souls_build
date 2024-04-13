from django.shortcuts import render


def game_detail(request, game_slug):
    return render(request, f"games/{game_slug}.html", {"game_slug": game_slug})
