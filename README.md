<!-- OUR AWESOME LOGO -->
# Elapse
##### Elapse is an interactive time visualization webapp that allows busy people to rationalize their busy lives.

## Using Elapse
Check out our app at http://quiet-garden-39600.herokuapp.com

## Running Elapse locally
To run Elapse locally (if you really want to), first clone our git repository.

    $ git clone https://github.com/aehoppe/Elapse
    $ cd Elapse

You'll need to set up a virtual environment. The following will create one named `flask`

    $ sudo pip2 install virtualenv
    $ python2.7 -m virtualenv flask

Then spin up the virtual environment

    $ source flask/bin/activate

and install dependencies

    $ flask/bin/pip install -r requirements.txt

Then you're ready to go, start up a local web server

    $ ./run.py

and go to `localhost:5000` in your browser of choice.

### Dependencies
Elapse makes heavy use of the following:
- [Flask](http://flask.pocoo.org)
- [flask_wtf](https://flask-wtf.readthedocs.org/en/latest/)
- [werkzeug](http://werkzeug.pocoo.org)
- [Jinja2](http://jinja.pocoo.org/docs/dev/)
- [heroku](https://www.heroku.com)
- [icalendar](https://github.com/collective/icalendar)
- [vincent](https://github.com/wrobstory/vincent)

Elapse's other dependencies are listed in [requirements.txt](https://github.com/aehoppe/Elapse/blob/master/requirements.txt). To install all dependencies, run the following on the command line:

    $pip install -r requirements.txt

## Examples
Coming soon...

## Implementation
Elapse was developed using Python.  We used the [icalendar](https://github.com/collective/icalendar) package to parse iCal data, and [vincent](https://github.com/wrobstory/vincent) to implement our data visualizations.  More about our implementation to come...

## License
Eventually, Elapse will be licensed (probably with an MIT License).  It isn't yet.

## Contributors
Elapse was created by [Gaby Clarke](https://github.com/gabyclarke) and [Alexander Hoppe](https://github.com/aehoppe) for our Software Design course at [Olin College of Engineering](http://www.olin.edu).
