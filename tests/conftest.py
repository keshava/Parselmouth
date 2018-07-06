import pytest

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'installed')))

class Resources(object):
	def __init__(self, base_path):
		self.base_path = base_path
	
	def __getitem__(self, file_name):
		return os.path.join(self.base_path, "data", file_name)

@pytest.fixture(scope="module")
def resources(request):
	return Resources(request.fspath.dirname)

from resource_fixtures import *
