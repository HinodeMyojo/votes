from django.urls import path
from votes.views import PollCreateView, PollListView, PollDetailView
app_name = 'votes'

urlpatterns = [
    path('create/', PollCreateView.as_view(), name='create_polls'),
    path('', PollListView.as_view(), name='list_polls'),
    path('detail/<uuid:pk>/', PollDetailView.as_view(), name='detail_polls'),
#     path('create/', CreatePoll.as_view(), name='create_poll'),
#     path('<uuid:vote_id>/', DetailPoll.as_view(), name='detail_poll'),
#     path('<uuid:vote_id>/edit/', EditPoll.as_view(), name='edit_poll')
]