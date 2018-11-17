#! python3

# updatePackages.py - update all pip packages that are outdated

import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]    # List all of the pip packages

# Update all pip packages
call(f'pip install --upgrade {" ".join(packages)}', shell=True)