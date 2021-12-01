from django.shortcuts import render

def takenBooks_list(request):
    return render(request,'takenBooks_list.html')