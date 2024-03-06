from django.contrib import admin

from votes.models import Category, Vote, Poll, VoteOption


admin.site.register(Category)
admin.site.register(Vote)
admin.site.register(VoteOption)
admin.site.register(Poll)
