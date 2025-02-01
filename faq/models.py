from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    language_code = models.CharField(max_length=5, default="en")

    def translate_text(self, field_name, target_lang):
        translator = Translator()
        text = getattr(self, field_name)
        try:
            translation = translator.translate(text, dest=target_lang)
            return translation.text
        except Exception:
            # Fallback to original text if translation fails
            return text

    def get_translation(self, lang="en"):
        return {
            "question": self.translate_text("question", lang),
            "answer": self.translate_text("answer", lang),
        }

    def __str__(self):
        return self.question
