from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import Sadhu, StatusVidyaSadhahy, StatusVSlugenii, StatusGertvovatilya, Stupen, Gragdanstvo, RatingSadhu, \
    Country, Town, PriznakMonk, AdditionalCharacteristic


class RatingSadhuInline(admin.TabularInline):
    model = RatingSadhu
    fk_name = 'rating_to'
    extra = 1

class SadhuAdmin(admin.ModelAdmin):

    # date_hierarchy = "date_ankety"
    # list_display = ('username', 'spiritual_name', 'last_name', 'first_name', 'middle_name', 'country', 'town', 'email',
    #                 'rating_sum')
    # list_filter = ('priznak_monk', 'country', 'town', 'status_vidya', 'status_v_slugenii', 'status_gertvovatilya')
    # search_fields = ('username', 'spiritual_name', 'last_name')
    #
    # fieldsets = (
    #     (None, {'fields': ('username',
    #                        'spiritual_name', 'last_name', 'first_name','middle_name',
    #                        'priznak_monk',
    #                        'country', 'town', 'address',
    #                        'status_vidya', 'status_v_slugenii',
    #                        'status_gertvovatilya', 'primechanie',
    #                        'date_ankety', 'phone', 'soc_login', 'email',
    #                        'image',
    #                        'stupen', 'simvol_very', 'pribegishe', 'gragdanstvo', 'obrazovanie',
    #                        'den_rogdeniya', 'mesto_rogdeniya',
    #                        'max_add_rating',
    #                        'additional_characteristic',
    #                        'date_joined', 'is_active',
    #                        'is_staff', 'is_superuser', 'password')}),
    # )

    inlines = [
            RatingSadhuInline,
    ]

# Register your models here.
admin.site.register(Sadhu, SadhuAdmin)
admin.site.register(StatusVidyaSadhahy)
admin.site.register(StatusVSlugenii)
admin.site.register(StatusGertvovatilya)
admin.site.register(Stupen)
admin.site.register(Gragdanstvo)
admin.site.register(AdditionalCharacteristic)
admin.site.register(RatingSadhu)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(PriznakMonk)
