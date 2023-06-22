from django.shortcuts import render


# Create your views here.
def read_conference(request):
    return render(request, 'create_conference.html')


def create_conference(request):
    return render(request, 'read_conference.html')


def update_conference(request):
    return render(request, 'update_conference.html')


def delete_conference(request):
    return render(request, 'delete_conference.html')


from django.shortcuts import render

# Create your views here.
