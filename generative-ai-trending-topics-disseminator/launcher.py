# launcher.py

from flask import Flask, request
import os
import subprocess
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/run-script', methods=['POST'])
def run_script():
    # extract job name from headers
    job_name = request.headers.get('X-MyScript-Name', '')
    logging.info(f'Received request for job: {job_name}')


    if job_name.endswith('main_daily'):
        subprocess.run(['python', 'main_daily.py'])
    elif job_name.endswith('main_monthly'):
        subprocess.run(['python', 'main_monthly.py'])
    else:
        return 'Invalid job name. Job name must end with either "daily" or "monthly".', 400

    return 'Script ran successfully.', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
