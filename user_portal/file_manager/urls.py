from django.urls import path
from .views import home, dashboard, upload_file, search_profiles, view_profile, share_file

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('dashboard/', dashboard, name='dashboard'),
    path('upload/', upload_file, name='upload_file'),
    path('search/', search_profiles, name='search_profiles'),
    path('profile/<str:username>/', view_profile, name='view_profile'),
    path('share/<int:file_id>/<str:recipient_username>/', share_file, name='share_file')

]
