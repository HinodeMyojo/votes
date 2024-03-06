from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from votes.models import Poll
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from votes.forms import PollForm

User = get_user_model()


class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form = PollForm
    fields = (
        'headline',
        'essence',
        'text',
        'image',
        'mode',
        'type',
        'category',
        'city',
        )
    template_name = 'votes/poll_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PollListView(ListView):
    model = Poll
    paginate_by = 20
    template_name = 'votes/poll_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PollDetailView(DetailView):
    model = Poll