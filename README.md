## Fun Movies Web App


## Objective of Project
- In this project bascially we have made a movie web application. In which admin can upload movies links and search them. There are login for both user and admin.
- The user can also search and preview the vedio links. The rating can also be given by a user.

## Setup Project

1. Clone the project using following command
```
git clone https://github.com/AMOIZ0866/moviewebapp.git
```

2. Make sure you have python 3 installed in your system


3. For mac: 
- Install & Update brew
- Install, Run & Connect Postgres Service
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
brew install postgresql
brew services start postgresql
postgres psql
```

3. For Ubuntu: 
- Update package installer
- Install, Run & Connect Postgres Service
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo apt install postgresql postgresql-contrib pgadmin4
sudo su - postgres
```


4. Setup postgresql database user using postgre shell, postgres is default user, you can create your own or update default user password using following
```
ALTER USER postgres PASSWORD 'newpassword';
CREATE DATABASE cache_db;
```

5. Update Database connection credentials in settings/dev.py


6. Create Virtual Environment
```
python -m venv {{virtual_env}}
```

7. Activate Environment
```
source {{virtual_env}}/bin/activate
```

8. Install Required Dependencies
```
pip install -r requirements.txt
```

9. Run following command to migrate django models to database
```
python manage.py makemigrations
python manage.py migrate
```

10. Run following command to create superuser
```
python manage.py createsuperuser
```

12. Run following command to run server
```
python manage.py runserver
```



## Git Branching Structure
- Default latest branch is **Staging**
- Dev is child branch for development
- Every task branch finally merged in Staging upon completion/review.

## Overview of Platforms
Login- It is same for user and admin
Admin- Admin can add other users
User- User can sign up through signup page

## How to deploy new changes
- Create a new branch from **staging** branch
- Update the codebase according to the change-set required
- Create a **Pull Request** with **staging** branch
- Review & Merge that PR
