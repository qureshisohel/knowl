from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UploadedFile
# Create your views here.
def home(request):
    return render(request, 'home.html')
@login_required
def dashboard(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request,'dashboard.html',{'files':files})
@login_required
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        UploadedFile.objects.create(user=request.user,file=file)
    return redirect('dashboard')
@login_required
def search_profiles(request):
    query = request.GET.get('q', '')  # Default to an empty string if 'q' is not present
    users = User.objects.filter(username__icontains=query)
    return render(request, 'search_profiles.html', {'users': users})
@login_required
def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    files = UploadedFile.objects.filter(user=user)
    return render(request, 'view_profile.html', {'user': user, 'files': files})

@login_required
def share_file(request, file_id, recipient_username):
    file = get_object_or_404(UploadedFile, id=file_id, user=request.user)
    recipient = get_object_or_404(User, username=recipient_username)
    
    # Logic to share the file with the recipient
    # (e.g., create a new instance of SharedFile model)

    return redirect('dashboard')

