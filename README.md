## Sponsorship application and management

This is a project that allows students to apply for sponsorships, which is received by staff who then approves or rejects the application based on some merit.
When a sponsorship is approved, the sponsor can then be able to see a list of approved applicants. The sponsor can then choose to sponsor the applicant.

#### Assumptions
- At the current state, we have a list of courses statically defined in the database plus the schools.

#### How to use
The application is built using Python programming language and the Django framework with database being Postgres.
At the current state the project is only tested with python version 3.6.
##### Requirements
 - Python >= 3.5
 - Django 3.0.7
 - Postgres version >= 9.4
 - Virtualenv

**Running the application**
- To run the application, first clone the project from github using the command, for this you would require git installed. To clone run
```bash
$ git clone https://github.com/silaskenneth/sponsorship.git
```
- Change directory to the cloned repository by.
```bash
$ cd sponsorship
```
- Create an isolated work environment using virtualenv.
```bash
$ python -m virtualenv env
```
- Activate the virtual environment
```bash
$ source env/bin/activate #For unix systems
```
```bash
$ .\env\bin\activate.bat # For windows systems.
```


- Copy the `.env.example` file into a `.env` file and edit the credentials to match your credentials.
Note: 
   - `EMAIL_HOST_USER`,your email address, is used for sending emails so it is required.
   - `EMAIL_HOST_PASSWORD` , the password for the email address is used to authenticate with the mailing server to 
   authenticate and allow sending emails.
   
   **Note**
   
   For [Google Mail](https://gmail.com), you are required to follow the procedure in the [link](https://myaccount.google.com/lesssecureapps) to enable less secure apps to send emails for now.
- Install application dependencies.
```bash
pip install -r requirements.txt
```
- Create the database for the application in Postgres.
- Run the migrations to create tables and other objects.
```bash
python manage.py migrate
```
- Run the application server
```bash
python manage.py runserver
```
- Navigate the address `127.0.0.1:3000` in your browser to view you application.

## Application current state
The application API is almost done, what is remaining is linking up things to work together.
### What is missing?
- In developing Software, one of the core things is writing automated tests to test your application for possible errors not just limited
to logic errors, the application is not tested at the current state.
   ##### Why?
   - Given the time and the size of the project, testing would have been a good idea, but the project had
   small requirements which could just be tested manually.
   - With time the project would have tests to verify the logic and make sure bugs are caught before they
   reach production.

- Another thing that is missing is that most of the package version are never locked especially,
the ones that are dependencies of the installed packages. Adding a Pipefile to make sure dependencies are locked would be the best idea.

#### What can be improved
- To make the application scale, switching to a more reliable architecture such as event driven architecture or event sourcing would ease the load on the database to make
sure the load is given to something else like a messaging system.
- First off, the application is not complete, so completing it would make a big impact.
- Writing the tests.
- Using docker or vagrant to make sure there is a replicable environment for running the application.
- Including a CI/CD pipeline to make sure contributing to the project doesn't become a nightmare for me.