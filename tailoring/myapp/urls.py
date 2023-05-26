from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    
   
    path('contact_us', views.contact_us, name='contact_us'),
    path('user_login', views.user_login_check, name='user_login'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_home/<slug>/', views.user_home, name='user_home'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_update', views.user_details_update, name='user_details_update'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),
    path('user_feedback', views.user_feedback, name='user_feedback'),
    path('user_add_cart/<id>/', views.user_add_cart, name='user_add_cart'),



    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_product_add', views.product_add, name='admin_product_add'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_userdetails_view', views.admin_user_details, name='admin_userdetails_view'),
    path('admin_product_details_view', views.admin_product_details_view, name='admin_product_details_view'),
    path('admin_purchase_view', views.admin_purchase_view, name='admin_purchase_view'),
    path('admin_product_update', views.admin_product_update, name='admin_product_update'),
    path('view_feedback', views.view_feedback, name='view_feedback'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    
    


   



]
