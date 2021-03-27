from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from cv.db import get_db

from flask import Flask
from flask import render_template
from flask import make_response
import pdfkit

bp = Blueprint('cv', __name__)

@bp.route('/')
def generate_cv():
    html = render_template("cv.html")
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=CV_GEOFFROY_BLONDEL.pdf"
    return response
