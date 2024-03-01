from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView
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
        'city'
        )
    template_name = 'votes/votes_create.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)