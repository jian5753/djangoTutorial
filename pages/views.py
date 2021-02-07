from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')
# hello_view 是可以自己改的名字，其他只要照著打就可以了
def hello_view(request): 
    #'hello.html' 是自己指定要回傳的檔案，其他的也都照著打
    return render(request, 'hello.html') 