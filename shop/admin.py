from django.contrib import admin
from shop.models import UserProfiles,Blog,Comment,Product
# Register your models here.


admin.site.site_header = "My Shop"
admin.site.site_title = "Manage this shop"
admin.site.index_title = "Welcome to Dashboard"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','date_added','product_description','product_price','product_image','discount_price')
    search_fields = ('product_name','product_description')
    list_editable =('product_price','discount_price','product_image')


admin.site.register(UserProfiles)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Product,ProductAdmin)