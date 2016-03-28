
Read, search and write Twitter data
===================================

How to build & run:
-------------------

* Create python virtual environment.
    ::

        $ virtualenv twenv

* Activate virtual environment
    ::

        $ source twenv/bin/activate

* Install application dependencies
    ::

        $ pip install -r requirements.txt

* Run application
    ::

        $ python run_app.py
* How to use
    ::

        $ what do you want to do? read/tweet/search: read
        $ ip screen_name: <screen_name>
        $ number of tweets required: <int>
        $ <response>
    ::

        $ what do you want to do? read/tweet/search: tweet
        $ Do you want to tweet from the file? Y/n <'Y'/'n'>
        $ if 'Y', ip file path <file_path>
        $ if 'n', tweet: <Tweet>
    ::

        $ what do you want to do? read/tweet/search: search
        $ search for: <word>
        $ number of tweets required: <int>
        $ <reqponse: [{screen_name: tweet}, ...]>
