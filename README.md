# Interview scheduer API

API which provide the service for candidate/interviewer for scheduling their interviews and HR can see the time slots

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/muraliktg99/interview-scheduler.git
$ cd interview-scheduler
```
Create a virtual environment to install dependencies in and activate it:

```sh
$ py -m venv env
$ env\Scripts\activate
```
For further information regarding virtaul env, refer to the [docs](https://docs.python.org/3/library/venv.html).

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.