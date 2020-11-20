from flask import Blueprint,render_template

error_pages = Blueprint('error_pages',__name__)

# Client-Side Errors
## Lack of Authentication Credentials
@error_pages.app_errorhandler(401)
def error_401(error):
    return render_template('error_pages/401.html'),401

## Lack of Access Permissions
@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'),403

## Page Missing
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'),404

# Server-Side Errors
## Generic - Couldn't Complete Request
@error_pages.app_errorhandler(500)
def error_500(error):
    return render_template('error_pages/500.html'),500

## Bad Gateway/Network Connectivity
@error_pages.app_errorhandler(502)
def error_502(error):
    return render_template('error_pages/502.html'),502

## Service Temporarily Unavailable
@error_pages.app_errorhandler(503)
def error_503(error):
    return render_template('error_pages/503.html'),503

## Gateway Timeout/No Response
@error_pages.app_errorhandler(504)
def error_504(error):
    return render_template('error_pages/504.html'),504
