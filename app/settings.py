# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2018 Ircam
# Copyright (c) 2016-2018 Guillaume Pellerin
# Copyright (c) 2016-2018 Emilie Zawadzki

# This file is part of mezzanine-organization.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from __future__ import absolute_import, unicode_literals

import os, sys
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
import ldap, logging
from django.core.urlresolvers import reverse_lazy
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

DEBUG = True if os.environ.get('DEBUG') == 'True' else False

import warnings
warnings.filterwarnings(
        'ignore', r"DateTimeField .* received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

SILENCED_SYSTEM_CHECKS = ['fields.W342',]

SECRET_KEY = "H7665jhuyUTGuhuUYT6è-ertyezçuàçi'09Iikrpokfàçir"

###################################
# MEZZANINE ORGANIZATION SETTINGS #
###################################
try:
    from organization.settings import *
except ImportError as e:
    if "organization.settings" not in str(e):
        raise e


########################
# MAIN DJANGO SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['www.starts.eu', 'vertigo.starts.eu', 'vertigo2017.ircam.fr',
	'findpartner.starts.eu', 'wearsustain.starts.eu', 'starts01.ircam.fr',
    'sanbbox.www.starts.eu', 'sandbox.vertigo.starts.eu', 'sandbox.vertigo.ircam.fr',
        'starts02.ircam.fr',]
if DEBUG:
    ALLOWED_HOSTS = ['*']
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = False

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

AUTHENTICATION_BACKENDS = (
    # "organization.core.backend.OrganizationLDAPBackend",
    "mezzanine.core.auth_backends.MezzanineBackend",
    "guardian.backends.ObjectPermissionBackend",
)


##########
# LOCALE #
##########

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# Supported languages
LANGUAGES = (
    ('en', _('English')),
    #('fr', _('French')),
)

#############
# DATABASES #
#############
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    },
}


################
# APPLICATIONS #
################

INSTALLED_APPS = [
    "vertigo_components",
    "vertigo_ircam_fr",
    "vertigo_starts_eu",
    "www_starts_eu",

    "modeltranslation",
    "dal",
    "dal_select2",
    "dal_queryset_sequence",
    #"django.contrib.admin.apps.SimpleAdminConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    'django_extensions',
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.twitter",
    "mezzanine.accounts",
    # "mezzanine.galleries",
    # "mezzanine.mobile",
    "cartridge.shop",
    'djangobower',
    "meta",
    "mezzanine_agenda",
    "organization.core",
    "organization.media",
    "organization.pages",
    "organization.network",
    "organization.magazine",
    "organization.projects",
    "organization.agenda",
    "organization.shop",
    "organization.job",
    #"sorl.thumbnail", # required for thumbnail support
    "django_instagram",
    'hijack',
    'compat',
    'guardian',
    'extra_views',
    #'postman'
    'rdf_io',
    'skosxl',
    'versatileimagefield',
    'captcha',
]

CUSTOM_MODULES = False

if CUSTOM_MODULES:
    INSTALLED_APPS += [
        "organization.custom",
    ]

BOWER_COMPONENTS_ROOT = '/srv/bower/'
BOWER_PATH = '/usr/local/bin/bower'
BOWER_INSTALLED_APPS = (
    'jquery#2.2.4',
    'font-awesome#4.4.0',
)

# Add Migration Module path see : https://github.com/stephenmcd/mezzanine/blob/master/docs/model-customization.rst#field-injection-caveats
MIGRATION_MODULES = {
    "blog": "mezzanine.migrations.blog",
    "forms": "mezzanine.migrations.forms",
    "galleries": "mezzanine.migrations.galleries",
    "pages": "mezzanine.migrations.pages",
    "conf": "mezzanine.migrations.conf",
    "shop": "mezzanine.migrations.shop",
    "generic": "mezzanine.migrations.generic",
}

TEMPLATES = [{
               'BACKEND': 'django.template.backends.django.DjangoTemplates',
               'OPTIONS': {'builtins': ['mezzanine.template.loader_tags'],
                           'context_processors': ('django.contrib.auth.context_processors.auth',
                                                  'django.contrib.messages.context_processors.messages',
                                                  'django.template.context_processors.debug',
                                                  'django.template.context_processors.i18n',
                                                  'django.template.context_processors.static',
                                                  'django.template.context_processors.media',
                                                  'django.template.context_processors.request',
                                                  'django.template.context_processors.tz',
                                                  'mezzanine.conf.context_processors.settings',
                                                  'mezzanine.pages.context_processors.page',
                                                  'organization.core.context_processors.organization_settings',
                                                  "ulysses.context_processors.ulysse_context_processor",
                                                  "ulysses.context_processors.playlist",
                                                  ),
                            'loaders': [
                                'mezzanine.template.loaders.host_themes.Loader',
                                'django.template.loaders.filesystem.Loader',
                                'django.template.loaders.app_directories.Loader',
                                ],
                        }
            }]

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES += ()

