from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
#  Slug: a URL-friendly version of a string, typically used in URLs.


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(default="Unkonwn" ,max_length=100)
    author = models.CharField(null=True ,max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # db_index = True => 그 열에 대해 색인을 만들어서 검색 성능 향상 (id로 검색하지 않으면 검색 느림)
    slug = models.SlugField(default="", null=False, db_index=True) # Harry Potter 1 => harry-potter-1
    # we chaneged model so need to migrate (shell)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # slugify() converts the title (like "Harry Potter 1") to a slug (like "harry-potter-1") and That value is stored in the slug field
        super().save(*args, **kwargs) # Calls the original save() method to actually store the object in the database => shell 에서 book.save()를 직접 호출해야만 실행됨ㄴ
        # Overrinding: redefining a method that already exists in a parent class to change or extend its behavior in a child class.

    def __str__(self): # 객체를 문자열로 어떻게 표현할지 정의해주는 특수 메서드
        return f"{self.title} ({self.rating})"