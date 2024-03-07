
from django.views import generic

# def index(request):
#     return render(request, template_name="weapons/detail.html", context={})

from .models import Weapon


class IndexView(generic.ListView):
    template_name = "weapons/index.html"
    context_object_name = "weapon_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Weapon.objects.all()


class DetailView(generic.DetailView):
    model = Weapon
    template_name = "weapons/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()

        # Replace space characters with underscores
        updated_name = obj.name.replace(' ', '_')
        # Replace ' characters with underscores
        updated_name = updated_name.replace("'", '_')

        # Add both versions of the weapon name to the context
        context['weapon_name'] = obj.name
        context['updated_weapon_name'] = updated_name
        return context
