from django.views.generic import ListView


class ListPolls(ListView):
    template_name = "list.html"