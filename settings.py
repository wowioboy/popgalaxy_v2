# Django settings for popgalaxy project.
import os.path
import socket
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True

hostname = socket.gethostname()

AWS_S3URL = 'http://media.popgalaxy.com/'

#from S3 import CallingFormat
#if hostname == 'popgalaxy.com':
    #DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
#AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
#AWS_ACCESS_KEY_ID = 'AKIAJ5RENZ2C35363IHQ'
#AWS_SECRET_ACCESS_KEY = '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'
#AWS_STORAGE_BUCKET_NAME = 'media.popgalaxy.com'

GRAVATAR_DEFAULT_IMG = "http://popgalaxy.com/media/images/popgalaxy_default_avatar.png"
GRAVATAR_SIZE = 80


TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'table,spellchecker,paste,searchreplace,preview,fullscreen',
    'theme_advanced_buttons4': 'preview,spellchecker,fullscreen',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'theme': 'advanced',
    'extended_valid_elements': 'script[type|src],iframe[src|style|width|height|scrolling|marginwidth|marginheight|frameborder]'
}
TINYMCE_SPELLCHECKER = True


ADMINS = (
    #('Lawrence Leach', 'lleach@wowio.com'),
)

MANAGERS = ADMINS



if hostname == 'popgalaxy.com':
    DATABASE_HOST = '173.203.196.9'
    DATABASE_ENGINE = 'django.db.backends.mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_NAME = 'popgalaxy_production'             # Or path to database file if using sqlite3.
    DATABASE_USER = 'popgalaxy'             # Not used with sqlite3.
    DATABASE_PASSWORD = '@llstar$'         # Not used with sqlite3.
    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

#elif hostname == 'Moonbase-Three.local':
#    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#    DATABASE_ENGINE = 'django.db.backends.sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#    DATABASE_NAME = 'dev.db'       # Or path to database file if using sqlite3.
#    DATABASE_USER = ''             # Not used with sqlite3.
#    DATABASE_PASSWORD = ''         # Not used with sqlite3.
#    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
#    DEBUG = True

else:
    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_ENGINE = 'django.db.backends.mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_NAME = 'popgalaxy_development'             # Or path to database file if using sqlite3.
    DATABASE_USER = 'popgalaxy'             # Not used with sqlite3.
    DATABASE_PASSWORD = '@llstar$'         # Not used with sqlite3.
    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
    DEBUG = True

TEMPLATE_DEBUG = DEBUG


# Set MEDIA_ROOT Location    
if hostname == 'Zeus.local':
    MEDIA_ROOT = '/Users/zeus/Desktop/Dropbox/Sites/django/popgalaxy_new/media/'
elif hostname == 'Lawrence-Leachs-Mac-Pro.local':
    MEDIA_ROOT = '/Users/lawrenceleach/Dropbox/Sites/django/popgalaxy_new/media/'
else:
    MEDIA_ROOT = '/home/popgalaxy/public_html/popgalaxy/media/'


# Caching Setup
CACHE_BACKEND = 'db://pg_cache_table'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(%7bylm*s56^^9=fs(c37tuv*m5rx%rm9%v+%-ou@s#49c9&88'

# Twitter 
CONSUMER_KEY = 'z8o36ZRk6KBJTsrPRiLA'
CONSUMER_SECRET = 'LXksObjMcwz9HlF0fCAgEwlnK2rn15hIGs2bh5hmTIA'
ACCESS_TOKEN ='207726284-uFI8u4nTqBOW4wCsP9Ns3w64JGZwjosab2pdZ3P4'
ACCESS_SECRET = 'w7xe5xUqkV6qhlgmyUffrO0jaOKyxnj30BS9bwOWRQ'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

if hostname == 'popgalaxy.com':
    ROOT_URLCONF = 'urls'
else:
    ROOT_URLCONF = 'popgalaxy_new.urls'
	
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

TAGGING_AUTOCOMPLETE_JS_BASE_URL = '/media/js'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.markup',
    'tinymce',
    'pagination',
    'registration',
    'tagging',
    'tagging_autocomplete',
    'threadedcomments'
)

if hostname == 'popgalaxy.com':
    INSTALLED_APPS += (
        'south',
        'blog',
        'video',
        'headlines',
        'search',
        'corp',
        'shows',
        'profiles',
        'assetlocker',
        #'comments',
        #'search',
    )
else:
    INSTALLED_APPS += (
        'popgalaxy_new.blog',
        'popgalaxy_new.video',
        'popgalaxy_new.headlines',
        'popgalaxy_new.search',
        'popgalaxy_new.corp',
        'popgalaxy_new.shows',
        'popgalaxy_new.profiles',
        'popgalaxy_new.assetlocker',
        #'popgalaxy_new.comments',
        #'popgalaxy_new.search',
    )

