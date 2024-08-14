from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from customer.forms import CustomerUserForm
from customer.models import Customer


def index(request):
    return render(request, 'index.html')


def customer_search(request):
    query = request.GET.get('query', '')
    results = Customer.objects.filter(first_name__icontains=query)
    return render(request, 'customers.html', {'results': results, 'query': query})


def customer_list(request):
    customers = Customer.objects.all()
    search = request.GET.get('search', None)
    if search is not None:
        customers = Customer.objects.filter(full_name__icontains=search)
    context = {
        'customers': customers
    }
    return render(request, 'customers.html', context)


@login_required()
def customer_details(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    context = {
        'customer': customer
    }
    return render(request, 'customer-details.html', context)


@login_required()
def update_customer(request):
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            customer = form.save()
            customer.save()
            return render('customer-details.html', {'customer': customer})
    else:
        form = CustomerUserForm()
        return render('customer-details.html', {'form': form})


@login_required()
def customer_delete(self, request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if customer:
        customer.delete()
        return render('customers.html', self)


@login_required()
def edit_customer(request, product_id):
    customer = get_object_or_404(Customer, id=product_id)
    form = CustomerUserForm(instance=customer)
    if request.method == 'POST':
        form = CustomerUserForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_details', product_id)

    return render(request, 'edit-customer.html', {'form': form})
