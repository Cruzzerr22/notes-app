from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================
# SECURITY
# ==============================================
# Make sure you have SECRET_KEY set in Render Environment Variables!
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-fallback-key-for-testing")
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]

# ==============================================
# APPLICATIONS
# ==============================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "moon",
]

# ==============================================
# MIDDLEWARE
# ==============================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sand_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'moon' / 'templates' / 'moon'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sand_project.wsgi.application"

# ==============================================
# DATABASE
# ==============================================
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

# ==============================================
# PASSWORD VALIDATION
# ==============================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==============================================
# INTERNATIONALIZATION
# ==============================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ==============================================
# STATIC FILES
# ==============================================
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Use CompressedStaticFilesStorage instead of Manifest to prevent 500 errors on missing CSS files
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# ==============================================
# DEFAULT PK
# ==============================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==============================================
# AUTH REDIRECTS
# ==============================================
LOGIN_URL = 'login'