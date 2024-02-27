from django.urls import path
from votes.views import ListPolls
app_name = 'votes'

urlpatterns = [
    path('list/', ListPolls.as_view(), name='list_polls'),
#     path('create/', CreatePoll.as_view(), name='create_poll'),
#     path('<uuid:vote_id>/', DetailPoll.as_view(), name='detail_poll'),
#     path('<uuid:vote_id>/edit/', EditPoll.as_view(), name='edit_poll')
]