from django.urls import path
from .views import chat_view
from .views import home  # import the view


urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('', home),  # <-- root URL

]
