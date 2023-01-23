from django.shortcuts import redirect, render


from .form import BookForm, UnreadBookForm
from .models import ReadBooks, UnreadBooks
from .search import get_book_info


def readbooks(request):
    books = ReadBooks.objects.all()
    l = []
    for i in books:
        d = {}
        d['book_id'] = i.book_id
        d['title'] = i.title
        d['subtitle'] = i.subtitle
        d['author'] = i.author
        d['genre'] = i.genre
        d['my_rating'] = i.my_rating
        d['date_fin'] = i.date_fin
        d['img'] = i.cover
        l.append(d)
    context = {'read_books': l}
    return render(request, 'base/read.html', context)

def read_book(request, book_id):
    book = ReadBooks.objects.get(book_id=book_id)
    book_info = get_book_info(book)
    context = {'books': book_info}
    return render(request, 'base/book.html', context)

def unreadbooks(request):
    books = UnreadBooks.objects.all()
    l = []
    for i in books:
        d = {}
        d['book_id'] = i.book_id
        d['title'] = i.title
        d['subtitle'] = i.subtitle
        d['author'] = i.author
        d['img'] = i.cover
        if not len(i.summary) <= 600:
            d['summary'] = i.summary[0:600] + '...'
        else:
            d['summary'] = i.summary
        l.append(d)
    context = {'unread_books': l}
    return render(request, 'base/unread.html', context)

def addBook(request):
    form = BookForm

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')

    context = {'form': form}
    return render(request, 'base/read_form.html', context)

def addUnreadBook(request):
    form = UnreadBookForm
    if request.method == 'POST':
        form = UnreadBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unread')

    context = {'form': form}
    return render(request, 'base/unread_form.html', context)

def editBook(request, book_id):
    book = ReadBooks.objects.get(book_id=book_id)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('read')
    context = {'form': form}
    return render(request, 'base/read_form.html', context)

def deleteBook(request, book_id):
    book = ReadBooks.objects.get(book_id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('read')
    return render(request, 'base/delete.html', {'obj':book}) 

def deleteUnreadBook(request, book_id):
    book = UnreadBooks.objects.get(book_id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('unread')
    return render(request, 'base/delete.html', {'obj':book}) 
