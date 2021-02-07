from flask import render_template, request, Blueprint
from flaskblog.models import Post,Reply

main = Blueprint('main',__name__)



@main.route('/')
def about():
    return render_template('about.html',title = 'about')

@main.route('/comments')
def comments():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=4)
    posts1 = Reply.query.all()
    return render_template('comments.html',posts=posts,page=page,posts1=posts1)


@main.route('/about')

@main.route('/javascript1')
def javascript1():
    return render_template('/javascript/j1.html',title = 'javascript')
@main.route('/javascript2')
def javascript2():
    return render_template('/javascript/j2.html',title = 'javascript')
@main.route('/javascript3')
def javascript3():
    return render_template('/javascript/j3.html',title = 'javascript')
@main.route('/javascript4')
def javascript4():
    return render_template('/javascript/j4.html',title = 'javascript')
@main.route('/javascript5')
def javascript5():
    return render_template('/javascript/j5.html',title = 'javascript')
@main.route('/javascript6')
def javascript6():
    return render_template('/javascript/j6.html',title = 'javascript')
@main.route('/javascript7')
def javascript7():
    return render_template('/javascript/j7.html',title = 'javascript')
@main.route('/javascript8')
def javascript8():
    return render_template('/javascript/j8.html',title = 'javascript')
@main.route('/javascript9')
def javascript9():
    return render_template('/javascript/j9.html',title = 'javascript')


@main.route('/python')
def python():
    return render_template('/python/p1.html',title = 'python')
@main.route('/python1')
def python1():
    return render_template('/python/p2.html',title = 'python1')
@main.route('/python2')
def python2():
    return render_template('/python/p3.html',title = 'python1')
@main.route('/python3')
def python3():
    return render_template('/python/p4.html',title = 'python1')
@main.route('/python4')
def python4():
    return render_template('/python/p5.html',title = 'python1')

@main.route('/pythona1')
def pythona1():
    return render_template('/python/pa1.html',title = 'pythona1')
@main.route('/pythona2')
def pythona2():
    return render_template('/python/pa2.html',title = 'pythona2')
@main.route('/pythona3')
def pythona3():
    return render_template('/python/pa3.html',title = 'pythona3')