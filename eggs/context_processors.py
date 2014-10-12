from django.utils.safestring import mark_safe
import platform
import django
from django.conf import settings
import oscar


def usage_statistics_string():
    """
    For Eggs development, it is helpful to know which versions of Django and
    Python are in use, and which can be safely deprecated or removed. If
    tracking is enabled, this function builds a query string with that
    information. It is used in dashboard/layout.html with an invisible
    tracker pixel.
    If tracking is disabled, the tracker pixel does not get requested and
    no information is collected.
    """
    if getattr(settings, 'EGGS_TRACKING', True):
        query_str = 'django={django_ver}&python={python_ver}&oscar={oscar_ver}'.format(
            django_ver=django.get_version(),
            python_ver=platform.python_version(),
            oscar_ver=oscar.get_version(),
        )
        return mark_safe(query_str)
    else:
        return None


def metadata(request):
    """
    Add some generally useful metadata to the template context
    """
    return {'eggs_display_version': getattr(settings, 'EGGS_DISPLAY_VERSION', False),
            'eggs_version': getattr(settings, 'EGGS_VERSION', 'N/A'),
            'eggs_call_home': usage_statistics_string(),
            'eggs_manycontacts_bar': getattr(settings, 'EGGS_MANYCONTACTS_BAR', False),
            }
