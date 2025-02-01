from django.db import models
from ckeditor.fields import (
    RichTextField,
)  # or RichTextUploadingField if you need file uploads
from googletrans import Translator


class FAQ(models.Model):
    # Primary fields in English
    question = models.TextField(verbose_name="Question (English)")
    answer = RichTextField(verbose_name="Answer (English)")
    language_code = models.CharField(max_length=5, default="en")

    # Additional language fields (e.g., Hindi and Bengali)
    question_hi = models.TextField(
        verbose_name="Question (Hindi)", blank=True, null=True
    )
    answer_hi = RichTextField(verbose_name="Answer (Hindi)", blank=True, null=True)
    question_bn = models.TextField(
        verbose_name="Question (Bengali)", blank=True, null=True
    )
    answer_bn = RichTextField(verbose_name="Answer (Bengali)", blank=True, null=True)
    question = models.TextField(verbose_name="Question (English)")
    answer = RichTextField(verbose_name="Answer (English)")
    language_code = models.CharField(max_length=5, default="en")
    
    question_hi = models.TextField(verbose_name="Question (Hindi)", blank=True, null=True)
    answer_hi = RichTextField(verbose_name="Answer (Hindi)", blank=True, null=True)
    question_bn = models.TextField(verbose_name="Question (Bengali)", blank=True, null=True)
    answer_bn = RichTextField(verbose_name="Answer (Bengali)", blank=True, null=True)

    def get_translation(self, field_name, language_code):
        """
        Get the translated version of a field for a specific language code
        """
        if language_code == 'en':
            return getattr(self, field_name)
        
        translated_field = f"{field_name}_{language_code}"
        translated_value = getattr(self, translated_field, None)
        
        # Return the translated value if it exists, otherwise fallback to English
        return translated_value if translated_value else getattr(self, field_name)

    def save(self, *args, **kwargs):
        translator = Translator()
        # Auto-translate to Hindi if not provided
        if not self.question_hi:
            try:
                translation = translator.translate(self.question, dest="hi")
                self.question_hi = translation.text
            except Exception:
                # Fallback: use original English text
                self.question_hi = self.question

        if not self.answer_hi:
            try:
                translation = translator.translate(self.answer, dest="hi")
                self.answer_hi = translation.text
            except Exception:
                self.answer_hi = self.answer

        # Auto-translate to Bengali if not provided
        if not self.question_bn:
            try:
                translation = translator.translate(self.question, dest="bn")
                self.question_bn = translation.text
            except Exception:
                self.question_bn = self.question

        if not self.answer_bn:
            try:
                translation = translator.translate(self.answer, dest="bn")
                self.answer_bn = translation.text
            except Exception:
                self.answer_bn = self.answer

        super().save(*args, **kwargs)

    def __str__(self):
        # Return a short representation of the FAQ (e.g., first 50 characters of the question)
        return self.question[:50] + "..."
