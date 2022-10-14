from django import forms
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
            "movie_name": forms.TextInput(
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
        }
        labels = {
            "title": "글 제목",
            "movie_name": "영화 제목",
            "content": "줄거리",
            "grade": "평점",
        }
