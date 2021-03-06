"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home.views import home
from register.views import register
from addbooks.views import addbooks
from django.conf import settings
from django.conf.urls.static import static
from Home.views import view_books
from orders.views import place_order
from Home import views
from orders.views import my_orders, order_page, order_cancel, order_recieved
from dev.views import dev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("", include("django.contrib.auth.urls")),
    path("register/", register),
    path("addbooks/", addbooks, name="addbooks"),
    path("books/<int:id>", view_books),
    path("contact_dev/", views.contact_dev, "contact_dev"),
    path("place_order/<int:book_id>", place_order),
    path("my_orders/", my_orders,name="orders"),
    path("order_page/<int:id>", order_page, name="order_page"),
    path("order_cancel/<int:id>", order_cancel, name="cancel"),
    path("order_recieved/<int:id>", order_recieved, name="received"),
    path("dev/", dev, name="dev_page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
