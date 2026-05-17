#!/usr/bin/env bash

#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies from the root directory
pip install -r requirements.txt

# 2. Change directory into your Django project folder where manage.py is located
# (Change 'parkease' to 'parking' if that is your folder name)
cd parkease

# 3. Run management commands now that we are in the correct folder
python manage.py collectstatic --noinput
python manage.py migrate