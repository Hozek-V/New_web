from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn",)


admin.site.register(Books, BooksAdmin)