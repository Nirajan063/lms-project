from django.urls import path
from accounts.views import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', ProfileView.as_view(), name='signup')
    

]