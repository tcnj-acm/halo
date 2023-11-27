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

Make sure you have `pipenv` installed. If not, run `pip install pipenv`

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


4. Create the `pipenv` environment

   ```shell
   pipenv install
   ```

   Once you install the pipenv environment, you can activate it by doing:
   
   ```shell
   pipenv shell
   ```

5. Set up your [environmental variables](https://github.com/tcnj-acm/aslan/blob/main-dev/.github/ENVIRONMENTAL_VARIABLES.md) 
6. `python manage.py makemigrations`
7. `python manage.py runserver`

## Setup Data

We've compiled some setup data that you can use. 

1. `cd setup/`
2. `sh run_create_db.sh`


## Usage

We built this project because we wanted all hackathons to have a powerful application that can tackle on the big things. 

If you are organizing a hackathon and want a smooth process to manage your hackers and team, to operate registration and check-in, and to impress your sponsors with an exclusive website "booth" -- this project is for you!

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
