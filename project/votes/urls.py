from django.urls import path
from votes.views import VotesListView

app_name = 'votes'

urlpatterns = [
    path('', VotesListView.as_view())
]
