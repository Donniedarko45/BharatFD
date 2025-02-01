from django.urls import path
from .views import FAQViewSet

faq_list = FAQViewSet.as_view({"get": "list"})

urlpatterns = [
    path("faqs/", faq_list, name="faq-list"),
]
