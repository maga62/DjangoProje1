from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Images
class ProdctImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status',]
    list_filter = ['status']

#     readonly calismiyor sebeb ben kendim iliskisinin kurmamishim

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price','amount' ,'image_tag' ,'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [ProdctImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product','image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)

