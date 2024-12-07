from django.shortcuts import render,redirect
from .models import Request
from .forms import RequestForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    completed_requests = Request.objects.filter(status='completed').order_by('-created_at')[:4]
    in_progress_count = Request.objects.filter(status='in_progress').count()
    return render(request, 'home.html', {'completed_requests':completed_requests, 'in_progress_count':in_progress_count})

@login_required
def change_status(request, request_id):
    request_item = Request.objects.get(id=request_id)

    if request_item.method == 'POST':
        if request_item.status == 'new':
            if 'completed' in request.POST and request.FILES.get('image'):
                request_item.status = 'completed'
                request_item.image = request.FILES.get('image')
