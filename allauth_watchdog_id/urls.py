from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import WatchdogProvider

urlpatterns = default_urlpatterns(WatchdogProvider)
