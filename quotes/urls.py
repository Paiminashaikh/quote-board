from django.urls import path
from .views import (
    home,
    add_quote,
    list_quotes,
    edit_quote,
    delete_quote,
    quotes_by_author,
    like_quote
)

   # ✅ Optional: helps if project has multiple apps

urlpatterns = [
    path('', home, name='home'),  # 🏠 Home with random quote
    path('add/', add_quote, name='add_quote'),  # ➕ Add Quote
    path('all/', list_quotes, name='list_quotes'),  # 📄 All Quotes with Search
    path('edit/<int:pk>/', edit_quote, name='edit_quote'),  # ✏️ Edit
    path('delete/<int:pk>/', delete_quote, name='delete_quote'),  # 🗑 Delete
    path('author/<str:author>/', quotes_by_author, name='quotes_by_author'),  # 📂 Filter
    path('like/<int:pk>/', like_quote, name='like_quote'),  # ❤️ Like
]
