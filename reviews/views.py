from django.shortcuts import render, redirect
from reviews.forms import ReviewForm
from reviews.models import Review
from django.db.models import Q
from urllib.parse import urlparse
from urllib.request import urlopen
import django
import re
import requests
from bs4 import BeautifulSoup


# Create your views here.
def get_movie_data(url):
    # url 요청
    request = urlopen(url)
    byte_data = request.read()
    # 디코딩
    text_data = byte_data.decode("utf-8")
    # html 파싱
    html = BeautifulSoup(text_data, 'html.parser')
    soup = html.find("div", class_="poster")
    # tag & 내용 수집
    title = html.select_one('div[class="mv_info"] > h3[class="h_movie"] > a').string
    summary = html.select_one('div[class="story_area"] > p').text
    img = soup.find('img')["src"]

    # dictionary로 저장
    context = {
        'title': title,
        'img': img[:-15],
    }

    return context


def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            post = review_form.save(commit=False)
            data = get_movie_data(post.movie_url)
            post.movie_name = data['title']
            post.img = data['img']

            review_form.save()
            return redirect("reviews:index")
        else:
            print(0)
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


def detail(request, _pk):
    data = Review.objects.get(pk=_pk)
    context = {
        "data": data,
    }
    return render(request, "reviews/detail.html", context)


def update(request, _pk):
    review = Review.objects.get(pk=_pk)

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/update.html", context)


def delete(request, _pk):
    Review.objects.get(pk=_pk).delete()

    return redirect("reviews:index")


def search(request):
    all_data = Review.objects.order_by("-pk")
    search = request.GET.get("search", "")
    if search:
        search_list = all_data.filter(
            Q(title__icontains=search) | Q(movie_name__icontains=search)
        )

        context = {
            "search_list": search_list,
        }
    else:
        context = {
            "search_list": all_data,
        }

    return render(request, "reviews/search.html", context)
