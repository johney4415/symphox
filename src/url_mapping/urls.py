from django.urls import path
from .views import ShortenerView, RecoveryUrlView

urlpatterns = [
    path('', ShortenerView.as_view()),
    path('<shorted_url>', RecoveryUrlView.as_view())
]