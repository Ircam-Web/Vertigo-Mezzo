# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2017 Ircam
# Copyright (c) 2016-2017 Guillaume Pellerin
# Copyright (c) 2016-2017 Emilie Zawadzki

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

from settings import *


ULYSSES_ALLOW_IMPORT_FROM_PERSONAL_SPACE = False

# UGLY NEED TO REWRITE IT BECAUSE OF PRECEDENCE OF REDEFINITION OF MEDIA_ROOT
# it is set before in base.py
# Absolute filesystem path to the directory that will hold composer personal spaces files.
PERSONAL_FILES_ROOT = os.path.join(MEDIA_ROOT, 'composers')

# Absolute filesystem path to the directory that will hold admin files.
ADMIN_FILES_ROOT = os.path.join(MEDIA_ROOT, 'admin')

# Absolute filesystem path to the directory that will hold candidates files.
CANDIDATE_FILES_ROOT = os.path.join(MEDIA_ROOT, 'candidates')

# Absolute filesystem path to the directory that will hold temporary files.
TEMPORARY_FILES_ROOT = os.path.join(MEDIA_ROOT, 'temp')

# Absolute filesystem path to the directory that will hold draft files.
DRAFT_FILES_ROOT = os.path.join(MEDIA_ROOT, 'draft')

FILE_UPLOAD_PERMISSIONS = 0o664
FILE_UPLOAD_TEMP_DIR = TEMPORARY_FILES_ROOT



MIDDLEWARE_CLASSES += (
    'ulysses.middleware.RequestMiddleware',
    # 'ulysses.middleware.UlyssesPlayerMiddleware',
)


INSTALLED_APPS += [
    'floppyforms',
    'tinymce',
    'registration',
    'adminsortable',
    'colorbox',
    'sorl.thumbnail',
    'rest_framework',
    'snowpenguin.django.recaptcha2',
    
    # Utilities
    'ulysses.system',
    'ulysses.super_admin',

    # Core Ulysses apps
    'ulysses.web',
    'ulysses.reference',
    'ulysses.partners',
    'ulysses.profiles',
    'ulysses.competitions',
    'ulysses.composers',
    'ulysses.jury',
    'ulysses.works',
    'ulysses.events',
    'ulysses.social',
    'ulysses.community',
]


#Email settings
CONTACT_EMAIL = "contact@ulysses-network.eu"

# HIJACK
HIJACK_DISPLAY_WARNING = False
HIJACK_ALLOW_GET_REQUESTS = False
HIJACK_REGISTER_ADMIN = False
SILENCED_SYSTEM_CHECKS = ["hijack_admin.E001"]

ALLOW_HIJACK = True if os.environ.get('ALLOW_HIJACK') == 'True' else False

if ALLOW_HIJACK :
    SILENCED_SYSTEM_CHECKS = []
    HIJACK_LOGIN_REDIRECT_URL = "/login"
    HIJACK_LOGOUT_REDIRECT_URL = "/"
    HIJACK_ALLOW_GET_REQUESTS =  True
    HIJACK_DISPLAY_WARNING = True
    HIJACK_REGISTER_ADMIN = True

# https://docs.djangoproject.com/fr/1.10/ref/templates/api/
if ALLOW_HIJACK :
    INTERNAL_IPS = ['172.17.0.1']


COMPETITION_ADMINS_GROUP = 'competition-admins'
JURY_MEMBERS_GROUP = 'jury-members'
ACTIVE_COMPETITION_KEY = "active_competition"

TINYMCE_JS_URL = "/static/js/tiny_mce/tiny_mce.js"
TINYMCE_JS_ROOT = "/srv/static/js/tiny_mce/tiny_mce.js"

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

THUMBNAIL_FORMAT = 'PNG'

CAPTCHA_LENGTH = 8
CAPTCHA_TEST_MODE = 'test' in sys.argv

ULYSSES_COMMUNITY_FTP = {
    'host': 'community.ulysses-network.eu',
    'user': 'vi_live_ulysses_florence',
    'password': 'e3kxtlTpvF'
}

BROKER_HOST = "broker"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/" 

CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = "mysql://ulysses@db/ulysses_db"

LOG_FILE = '/var/log/app/app.log'

ASYNCHRONOUS_APPLICATION_PROCESSING = False

THUMBNAIL_DEBUG = True

RECAPTCHA_PUBLIC_KEY = '6LfV4i4UAAAAABHBE1yrCtewH_FxD8lpK9Zu7FO2'
RECAPTCHA_PRIVATE_KEY = '6LfV4i4UAAAAAMG-DxXH5R2wS7sOhUiXuMgUpj-g'

ALLOW_IMPORT_FROM_PERSONAL_SPACE = False
