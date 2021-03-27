# CV
Simple flask app to generate my resume from a html template.

### Dependencies:
[pdfkit](https://github.com/JazzCore/python-pdfkit) needs to have **wkhtmltopdf** installed:
```bash
apt-get install wkhtmltopdf
```

### Populate template
First, populate **cv/templates/cv.html**

### Update style
Then, modify style by updating **cv/static/style.css**

### Generate PDF
Finally, run flask local server:
```bash
$ export FLASK_APP=
$ export FLASK_ENV=development
$ flask run
```
Then navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
