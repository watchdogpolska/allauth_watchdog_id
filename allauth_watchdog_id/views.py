import requests

from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)

from .provider import WatchdogProvider


class WatchdogOAuth2Adapter(OAuth2Adapter):
    provider_id = WatchdogProvider.id
    access_token_url = 'http://id.siecobywatelska.pl/o/token/'
    authorize_url = 'http://id.siecobywatelska.pl/o/authorize/'
    profile_url = 'http://id.siecobywatelska.pl/api/users/me/'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer %s' % token.token}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(
            request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(WatchdogOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(WatchdogOAuth2Adapter)
