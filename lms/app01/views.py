from django.shortcuts import render, redirect

# Create your views here.
from app01 import models


# 出版社列表
def publisher_list(request):
    publisher = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': publisher})


# 添加出版社
def add_publisher(request):
    if request.method == 'POST':
        new_publisher_name = request.POST.get('name')
        models.Publisher.objects.create(name=new_publisher_name)
        return redirect('/publisher_list/')
    return render(request, 'add_publisher.html')


# 删除出版社
def drop_publisher(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/publisher_list/')


# 编辑出版社
def edit_publisher(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Publisher.objects.get(id=edit_id)
        new_name = request.POST.get('name')
        edit_obj.name = new_name
        edit_obj.save()
        return redirect('/publisher_list/')

    edit_id = request.GET.get('id')
    edit_obj = models.Publisher.objects.get(id=edit_id)
    return render(request, 'edit_publisher.html', {'publisher': edit_obj})


# 书籍的列表
def book_list(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book_list': book})


# 添加本书籍
def add_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        publisher_id = request.POST.get('publisher_id')
        models.Book.objects.create(name=new_book_name, publisher_id=publisher_id)
        return redirect('/book_list/')

    res = models.Publisher.objects.all()
    return render(request, 'add_book.html', {'publisher_list': res})


# 删除本书籍
def drop_book(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Book.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/book_list/')


# 编辑本书籍
def edit_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        new_publisher_id = request.POST.get('publisher_id')
        edit_id = request.GET.get('id')
        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.name = new_book_name
        edit_obj.publisher_id = new_publisher_id
        edit_obj.save()
        return redirect('/book_list/')

    edit_id = request.GET.get('id')
    edit_obj = models.Book.objects.get(id=edit_id)
    all_publisher = models.Publisher.objects.all()
    return render(request, 'edit_book.html', {'book': edit_obj, 'publisher_list': all_publisher})


# 作者的列表
def author_list(request):
    author = models.Author.objects.all()
    return render(request, 'author_list.html', {'author_list': author})


# 添加个作者
def add_author(request):
    if request.method == 'POST':
        new_author_name = request.POST.get('name')
        models.Author.objects.create(name=new_author_name)
        return redirect('/author_list/')
    return render(request, 'add_author.html')


# 删除个作者
def drop_author(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Author.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/author_list/')


# 修改下作者
def edit_author(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = models.Author.objects.get(id=edit_id)
        new_author_name = request.POST.get('name')
        new_book_id = request.POST.getlist('book_id')
        edit_obj.name = new_author_name
        edit_obj.book.set(new_book_id)
        edit_obj.save()
        return redirect('/author_list/')

    edit_id = request.GET.get('id')
    edit_obj = models.Author.objects.get(id=edit_id)
    all_book = models.Book.objects.all()
    return render(request, 'edit_author.html', {
        'author': edit_obj,
        'book_list': all_book
    })

