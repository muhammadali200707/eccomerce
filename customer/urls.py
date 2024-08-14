from django.urls import path
from customer import views, auth

urlpatterns = [
    path('', views.index, name='index'),
    path('customer-list/', views.customer_list, name='customer_list'),
    path('customer-detail/<int:customer_id>/', views.customer_details, name='customer_details'),
    path('customer-delate/<int:customer_id>', views.customer_delete, name='customer_delate'),
    path('customer-edit/<int:customer_id>', views.edit_customer, name='edit_customer'),
    path('search/', views.customer_search, name='search'),
    path('login/', auth.LoginForm, name='login'),
    path('logout/', auth.logout, name='logout'),
    path('register/', auth.RegisterForm, name='register'),
]
