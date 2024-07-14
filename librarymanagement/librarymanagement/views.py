# from django.http import HttpResponse
# from django.shortcuts import render
# import http.client
# import json
# def home(request):
#     return render(request, 'index.html')

# def search(request):
#     return render(request, 'search.html')

# def user(request):
#     return render(request, 'user.html')

# def registerform(request):
#     return render(request,'registerform.html')

# def about(request):
#     return HttpResponse("<h1>Welcome to Chai's Django Project: About page</h1>")

# def contact(request):
#     return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")

# # def fetch_books(request):
# #     conn = http.client.HTTPSConnection("goodreads12.p.rapidapi.com")
# #     headers = {
# #         'x-rapidapi-key': "328a469ce8msh3b5ae0cff237e4ep1dc00djsnaebca66ff65b",
# #         'x-rapidapi-host': "goodreads12.p.rapidapi.com"
# #     }
# #     conn.request("GET", "/getBookByID?bookID=42844155", headers=headers)
# #     res = conn.getresponse()
# #     data = res.read()
# #     book_data = json.loads(data.decode("utf-8"))

# #     return render(request, 'books.html', {'book': book_data})

# def fetch_books(request):
#     conn = http.client.HTTPSConnection("goodreads12.p.rapidapi.com")
#     headers = {
#         'x-rapidapi-key': "328a469ce8msh3b5ae0cff237e4ep1dc00djsnaebca66ff65b",
#         'x-rapidapi-host': "goodreads12.p.rapidapi.com"
#     }
#     conn.request("GET", "/getBookByID?bookID=42844155", headers=headers)
#     res = conn.getresponse()
#     data = res.read()
#     book_data = json.loads(data.decode("utf-8"))

#     # Extracting the necessary details
#     book_details = {
#         'imageUrl': book_data.get('imageUrl', ''),
#         'bookId': book_data.get('bookId', ''),
#         'workId': book_data.get('workId', ''),
#         'bookUrl': book_data.get('bookUrl', ''),
#         'title': book_data.get('title', ''),
#         'authors': [author['name'] for author in book_data.get('author', [])],
#         'rating': book_data.get('rating', ''),
#         'totalRatings': book_data.get('totalRatings', ''),
#         'publishedYear': book_data.get('publishedYear', ''),
#         'totalEditions': book_data.get('totalEditions', '')
#     }

#     return render(request, 'books.html', {'book': book_details})



from django.http import HttpResponse
from django.shortcuts import render
import http.client
import json
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def user(request):
    return render(request, 'user.html')

def registerform(request):
    return render(request, 'registerform.html')

def about(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")


def fetch_books(request):
    conn = http.client.HTTPSConnection("goodreads12.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "328a469ce8msh3b5ae0cff237e4ep1dc00djsnaebca66ff65b",
        'x-rapidapi-host': "goodreads12.p.rapidapi.com"
    }
    conn.request("GET", "/getBookByID?bookID=42844155", headers=headers)
    res = conn.getresponse()
    data = res.read()
    book_data = json.loads(data.decode("utf-8"))

    logger.debug("Fetched book data: %s", book_data)

    try:
        book_details = {
            'imageUrl': book_data.get('imageUrl', ''),
            'bookId': book_data.get('bookId', ''),
            'workId': book_data.get('workId', ''),
            'bookUrl': book_data.get('bookUrl', ''),
            'title': book_data.get('title', ''),
            'authors': [author['name'] for author in book_data.get('author', []) if isinstance(book_data.get('author', []), list)],
            'rating': book_data.get('rating', ''),
            'totalRatings': book_data.get('totalRatings', ''),
            'publishedYear': book_data.get('publishedYear', ''),
            'totalEditions': book_data.get('totalEditions', '')
        }
        print(book_details)
    except Exception as e:
        logger.error("Error parsing book data: %s", e)
        return HttpResponse("Error parsing book data", status=500)

    return render(request, 'books.html', {'book': book_details})




