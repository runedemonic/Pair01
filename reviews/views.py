from django.shortcuts import render, redirect
from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/create.html", context)


def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)