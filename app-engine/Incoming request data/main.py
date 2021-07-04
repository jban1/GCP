# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask, request


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/query_example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    # Enter the url after deploying the code
    # https://abiding-center-317412.ue.r.appspot.com/query_example?language=jdfvnvnh&framework=Flask&website=DigitalOcean

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)


@app.route('/form-example', methods=['GET', 'POST'])

# allow both GET and POST requests
def form_example():

    # Enter the url after deploying the code
    # https://abiding-center-317412.ue.r.appspot.com/form-example

    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Enter the Language of your Choice: <input type="text" name="language"></label></div>
               <div><label>Enter the Framework of your Choice: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''

@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    if 'language' in request_data:
        language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
