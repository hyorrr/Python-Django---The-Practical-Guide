from django.contrib import admin
from .models import Book

# Register your models here.

# 장고 관리자 페이지에서 Book 모델을 어떻게 보여줄지 커스터마이징해주는 클래스
class BookAdmin(admin.ModelAdmin):
    # prepopulated_fields: slug 필드를 title 필드 기반으로 자동으로 채워주게 하는 설정
    prepopulated_fields = {"slug": ("title",)}
    # list_filter: 입력한 필드에 따라 필터 검색 기능
    list_filter = ("author", "rating",)
    # list_display: 입력한 필드를 테이블에 보여줌
    list_display = ("title", "author",)
    

admin.site.register(Book, BookAdmin)
# admin.site.register(Book)