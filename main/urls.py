from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    # path('contact-us/', views.contact_us, name='contact_us'),
    path('faq/', views.faq, name='faq'),
]