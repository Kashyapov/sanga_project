from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from sorl.thumbnail.admin import AdminImageMixin
from models import Sadhu, StatusVidyaSadhahy, StatusVSlugenii, StatusGertvovatilya, Stupen, Gragdanstvo, Samaya, RatingSadhu, \
    Country, Town, PriznakMonk


class RatingSadhuInline(admin.TabularInline):
    model = RatingSadhu
    fk_name = 'rating_to'
    extra = 1

class MyUserAdmin(UserAdmin):
    date_hierarchy = "date_ankety"
    list_display = ('username', 'spiritual_name', 'last_name', 'first_name', 'middle_name', 'country', 'town', 'email',
                    'rating_sum')
    list_filter = ('samaya', 'priznak_monk', 'country', 'town', 'status_vidya', 'status_v_slugenii', 'status_gertvovatilya')
    search_fields = ('username', 'spiritual_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('username',
                           'spiritual_name', 'last_name', 'first_name','middle_name',
                           'priznak_monk',
                           'samaya', 'country', 'town', 'address',
                           'status_vidya', 'status_v_slugenii',
                           'status_gertvovatilya', 'primechanie',
                           'date_ankety', 'phone', 'soc_login', 'email',
                           'image',
                           'stupen', 'simvol_very', 'pribegishe', 'gragdanstvo', 'obrazovanie',
                           'den_rogdeniya', 'mesto_rogdeniya',
                           'max_add_rating',
                           'date_joined', 'is_active',
                           'is_staff', 'is_superuser', 'password')}),
    )

    inlines = [
            RatingSadhuInline,
    ]

# Register your models here.
# admin.site.register(Sadhu, UserAdmin)
admin.site.register(get_user_model(), MyUserAdmin)
admin.site.register(StatusVidyaSadhahy)
admin.site.register(StatusVSlugenii)
admin.site.register(StatusGertvovatilya)
admin.site.register(Stupen)
admin.site.register(Gragdanstvo)
admin.site.register(Samaya)
admin.site.register(RatingSadhu)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(PriznakMonk)
