from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post,Reply
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts',__name__)



@posts.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created !','success')
        return redirect(url_for('main.comments'))
    return render_template('post.html',title="new post",form=form, legend='New Post')

@posts.route("/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post1.html',title=post.title,post=post)

@posts.route("/post/<int:post_id>/update",methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form .validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated ', 'success')
        return redirect(url_for('posts.post',post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template("post.html",title="Update Post",form=form ,legend = 'Update Post')


@posts.route("/post/<int:post_id>/delete",methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted ', 'success')
    return redirect(url_for('main.comments'))

@posts.route('/rep<int:post_id>')
def rep(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('replies.html',post=post)

@posts.route('/reply/<int:post_id>', methods=['GET','POST'])
def reply(post_id):

    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        replies = request.form['replies']
        ruser = request.form['ruser']
        post1 = Reply(replies=replies,ruser=ruser)#,owner=post,author1=current_user#
        db.session.add(post1)
        db.session.commit()
        return redirect(url_for('main.comments',post_id=post.id,ruser=ruser))
    return render_template('replies.html', post=post)

