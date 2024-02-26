from django.views.generic import ListView


class VotesListView(ListView):
    template_name = "list.html"