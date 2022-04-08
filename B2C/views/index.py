from django.shortcuts import render, redirect

def main(request):
    return render(request, 'B2C/index.html')