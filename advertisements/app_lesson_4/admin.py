from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date', 'user', 'loaded_image']
    list_filter = ['price', 'creat_at']
    actions = ['make_auction_as_true', 'make_auction_as_false']

    fieldsets = (
        ('Общие', {'fields': ('title', 'description', 'user', 'image')}),
        ('Финансы', {'fields': ('price', 'auction'), 'classes': ['collapse']})
    )
    @admin.action(description= 'Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update (auction = True)

    @admin.action(description= 'Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update (auction = False)

admin.site.register(Advertisement, AdvertisementAdmin)