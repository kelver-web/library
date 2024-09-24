from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, Category

# Create your views here.

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')
        category = self.request.GET.get('category')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__name__icontains=author)
        if category:
            queryset = queryset.filter(category__name__icontains=category)

        return queryset


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'catalog/category.html'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context



def book(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        'book': book
    }

    return render(request, 'catalog/book.html', context)
