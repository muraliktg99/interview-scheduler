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

Once `pip` has finished downloading the dependencies make the migrations for setupping the db:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Once all migrations done:
```sh
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

Provided browsable API comes with Django rest_framework. Once you run localhost, you can schedule the interview by navigating to 'http://127.0.0.1:8000/schedule/'.
This endpoint accepts GET, POST, HEAD, OPTIONS. POST the scheduling data

```json
{
    "schedule": "http://127.0.0.1:8000/schedule/"
}
```
1. Give the name.
2. Type (interviewer/Candidate).
3. Date of avaialability.
4. Give avaialble from timing and avaialable to timing.
5. POST the data.

Eg:
```json
{
    "id": "65771881-f5b7-424e-a18d-6dc3fd3fea59",
    "name": "Krishnan",
    "type": "C",
    "available_on": "2022-06-25",
    "available_from": "10:00:00",
    "available_to": "14:00:00"
}
```
After adding the approprate data, navigate to 'http://127.0.0.1:8000/search/'

1. Give the candidate ID and Interviewer ID as POST request
2. If any slot are avaialble it will return list of slots
3. If curresponding ID's are not avaialble, will return json person not found

Eg: 

```json
{
    "candidate_id": "65771881-f5b7-424e-a18d-6dc3fd3fea59",
    "interviewer_id": "a0ac2e72-af7b-4a19-a77c-14537b7eb6c5"
}
```
Response
```json
[
    [
        "10:00 AM",
        "11:00 AM"
    ],
    [
        "11:00 AM",
        "12:00 PM"
    ]
]
```

## Thankyou
Interview scheduler is a simple API which help HR to get available slots
Thankyou for reading and supporting
