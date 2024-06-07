"""
A manangement command to populate the `certificate_available_date` field of the CourseCertificateConfiguration model in
the Credentials IDA.

This management command is required when moving from using `visible_date` to the certificate available date (a field of
the CourseCertificateConfiguration model) for managing certificate visibility. It can also be run ad-hoc to fix up any
data inconsistencies that may occur in the Credentials data.
"""
from django.core.management.base import BaseCommand

from openedx.core.djangoapps.credentials.tasks.v1.tasks import backfill_date_for_all_course_runs


class Command(BaseCommand):
    """
    A management command responsible for syncing certificate availability dates to Credentials using data from the CMS.

    Example usage:
        $ ./manage.py lms
    """
    def handle(self, *args, **options):
        backfill_date_for_all_course_runs.delay()
