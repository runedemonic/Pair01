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
            # 리뷰 폼이 바로 저장 되지 않도록 commit = False 하고 post에 저장
            post = review_form.save(commit=False)
            # post에 저장된 movie_url을 가져와서 크롤링하여 data에 저장
            data = get_movie_data(post.movie_url)
            # post에 있는 movie_name과 img를 크롤링한 결과값으로 교체
            post.movie_name = data['title']
            post.img = data['img']
            # 리뷰폼 저장
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
            # 리뷰 폼이 바로 저장 되지 않도록 commit = False 하고 post에 저장
            post = review_form.save(commit=False)
            # post에 저장된 movie_url을 가져와서 크롤링하여 data에 저장
            data = get_movie_data(post.movie_url)
            # post에 있는 movie_name과 img를 크롤링한 결과값으로 교체
            post.movie_name = data['title']
            post.img = data['img']
            # 리뷰폼 저장
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
