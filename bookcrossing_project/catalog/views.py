from django.http import Http404, HttpResponse
from django.shortcuts import render

from data import BOOKS, CATEGORIES

def index_view(request):
    context = {'books':BOOKS}
    return render(request, 'catalog/index.html', context)


def categories_view(request):
    context = {'categories':CATEGORIES}
    return render(request, 'catalog/categories.html', context)


books_ = {book['id']:book for book in BOOKS}
split_books_by_categories = set(category 
                        for book in books_.values() 
                        for category in book['category'])


def category_detail_view(request, category_slug):
        if category_slug in split_books_by_categories:
            context = {'category': category_slug,
                    'category_book_list': BOOKS}  # category_book_list[category_slug]
            return render(request, 'catalog/category.html', context)
        else:
            raise Http404(f'Страница с category: {category_slug} не существует...')


def book_detail_view(request, book_id):
    if book_id in books_:
        context ={'book': books_[book_id]}
        return render(request, 'catalog/book.html', context)
    else:
        raise Http404(f'Страница с book_id: {book_id} не существует...')