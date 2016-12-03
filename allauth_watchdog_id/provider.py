from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class WatchdogAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('absolute_url')

    def to_str(self):
        dflt = super(WatchdogAccount, self).to_str()
        return self.account.extra_data.get('username', dflt)


class WatchdogProvider(OAuth2Provider):
    id = 'watchdog'
    name = 'Watchdog'
    account_class = WatchdogAccount

    def extract_uid(self, data):
        return data['username']

    def extract_common_fields(self, data):
        return dict(username=data.get('username'),
                    name=data.get('username'),
                    email=data.get('email'))


providers.registry.register(WatchdogProvider)
