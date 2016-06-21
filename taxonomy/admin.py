from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from taxonomy.models import Taxon

class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 40

admin.site.register(
    Taxon,
    CustomMPTTModelAdmin,
    list_display=(
        'name',
        'rank',
    )
)
