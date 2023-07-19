# launcher.py

import os
import subprocess

script = os.getenv('SCRIPT_NAME')

if script == 'main_daily':
    subprocess.run(['python', '/app/main_daily.py'])
elif script == 'main_monthly':
    subprocess.run(['python', '/app/main_monthly.py'])
else:
    print('Invalid SCRIPT_NAME. Please set SCRIPT_NAME to either "main_daily" or "main_monthly".')

