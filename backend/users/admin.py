from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import FollowRelationship, User


class FollowToInline(admin.TabularInline):
    model = FollowRelationship
    fk_name = 'from_user'
    extra = 1
    verbose_name = 'Подписки'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [FollowToInline]
    list_display = ['id', 'username', 'email']
    search_fields = ['email', 'username']
    list_filter = ['email', 'username']
    empty_value_display = '-пусто-'
    list_display_links = ['id', 'username', 'email']


admin.site.register(FollowRelationship)
admin.site.unregister(Group)
