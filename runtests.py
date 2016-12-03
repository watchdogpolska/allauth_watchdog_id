import os
import sys


import django
from django.conf import settings
from django.test.utils import get_runner

test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
django.setup()
TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests(["tests"])
sys.exit(bool(failures))
