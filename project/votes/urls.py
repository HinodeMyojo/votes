from django.urls import path
from votes.views import PollCreateView
app_name = 'votes'

urlpatterns = [
    path('create/', PollCreateView.as_view(), name='create_polls'),
#     path('create/', CreatePoll.as_view(), name='create_poll'),
#     path('<uuid:vote_id>/', DetailPoll.as_view(), name='detail_poll'),
#     path('<uuid:vote_id>/edit/', EditPoll.as_view(), name='edit_poll')
]