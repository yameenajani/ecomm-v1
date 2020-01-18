from django.contrib import admin

from .models import Product, ProductFile,ProductComments,ProductCategories,ProductFAQ


class ProductFileInline(admin.TabularInline):
    model = ProductFile
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'is_digital']
    inlines = [ProductFileInline]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductComments)
admin.site.register(ProductCategories)
admin.site.register(ProductFAQ)