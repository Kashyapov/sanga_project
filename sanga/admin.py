from django.contrib import admin
from models import Sadhu, SignMonk, StatusVidyaSadhana, StatusBhakti, StatusDonate, Level, Citizenship, RatingSadhu, \
    Country, Town, AdditionalCharacteristic, SadhuAdditional
from sanga_project import settings


class SadhuAdditionalInline(admin.StackedInline):
    model = SadhuAdditional
    StackedInline = 'sadhu'


class RatingSadhuInline(admin.TabularInline):
    model = RatingSadhu
    fk_name = 'rating_to'
    extra = 1


class SadhuAdmin(admin.ModelAdmin):

    # date_hierarchy = "date_ankety"
    list_display = ('username', 'spiritual_name', 'last_name', 'first_name', 'middle_name')
    # list_filter = ('priznak_monk', 'country', 'town', 'status_vidya', 'status_v_slugenii', 'status_gertvovatilya')
    search_fields = ('username', 'spiritual_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('username',
                           'spiritual_name', 'last_name', 'first_name','middle_name',
                           'date_joined', 'is_active',
                           'is_staff', 'is_superuser', 'password')}),
    )

    inlines = [
            SadhuAdditionalInline, RatingSadhuInline,
    ]

# Register your models here.
admin.site.register(Sadhu, SadhuAdmin)
admin.site.register(StatusVidyaSadhana)
admin.site.register(StatusBhakti)
admin.site.register(StatusDonate)
admin.site.register(Level)
admin.site.register(Citizenship)
admin.site.register(AdditionalCharacteristic)
admin.site.register(RatingSadhu)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(SignMonk)
admin.site.register(SadhuAdditional)
