from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer


class FAQViewSet(viewsets.ViewSet):

    def list(self, request):
        lang = request.GET.get("lang", "en")
        cache_key = f"faqs_{lang}"
        data = cache.get(cache_key)

        if not data:
            faqs = FAQ.objects.all()
            # Use the model's method to get translated content.
            data = [faq.get_translation(lang) for faq in faqs]
            cache.set(cache_key, data, timeout=300)  # Cache for 5 minutes

        return Response(data)
