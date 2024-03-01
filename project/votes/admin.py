from django.contrib import admin

from votes.models import Category, Vote, Poll


admin.site.register(Category)
admin.site.register(Vote)
admin.site.register(Poll)
