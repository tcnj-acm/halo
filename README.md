 <br/>

<p align="center">
  <a href="https://github.com/tcnj-acm/aslan">
    <img src="logo.png" alt="Logo" width="500">
  </a>

  <h3 align="center">HALO</h3>
  
  <h4 align="center">Hackathons with Awesome Logistics Organization</h4>

  <p align="center">
    A Hackathon Management System built on Django
    <br/>
    <br/>
    <a href="https://github.com/tcnj-acm/aslan">View Demo</a>
    .
    <a href="https://github.com/tcnj-acm/aslan/issues">Report Bug</a>
    .
    <a href="https://github.com/tcnj-acm/aslan/issues">Request Feature</a>
  </p>


</p>



## About The Project


HALO is a web application that gives alleviates hackathon operations. From handling registration to hacker and organizer management, HALO works as a resource management tool for all organizers. This is what it can do:

1. Seamless Registration and Check-in module from the platform
2. Check-in hackers via QR Code
3. Website Waiting List mode
4. Hacker team building functionality with invitation integration via email
5. Exclusive sponsor booth pages on your website
6. Quick Deployment to Heroku
7. Integrated Email Module with Sendgrid
8. Resume Drop storage with AWS S3



## Built With

|  dependencies |
| ------------ |
| django  |
| mysqlclient  |
| python-dotenv  |
| django-qr-code  |
| django-storages  |
| boto3  |
| gunicorn  |
| dj-database-url  |
| whitenoise  |
| psycopg2-binary  |
| django-heroku  |
| sendgrid  |

Python 3.9.10



## Getting Started

### Prerequisites

You need a Unix-based Machine. If you only have a Windows Machine please refer to the [WSL Guide.](https://github.com/tcnj-acm/halo/blob/main-dev/.github/WSL_SETUP.md)

You can also find the required packages you NEED to have to run the application locally.

### Deployment Reqs

Heroku with Postgres used. Used Postgres add-on with heroku. Be sure to add all your envs to your secret variables on linkedin

### Environmental Variables

The project uses multiple .env variables and unfortunately couldn't be compiled to one file. Please read the Environmental Variables [doc](https://github.com/tcnj-acm/aslan/blob/main-dev/.github/ENVIRONMENTAL_VARIABLES.md) to properly set this up. 

### Installation


1. Clone the repo

   ```shell
   git clone git@github.com:tcnj-acm/halo.git
   ```

   

   Note: If you don't have ssh keys setup to clone git repos, then replace the ssh link with `https://github.com/tcnj-acm/.git`

2. `cd` to repo

3. Create the `pipenv` environment

   ```shell
   pipenv install
   ```

   Once you install the pipenv environment, you can activate it by doing:
   
   ```shell
   pipenv shell
   ```

4. Set up your [environmental variables](https://github.com/tcnj-acm/aslan/blob/main-dev/.github/ENVIRONMENTAL_VARIABLES.md) 
5. `python manage.py migrate`
6. `cd setup/`
7. `sh run_create_db.sh`
8. `cd ..`
9. `python manage.py runserver`


## Usage

We built this project because we wanted all hackathons to have a powerful application that can tackle on the big things. 

If you are organizing a hackathon and want a smooth process to manage your hackers and team, to operate registration and check-in, and to impress your sponsors with an exclusive website "booth" -- this project is for you!

## Resources

Here are some resources we believe that will help you to navigate and understand the repo's codebase:
- Free Resources
  - [\[Article\] Frontend vs Backend](https://www.geeksforgeeks.org/frontend-vs-backend/)
  - [\[Article\] Web Application Framework – A Comprehensive Guide](https://www.sencha.com/blog/a-comprehensive-guide-to-web-application-frameworks/)
  - [\[Article\] model-view-controller (MVC)](https://www.techtarget.com/whatis/definition/model-view-controller-MVC)
  - [\[Article\] Django Project MVT Structure](https://www.geeksforgeeks.org/django-project-mvt-structure/)
  - [\[Article\] An easy guide to understanding databases](https://dev.to/efkumah/an-easy-guide-to-understanding-databases-2hcf)
  - [\[Article\] Understanding databases: A comprehensive guide to different types for beginners](https://datasciencedojo.com/blog/understanding-databases/)
  - [\[Blog\] SQL Tutorial](https://www.sqltutorial.org/)
  - [\[Video\] How To Make A Portfolio Website Using HTML CSS JS | Complete Responsive Website Design (Project to follow along to.)](https://www.youtube.com/watch?v=0YFrGy_mzjY)
  - [\[Video\] Django Project - Simple Blog App (Project to follow along to.)](https://www.youtube.com/watch?v=AF4ji8bb1M8)
  - [\[Blog\] Getting started with Django](https://www.djangoproject.com/start/)
  - [\[Tutorial Course\] Cloud Computing Tutorial for Beginners](https://www.simplilearn.com/tutorials/cloud-computing-tutorial)
  - [\[Tutorial Course\] AWS Tutorial: A Step-by-Step Tutorial for Beginners](https://www.simplilearn.com/tutorials/aws-tutorial)
  - [\[Blog\] Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)
- Paid Resources
  - [\[Course\] Meta Front-End Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-front-end-developer)
  - [\[Course\] Meta Back-End Developer Professional Certificate (I used this personally to learn Django)](https://www.coursera.org/professional-certificates/meta-back-end-developer)
  - [\[Course\] Python & Django REST API Bootcamp - Build A Python Web API](https://www.udemy.com/course/the-complete-python-django-rest-api-development-bootcamp/)
  - [\[Course\] Ultimate AWS Certified Cloud Practitioner CLF-C02](https://www.udemy.com/course/aws-certified-cloud-practitioner-new/)

## Contributing

Please read our [Contributing](https://github.com/tcnj-acm/aslan/blob/main/.github/CONTRIBUTING.md) guide and [Code Of Conduct](https://github.com/tcnj-acm/aslan/blob/main/.github/CODE_OF_CONDUCT.md).

## License

Distributed under the MIT License. See [LICENSE](https://github.com/tcnj-acm/aslan/blob/main/LICENSE.md) for more information.


## Contributors

We'd like to thank everyone who has contributed to the project:

[Abhi Vempati](https://github.com/abhivemp) - *Believes chocolate is the only superior ice cream flavor*

[Kevin Williams](https://github.com/kvnwill) - *Who the heck likes chocolate frosted flakes anyway??* 

[Sterly Deracy](https://github.com/sderacy) - *Maestro of finesse, hustler extraordinaire* 

[JM Tameta](https://github.com/JmTameta) - *unofficial bachelors in the arts*

[Simon Blamo](https://github.com/Simon-Blamo) - *I go by Sam sometimes*