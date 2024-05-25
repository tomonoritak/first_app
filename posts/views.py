from django.shortcuts import render
from django.views import View
from posts.models import Post

class IndexView(View):
    def get(self,request,*args,**kwargs):
        posts =  Post.objects.all()  # 1番目のレコードをpostに代入
        return render(request, 'posts/index.html',{'posts':posts})