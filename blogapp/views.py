from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Posting


# Create your views here.
def index(request):
    return render(request, 'index.html')

def send(request):
    posting = Posting()
    posting.title = request.GET['title']
    posting.body = request.GET['body']
    posting.pubData = timezone.datetime.now()
    posting.save()
    return redirect('question')

def question(request):
    posting = Posting.objects
    return render(request, 'question.html', {'modelList':posting})

def question_detail(request, posting_id):
    posting_detail = get_object_or_404(Posting, pk=posting_id)
    return render(request, 'question_detail.html', {'postingNumb':posting_detail})

def aboutMe(request):
    return render(request, 'aboutMe.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def heeburndeuk(request):
    return render(request, 'heeburndeuk.html')

def our_school(request):
    return render(request, 'our_school.html')

def news_crawling(request):
    return render(request, 'news_crawling.html')


