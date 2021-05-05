# social_network_project


# General information 
This is my project for resume. I am creating REST API for social network. 
  
To register new user: api/v1/users/signup/  
  
To login: api-auth/login/  
  
Other urls you can find in urls.py file inside the project  


# Setup

To run this project firstly clone it (in command line):  
  
> git clone https://github.com/aaaivanko/social_network_project.git  
  
Activate virtual environment.   
  
  
Activation for windows: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html  
  
than install requirements   
  
> pip install -r requirements.txt  
  
after that run migrations   
  
> python manage.py migrate  

and finally  

> python manage.py runserver
