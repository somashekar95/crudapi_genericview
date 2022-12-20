
from django.contrib import admin
from django.urls import path
from library.views import bookList,bookDetail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books', bookList.as_view()),
    path('api/books/<int:pk>',bookDetail.as_view()),
]


