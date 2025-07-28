from django.db import models
#from django.core.validators import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"
    # verbose_name_plural -> 모델의 복수형 이름을 직접 지정하는 데 사용

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    # OneToOneField -> 두 모델 간에 1:1 관계를 설정할 때 사용
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    #author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    # ForeignKey -> one-to-many-relationships, 여기서는 하나의 author 가 여러개의 Book 을 쓸수있도록
    # related_name -> ForeignKey 필드에서 역참조를 할 수 있는 이름 설정
    
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)
    
    published_countries = models.ManyToManyField(Country, null=False)
    # ManyToManyField -> 두 모델이 서로 여러 개의 객체를 가질 수 있는 관계, 예) 학생 여러 수업 참여 가능, 하나의 수업엔 여러 학생이 수강가능

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"