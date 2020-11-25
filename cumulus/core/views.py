from flask import render_template,request,Blueprint
from cumulus.models import Posting

core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    postings = Posting.query.order_by(Posting.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',postings=postings)

@core.route('/info')
def info():
    return render_template('info.html')