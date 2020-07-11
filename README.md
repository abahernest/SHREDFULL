# SHREDFULL
Shredfull is a fitness consulting agency for University of Lagos. Its a central hub for gymnastic centers, personal trainers and purchase of gym equipment

If you're reading this, do pardon my clumsy use of folder and file names. I had not learn't Software engineering practices at that time. I promise to update this in due time

The Website contains 3 django apps
1. blog : This contains all the necessary python files and templates for the blog section of the website
2. homepage: Although this was totally unnecessary. I just wanted to be able to easily change the carousel images and notifications from the django admin site.I also included the remainder sections (about page and equpments store page) of the website here
3. trainer: This contains html templates and python files for the gym centers and trainers. I still don't know why i used 2 separate templates for this. I obviously violated DRY since both pages had same format and style.

The_Pit : contains the base files. (settings,wsgi,asgi,...)

Asides the above mentioned, every other information can be detected.


TIP: If you ever fork this repo and try cloning it, just ensure you comment out SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE in the settings file before running locally.
