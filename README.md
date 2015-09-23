#Project Atlas

##### Created by (alphabetical order): Brian Su, Can Koc, Cem Koc in HackMIT September 2015.

##Onboarding

####Postgresql Setup:

1. If you haven't already done so [Install Postgres.app](http://postgresapp.com)

2. Add to `~/.bash_profile`:
    `export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.4/bin`

3. Source the new `~/.bash_profile` so it takes effect in current session:
    `source ~/.bash_profile`

4. Open psql from Postgres.app
    a. `CREATE DATABASE newadmit_db;`
    b. `CREATE USER admin WITH PASSWORD 'pizza_rocks_516!';`

5. If it tells you `admin` already exists then you can assume its done

####Django Project:
1. `git clone https://github.com/briansudo/newadmit.git`
2. `git pull https://github.com/briansudo/newadmit.git`

3. `cd`

4. `virtualenv -p <path to python2> venv`

5. `source venv/bin/activate`

6. `pip install -r requirements.txt`
    (If `psycopg2` fails, `brew install postgres`, then run again.)

7. `python manage.py migrate`

8. `python manage.py runserver`

* If you haven't created a super user, `python manage.py createsuperuser`
