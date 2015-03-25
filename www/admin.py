# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User
from www.models import UserProfile, Rating, Categories, Tovar, Pictures, Comments, Bets
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

class UserProfileInline (admin.TabularInline):
    model = UserProfile


class UserAdmin(DjangoUserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_staff')
    list_display_links = ('email', 'username')
    ordering = ('-id',)
    inlines = [
        UserProfileInline,
    ]


def set_last(self, request, queryset):
    last_str = Categories.objects.last()
    set_last.short_description = 'Поставити в кінець'
    queryset.update(id=last_str.id + 1)


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name',)
    actions = [set_last]


class PictureInline(admin.TabularInline):
    model = Pictures


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('pic_name', 'pic_path', 'get_thumbnail_html')


class TovarAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline,
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tovar, TovarAdmin)
admin.site.register(Rating)
admin.site.register(UserProfile)
admin.site.register(Categories, CatAdmin)
admin.site.register(Pictures, PicturesAdmin)
admin.site.register(Comments)
admin.site.register(Bets)





# Register your models here.