STATICFILES_FINDERS += ()

SEARCH_MODEL_CHOICES += ()

PAGES_MODELS += ()


#########################
# ADMIN MENU            #
#########################

GRAPPELLI_INSTALLED = True
# JQUERY_FILENAME = 'jquery-3.1.0.min.js'
JQUERY_UI_FILENAME = 'jquery-ui-1.9.2.min.js'
TINYMCE_SETUP_JS = "/js/tinymce_setup.js"

SEARCH_PARENTS_MODELS = ('organization-network.Person',)

PAGES_PUBLISHED_INCLUDE_LOGIN_REQUIRED = True

SEARCH_PER_PAGE = 10
MAX_PAGING_LINKS = 10
DAL_MAX_RESULTS = 100

EVENT_SLUG = 'agenda'
EVENT_GOOGLE_MAPS_DOMAIN = 'maps.google.fr'
EVENT_PER_PAGE = 50
EVENT_USE_FEATURED_IMAGE = True
EVENT_EXCLUDE_TAG_LIST = [ ]
PAST_EVENTS = True

BLOG_SLUG = ''
BLOG_POST_PER_PAGE = 200
ARTICLE_PER_PAGE = 10
MEDIA_PER_PAGE = 9
ARTICLE_KEYWORDS = ''

#SHOP_CURRENCY_LOCALE = ''
SHOP_USE_VARIATIONS = False
SHOP_USE_RATINGS = False

FORMS_UPLOAD_ROOT = '/srv/media'

PROJECT_DEMOS_DIR = '/srv/media/projects/demos/'
if not os.path.exists(PROJECT_DEMOS_DIR):
    os.makedirs(PROJECT_DEMOS_DIR)

FORMAT_MODULE_PATH = [
    'organization.formats',
]

CUSTOM_MODULES = False

if CUSTOM_MODULES:
    INSTALLED_APPS += [
        "organization.custom",
    ]

# authorize models which does not heritate from Displayable
SEARCH_MODEL_NO_DISPLAYABLE = ('organization-network.Person',)

##########
# THEMES #
##########

HOST_THEMES = [
    ('vertigo.ircam.fr', 'vertigo_ircam_fr'),
    ('vertigo2017.ircam.fr', 'vertigo_ircam_fr'),
    ('vertigo.starts.eu', 'vertigo_starts_eu'),
    ('www.starts.eu', 'www_starts_eu'),
    ('sandbox.vertigo.ircam.fr', 'vertigo_ircam_fr'),
    ('sandbox.vertigo.starts.eu', 'vertigo_starts_eu'),
    ('sandbox.www.starts.eu', 'www_starts_eu'),
    ('starts02.ircam.fr', 'www_starts_eu'),

]

EXTRA_THEMES_BUILD = [
        ('vertigo_components', 'npm run build')
]

##################
#### GUARDIAN ####
##################

ANONYMOUS_USER_NAME = None
LOGIN_REDIRECT_URL = reverse_lazy('organization-network-profile-edit')

############
# HAYSTACK #
############

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'ulysses.search_backend.CustomElasticEngine',
        'URL': 'http://search:9200/',
        'INDEX_NAME': 'ulysses_search',
        'INCLUDE_SPELLING': True,
        'EXCLUDED_INDEXES': [
        ]
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


###########
# CAPTCHA #
###########

CAPTCHA_FONT_SIZE = 30
CAPTCHA_LENGTH = 6

############
# ACCOUNTS #
############

ACCOUNTS_VERIFICATION_REQUIRED = True


##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from local_settings import *
except ImportError as e:
    if "local_settings" not in str(e):
        raise e


##################
# ULYSSES SETTINGS #
##################

try:
    from ulysses_settings import *
except ImportError as e:
    if "ulysses_settings" not in str(e):
        raise e

####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())


move = lambda n, k, i: n.insert(i, n.pop(n.index(k)))
try:
    move(INSTALLED_APPS, "ulysses.system", len(INSTALLED_APPS))
except ValueError:
    pass
