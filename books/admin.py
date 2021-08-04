from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book) # just display title


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price",)


admin.site.register(Book, BookAdmin)
