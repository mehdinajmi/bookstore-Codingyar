from django.urls import path , include

from .views import BookListView, BookCreateView,BookUpdateView,BookDeleteView,book_detail_view


urlpatterns = [
    path('',BookListView.as_view(),name='book_list'),
    path('<int:pk>/', book_detail_view, name="book_detail"),
    path('create/', BookCreateView.as_view() , name='book_create'),
    path('<int:pk>/update/', BookUpdateView.as_view() , name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete')
]