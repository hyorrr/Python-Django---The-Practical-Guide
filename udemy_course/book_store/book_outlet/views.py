from django.shortcuts import get_object_or_404,render
from .models import Book
from django.http import Http404
from django.db.models import Avg, Max, Min

# Create your views here.

def index(request):
    # books = Book.objects.filter() # without condition, it means Book.objects.all()
    # books = Book.objects.all()
    books = Book.objects.all().order_by("title") # reversed: books = Book.objects.all().order_by("-title")
    num_books = books.count()
    # avg_rating = books.aggregate(Avg("rating"), Min("rating")) #  rating__Avg, rating__min
    avg_rating = books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })

#def book_detail(request, id):
def book_detail(request, slug):
    # book = Book.objects.get(pk=id)
    # book = get_object_or_404(Book, pk=id) # Book 테이블에서 id에 해당하는 레코드를 찾아서 그 레코드를 Book 모델의 인스턴스로 반환해주는 함수, 만약 해당 id가 없으면 → 404 에러를 자동 발생
    book = get_object_or_404(Book, slug=slug) 
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })