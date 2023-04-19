from django.contrib import admin

from .models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductAttributeValues,
    ProductInventory,
    ProductType,
    Stock,
)

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductAttributeValues)
admin.site.register(ProductInventory)
admin.site.register(ProductType)
admin.site.register(Stock)
