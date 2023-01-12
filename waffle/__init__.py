from __future__ import unicode_literals

from decimal import Decimal
import random

from waffle.utils import get_setting, keyfmt, get_cache
# from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site


VERSION = (1, 0, 0)
__version__ = '.'.join(map(str, VERSION))


def flag_is_active(request, flag_name):
    from .models import Flag

    current_site = get_current_site(request)
    flag = Flag.get(name=flag_name, site=current_site)
    return flag.is_active(request)

def switch_is_active(request, switch_name):
    from .models import Switch

    current_site = get_current_site(request)
    switch = Switch.get(name=switch_name, site=current_site)
    return switch.is_active()

def sample_is_active(request, sample_name):
    from .models import Sample

    current_site = get_current_site(request)
    sample = Sample.get(name=sample_name, site=current_site)
    return sample.is_active()
