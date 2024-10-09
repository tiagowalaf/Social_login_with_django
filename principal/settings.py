from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-g*jhd=x-1_h29h()bf8ap!%dd4d-ge81$1(igv50eon9mt2-^_'
DEBUG = True
ALLOWED_HOSTS = []

# Acesse a documentação abaixo e instale o django allauth.
# https://docs.allauth.org/en/latest/installation/quickstart.html

INSTALLED_APPS = [
    'django.contrib.admin',

    # Os dois apps abaixo são obrigatórios.
    'django.contrib.auth',
    'django.contrib.messages',
    # -------------------------

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'users',

    # Os dois apps abaixo são obrigatórios.
    'allauth',
    'allauth.account',
    # -----------------

    # Adicione os dois campos abaixo para usar o google.
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Adicione o middleware de contas.
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'principal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',

                #  allauth necessita do contexto abaixo.
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    # Necessário para logar com usuário no django admin, independente do "allauth"
    'django.contrib.auth.backends.ModelBackend',

    # 'allauth' especifica os métodos de autenticação, como logar com email.
    'allauth.account.auth_backends.AuthenticationBackend',
]

# O dicionário (google) dá a opção de colocarmos os nossos dados que serão criados na 
# google cloud platform.
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # "APP": {
        #     "client_id": os.getenv("client_id"),
        #     "secret": os.getenv("secret"),
        #     "key": "",
        # },
        "SCOPE": [
            "profile",
            "email",
        ],
    }
}
# SCOPE permite que o email do usuário e seu perfil estejam disponíveis 
# em nossa base de dados caso precisarmos.

# Quando for logar com o google e der erro de URI, clique em detalhes e cole o link,
# na gogle cloud, informado abaixo a "URI DE REDIRECIONAMENTO".
# URIs de redirecionamento autorizados

# Documentação
# https://docs.allauth.org/en/latest/installation/index.html

# Detalhes login com google
# https://docs.allauth.org/en/latest/socialaccount/providers/google.html



# Aqui temos as configurações para não permitir os usuários de se cadastrarem,
# com usuário e email.
# ACCOUNT_AUTHENTICATION_METHOD = "email"  # Pode ser "username_email" ou "username"
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # Pode ser "none", "optional", ou "mandatory"
# ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"
# SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"


WSGI_APPLICATION = 'principal.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Faz com que seja ignorado o template padrão 'login' do allauth.
# Esta é a forma mais simples de aplicar.
SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = "/minha-url/"
LOGOUT_REDIRECT_URL = "/"
# https://docs.allauth.org/en/latest/account/configuration.html
# https://stackoverflow.com/questions/20984434/bypass-signup-form-using-allauth/70680165#70680165


