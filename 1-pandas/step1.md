# Install Libraries

We are going to use ``virtualenv`` and ``pip`` to install our libraries.

First we need to install virtualenv. Run the following:

`apt install python3.8-venv`{{execute}}

Create and activate the virtual environment:

`python3 -m venv env`{{execute}}
`source env/bin/activate`{{execute}}

Finally install the libraries:

`pip install pandas scikit-learn`{{execute}}
