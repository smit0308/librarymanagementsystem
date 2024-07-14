from django.http import HttpResponse
from django.shortcuts import redirect, render
import http.client
import json
import logging
from app1.models import librarian, reader, Booked
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

logger = logging.getLogger(__name__)



import http.client
import urllib.parse
import json
from django.shortcuts import render

def fetch_books_from_api():
    conn = http.client.HTTPSConnection("all-books-api.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "0c0393d662mshb446aa2c351340dp198f0bjsn1a7dfd746322",
        'x-rapidapi-host': "all-books-api.p.rapidapi.com"
    }

    conn.request("GET", "/getBooks", headers=headers)
    res = conn.getresponse()
    data = res.read()

    books_data = data.decode("utf-8")

    books = json.loads(books_data)

    return books

def search_bk(request):
    books = fetch_books_from_api()

    if request.method == 'POST':
        search_term = request.POST.get('search_term')

        if search_term:
            if search_term.isdigit():
                endpoint = f"/isbn/{search_term}"
            else:
                encoded_author = urllib.parse.quote(search_term)
                endpoint = f"/author/{encoded_author}"

            conn = http.client.HTTPSConnection("all-books-api.p.rapidapi.com")
            headers = {
                'x-rapidapi-key': "0c0393d662mshb446aa2c351340dp198f0bjsn1a7dfd746322",
                'x-rapidapi-host': "all-books-api.p.rapidapi.com"
            }

            conn.request("GET", endpoint, headers=headers)
            res = conn.getresponse()
            data = res.read()

            books = [json.loads(data.decode("utf-8"))]

    return render(request, 'all_books.html', {'books': books})

def home(request):
    first_five_books = []

    try:
        conn = http.client.HTTPSConnection("all-books-api.p.rapidapi.com")

        headers = {
            'x-rapidapi-key': "0c0393d662mshb446aa2c351340dp198f0bjsn1a7dfd746322",
            'x-rapidapi-host': "all-books-api.p.rapidapi.com"
        }

        conn.request("GET", "/getBooks", headers=headers)
        res = conn.getresponse()
        data = res.read()

        if res.status == 200:
            books_data = json.loads(data.decode("utf-8"))

            first_five_books = books_data[:5]

    except Exception as e:
        print(f"Error fetching books: {e}")

    return render(request, 'index.html', {'first_five_books': first_five_books})

def search(request):
    return render(request, 'search.html')

def user(request):
    current_user = request.user

    read = reader.objects.filter(user=current_user).first()
    booked_books = Booked.objects.filter(reader=read) if read else []
    return render(request, 'user.html', {'user': current_user, 'read': read, 'booked_books': booked_books})

def logout_view(request):
    logout(request)
    return redirect('/')

def registerform(request):
    return render(request, 'registerform.html')

def about(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")

def get_books(request):
    conn = http.client.HTTPSConnection("goodreads12.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "0c0393d662mshb446aa2c351340dp198f0bjsn1a7dfd746322",
        'x-rapidapi-host': "all-books-api.p.rapidapi.com"
    }

    conn.request("GET", "/getBooks", headers=headers)

    res = conn.getresponse()
    data = res.read()
    books = json.loads(data.decode("utf-8"))

    return render(request, 'books.html', {'books': books})

import http.client

import http.client
import urllib.parse
from django.shortcuts import render

def search_books(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')

        if search_term.isdigit():

            endpoint = f"/isbn/{search_term}"
        else:

            encoded_author = urllib.parse.quote(search_term)
            endpoint = f"/author/{encoded_author}"

        conn = http.client.HTTPSConnection("all-books-api.p.rapidapi.com")

        headers = {
            'x-rapidapi-key': "0c0393d662mshb446aa2c351340dp198f0bjsn1a7dfd746322",
            'x-rapidapi-host': "all-books-api.p.rapidapi.com"
        }

        conn.request("GET", endpoint, headers=headers)
        res = conn.getresponse()
        data = res.read()

        books = []
        if res.status == 200:
            books.append(data.decode("utf-8"))

        return render(request, 'search_results.html', {'books': books})

    return render(request, 'search_books.html')

@login_required
def add_booked(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name')
        current_user = request.user
        
        reader_instance = reader.objects.filter(user=current_user).first()

        if reader_instance:
            booked = Booked(
                reader=reader_instance,
                book_name=book_name,
                author_name=author_name,
                allocated_date=timezone.now(), 
                due_date=timezone.now() + timezone.timedelta(days=30) 
            )
            booked.save()
            return redirect('home')  
        else:
            return redirect('home')  

    return redirect('home') 

