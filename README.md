# PofP
Prince of Pauper website

## Description
This project is intended to create a simple site for Magic: The Gathering content centered on the pauper format.
Currently the site has a home page and a page for articles which also includes functionality for comments.
Their is user account registration and login supported by Django included, necessary for making comments.

## Requirements
1. Django - https://www.djangoproject.com/download/
2. Python 3 - https://www.python.org/downloads/

## Installation
1. Download all files to a folder on your PC.
2. I suggest creating a virtual environment to work on this. To do this:
   1. In windows command line run the command "python -m pip install pip"
   2. Then use the commands "pip install virtualenv" followed by "pip install virtualenvwrapper-win"
   3. You can now enter "mkvirtualenv [name of your virtual environment]" to create a virtual environment
     You can now use the command "workon [name of your virtual environment]" to begin working in the virtual environment.
3. In order for the site to run correctly you will need to make migrations for the 'blog' app which handles articles and comments.
  to do this:
   1. In command prompt use the command "cd [filepath for the directory you downloaded this project to]" to select the project directory.
      (make sure you are working in your virtual environment at this point)
   2. Run the following commands:
      1. python manage.py migrate
      2. python manage.py makemigrations blog
      3. python manage.py sqlmigrate blog 0001
      4. python manage.py migrate
4. You should make yourself a superuser account so you can enter the admin page, to do this in command prompt enter:
   "python manage.py createsuperuser" and follow the steps to create your account

## Usage
To run the site open command prompt and make sure the base directory you saved the files in is selected (this should be the directory containing manage.py).
You can now activate you virtual environment and enter the command "python manage.py runserver" to run the site. It should look like this:

![RunServer](https://user-images.githubusercontent.com/15369629/219766991-2a961fbf-a877-4b12-845e-bf5931999251.PNG)

The site should now be displayed if you navigate to http://127.0.0.1:8000/ in your browser of choice. 8000 is the default port, you can change this by
adding the port number you want to use to the end of the runserver command (i.e. python manage.py runserver 8080). You can stop running the server by entering ctrl + c into command prompt.

With the site running you should see this when you go to the site:

![Site Home](https://user-images.githubusercontent.com/15369629/219767815-de70a114-1839-42de-8b51-93a02c971e42.PNG)

You can navigate the site by selecting the links at the top, You may already be logged in, in which case you will see your username and a logout button at the top instead of the login and register buttons.

The site will be pretty empty at the start, if you want to add an article got to the admin page by navigating to http://127.0.0.1:8000/admin/ (if you changed the site to not run on the default port you will need to put whichever port you chose instead of 8000). If you are not logged in you will be prompted to here and you need to have a superuser account to access the page which you should have made during the install. Then it should take you to this page:

![Admin](https://user-images.githubusercontent.com/15369629/219769379-e8f5a949-2ed4-4225-bca5-e76618e2a5df.PNG)

Under the 'Blogs' section you can click to add a post which will bring you to this screen where you can create a post:

![Post](https://user-images.githubusercontent.com/15369629/219772139-c21397e8-180e-48f1-9209-04f069c84289.PNG)

After you fill in your post press Save and it will be added to your database and will be visible in the site under the "Articles" page which lists all posts added in chronological order:

![ArticleList](https://user-images.githubusercontent.com/15369629/219781428-c3244d36-2375-45d1-8536-2cc441a49ea6.PNG)

Once you select an article from the list it will take you to the full view for the post:

![Article View](https://user-images.githubusercontent.com/15369629/219781639-dac5417f-f9af-4ed2-a495-ad4f87ef5bdf.PNG)

This also includes comments at the bottom of the page, and if you are logged in there is the option to add your own comment:

![comments](https://user-images.githubusercontent.com/15369629/219781905-fae09296-75bc-4577-b27a-38d845f0602d.PNG)


## Running in a container
To run this projext in a container you will either need to install Docker Decktop (https://www.docker.com/) or creat an account on Docker and use Docker Playground (https://labs.play-with-docker.com/)

### To run with Docker Desktop
1. Using command line in the root directory for the project (where the Dockerfile is found) run 
   'docker build -t [Enter a tag for the image] ./'
2. Once this has finished you can now run
   'docker run -d -p 80:80 [the tag you chose]'
3. You should now be able to access the site by going to http://localhost in your browser
4. To stop the app from running enter
   'docker ps'
   to find the ID of the container running the image and then enter
   'docker stop [ID]'

### To run in docker playground
1. Follow step 1 from the Docker Desktop instructions to build the image.
2. In command line enter 'docker login' and enter your login details for docker hub.
3. On docker hub you will need to create a repository and then retag the local image to match your repository's name.
   to do this in command line run
   'docker tag [local tag for the image] [user]/[repo]'
   where user is your Docker hub username and repo is the repositories name.
4. Now upload the image by entering
   'docker push [user]/[repo]'
5. Now you can login to Docker playground with your Docker account and start a session and begin a new instance/
6. In the instance enter
   'docker run -d -p 8000:8000 [user]/[repo]'
   Once this finishes executing the port number, 8000, should appear next to the 'open port' button near the top of the screen
   If you click this it will take you to the app's web page.

## Credits
- Murray Bosworth
- https://www.hyperiondev.com/ for their course resources
