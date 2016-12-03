=====
Usage
=====

To use allauth-watchdog_id in a application set ``settings.py`` to ::

    # For Django 1.7, use:
    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        # Required by `allauth` template tags
        'django.core.context_processors.request',
        ...
    )

    # If you are running Django 1.8+, specify the context processors
    # as follows:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    # Already defined Django-related contexts here

                    # `allauth` needs this from django
                    'django.template.context_processors.request',
                ],
            },
        },
    ]

    AUTHENTICATION_BACKENDS = (
        ...
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',
        ...
    )

    INSTALLED_APPS = (
        ...
        # The Django sites framework is required
        'django.contrib.sites',

        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth_watchdog_id'
        ...
    )

    SITE_ID = 1
