from flask import render_template,url_for,flash,request,redirect,Blueprint
from flask_login import current_user,login_required
from cumulus import db
from cumulus.models import Posting
from cumulus.postings.forms import PostingForm

postings = Blueprint('postings',__name__)

#############################
## CHECKLIST
#############################

# CREATE
# READ
# UPDATE
# DELETE

#
@postings.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form=PostingForm()

    if form.validate_on_submit():

        posting = Posting(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id
                             )
        db.session.add(posting)
        db.session.commit()
        flash('Posting Created')
        return redirect(url_for('core.index'))

    return render_template('create_posting.html',form=form)

#
@postings.route('/<int:posting_id>')
def posting(posting_id):
    posting=Posting.query.get_or_404(posting_id)
    return render_template('posting.html',title=posting.title,
                            date=posting.date,post=posting
    )

#
@postings.route("/<int:posting_id>/update",methods=['GET', 'POST'])
@login_required
def update(posting_id):
    posting = Posting.query.get_or_404(posting_id)

    if posting.author!=current_user:
        abort(403)
    form=PostingForm()

    if form.validate_on_submit():
        posting.title=form.title.data
        posting.text=form.text.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('postings.posting',posting_id=posting.id))

    elif request.method=='GET':
        form.title.data=posting.title
        form.text.data=posting.text
    return render_template('create_posting.html',title='Update',
                           form=form)

#
@postings.route("/<int:posting_id>/delete", methods=['POST'])
@login_required
def delete_post(posting_id):
    posting=Posting.query.get_or_404(posting_id)

    if posting.author!=current_user:
        abort(403)
    db.session.delete(posting)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('core.index'))