from django.urls import path
from .views import ShortenerView, RecoveryUrlView

urlpatterns = [
    path('', ShortenerView.as_view(), name='get_shorted_url'),
    path('<shorted_url>', RecoveryUrlView.as_view())
]