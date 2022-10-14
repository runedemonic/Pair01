from django import forms
from django.forms import HiddenInput

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "movie_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "content": forms.Textarea(attrs={"class": "from-control", "rows": 10}),
            "grade": forms.Select(
                attrs={
                    "class": "from-control",
                }
            ),
            "movie_name": HiddenInput(),
            "img":HiddenInput(),
        }
        labels = {
            "title": "글 제목",
            "movie_url": "영화 링크",
            "content": "줄거리",
            "grade": "평점",
        }
