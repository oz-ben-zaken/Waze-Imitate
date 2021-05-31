# wazelike

The project imitate path navigation. The user select origin, destenation and means of transportation, and the system generate all the available paths with randomize traffics delay. The system uses belman-ford algorithm to select the fastest path between the two points, then it present it to the user with the total time required for the journey.


## Installation

Requirements: Python 3.6.

install without pipenv:
```
$ pip3 install -r requirements.txt
python wazelike\\wazelike.py
```

install with pipenv:
```
pipenv install
pipenv run python wazelike\\wazelike.py

```


Run unit tests:

test without pipenv:
```
python test\\test_base.py
```

test with pipenv:
```
pipenv run python test\\test_base.py
```