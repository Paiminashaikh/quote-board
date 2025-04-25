from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm
from .models import Quote
from django.db import models
from django.contrib import messages
import random

def home(request):
    quotes = list(Quote.objects.all())
    random_quote = random.choice(quotes) if quotes else None
    return render(request, 'quotes/home.html', {'quote': random_quote})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Quote added successfully!")  # ✅ inside POST
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def list_quotes(request):
    query = request.GET.get('q')
    if query:
        quotes = Quote.objects.filter(
            models.Q(content__icontains=query) |
            models.Q(author__icontains=query)
        ).order_by('-created_at')
    else:
        quotes = Quote.objects.order_by('-created_at')
    
    return render(request, 'quotes/list_quotes.html', {
        'quotes': quotes,
    })

def edit_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            messages.success(request, "Quote updated successfully!")  # ✅ inside POST
            return redirect('list_quotes')
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'quotes/edit_quote.html', {'form': form, 'quote': quote})

def delete_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        quote.delete()
        messages.success(request, "Quote deleted successfully!")  # ✅ added
        return redirect('list_quotes')
    return render(request, 'quotes/confirm_delete.html', {'quote': quote})

def quotes_by_author(request, author):
    quotes = Quote.objects.filter(author=author).order_by('-created_at')
    return render(request, 'quotes/quotes_by_author.html', {'quotes': quotes, 'author': author})

def like_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    quote.likes += 1
    quote.save()
    messages.success(request, "You liked this quote!")
    return redirect('list_quotes')
