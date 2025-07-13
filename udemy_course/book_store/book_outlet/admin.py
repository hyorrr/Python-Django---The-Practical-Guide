from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",) # can see slug data on site not allowing editing
    prepopulated_fields = {"slug": ("title",)} # 사용하려면 editable=False 지우기
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)

    

# admin.site.register(Book)
admin.site.register(Book,BookAdmin)