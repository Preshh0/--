Python web page example
To create a sample Python web page, you’d need a Linux server running Apache. You would also need to install Apache and the necessary dependency with the command:

sudo apt-get install apache2 libapache2-mod-python -y

With everything installed, create a new configuration file with the command:

sudo nano /etc/apache2/sites-available/python.conf

In that file, paste the following:

LoadModule python_module /usr/lib/apache2/modules/mod_python.so

<Directory /var/www/html/python>

    AddHandler mod_python .py

    PythonHandler hello

    PythonDebug On

</Directory>

Save and close the file.

Enable the configuration with the command:

sudo a2ensite python

Enable the Python Apache module with the command:

sudo a2enmod python

Restart Apache with the command:

sudo systemctl restart apache2

Create a new directory with the command:

sudo mkdir /var/www/html/python

Create a new file in that directory with the command:

sudo nano /var/www/html/python/hello.py

Paste the following in that new file:

from mod_python import apache

def handler(req):

    req.content_type = ‘text/plain’

    req.write(“Hello, World!”)

    return apache.OK

The above code uses Python to print out the text “Hello, World!” in the browser. Save and close the file. Change the ownership of that file with the command:

sudo chown www-data:www-data /var/www/html/python/hello.py

Point a web browser to http://SERVER_IP/python/hello.py

You should now see Hello, World! printed out in your web browser. 

Congratulations, you’ve just created your first web page using Python.

 