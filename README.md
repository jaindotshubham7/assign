# FamPay-Hiring-Assignment


##### How to setup and run locally 

  1. Clone the Repository and change directory
  2. Configure ENV values in docker-compose and create .env file (You can refer to .env-sample)
  3. Run Docker
    $ docker-compose build
    $ docker-compose run web python manage.py createsuperuser
    $ docker-compose up
  4. Add Key
    $ curl --location --request POST 'http://localhost:8000/api/keys/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "active": true,
            "key": "test"
        }'
  5. Update query and limit through django admin in Config section (http://localhost:8000/manage/)
  
Note: You can access all the APIs through browser as well. (http://localhost:8000/api/)
