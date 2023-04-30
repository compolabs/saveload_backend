#!/usr/bin/env python
import os
import sys
# from django.contrib.sites.models import Site

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "charting_library_charts.settings")
	# Site.objects.create(pk=1, domain='127.0.0.1', name='localhost')

	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)