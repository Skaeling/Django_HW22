from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Product, Contact
from .forms import ProductForm, ContactForm


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    extra_context = {'title': 'Главная'}
    paginate_by = 6


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    extra_context = {'title': 'Контакты'}
    template_name = 'catalog/contact.html'
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        context_data['contacts'] = Contact.objects.all()
        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    extra_context = {'title': 'Описание товара'}


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    context_object_name = 'product'
    extra_context = {'title': 'Добавить товар'}


# def user_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_product = form.save()
#             print(f'Добавлен новый продукт: {new_product.name} стоимостью {new_product.price}$')
#             return redirect('product', new_product.pk)
#     else:
#         form = ProductForm()
#     return render(request, 'catalog/add_product.html', {'title': "Добавить товар", "form": form})

