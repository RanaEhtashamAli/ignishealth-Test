# ignishealth-Assigment

* Take Pull from the repo.
* Install requirements listed in requirement.txt
* Run Project using following command:
  * python manage.py runserver
* Once the project is up run following command:
  * python manage.py mirate
* The above command will create database tables and will load the csv into respective table.
* Now on browser goto localhost:8000/api/data/
* Here you will see all the data without any filter but paginated.
* You can filter out the data by clicking on the Filter button.
* Following are the URLs for the use-cases:
  * http://localhost:8000/api/data/AggImpClkView/
  * http://localhost:8000/api/data/AggInstallView/
  * http://localhost:8000/api/data/AggRevenueView/
  * http://localhost:8000/api/data/AggCpiSpndView/
