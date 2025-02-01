import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ


@pytest.mark.django_db
def test_faq_translation():
    FAQ.objects.create(question="Hello", answer="World", language_code="en")
    client = APIClient()
    url = reverse("faq-list") + "?lang=hi"
    response = client.get(url)
    assert response.status_code == 200
    # Check that translated keys exist in the response
    data = response.json()
    assert "question" in data[0]
    assert "answer" in data[0]
