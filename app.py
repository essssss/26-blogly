"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)
app.app_context().push()
db.create_all()


@app.route("/")
def list_users():
    """show a list of users"""

    users = User.query.all()
    return render_template("list.html", users=users)


@app.route("/", methods=["POST"])
def create_new_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")


@app.route("/add-new-user")
def show_form():
    """show a form to add a new user"""

    return render_template("new-user-form.html")


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """show a user's details"""
    user = User.query.get_or_404(user_id)
    blogposts = Post.query.filter(Post.posted_by == user_id).all()
    if blogposts:
        posts = blogposts
    else:
        posts = []
    return render_template("user-details.html", user=user, posts=posts)


@app.route("/users/<int:user_id>", methods=["POST"])
def edit_user(user_id):
    """Edit a user's details"""
    user = User.query.get_or_404(user_id)

    if request.form["first_name"]:
        user.first_name = request.form["first_name"]
    if request.form["last_name"]:
        user.last_name = request.form["last_name"]
    if request.form["image_url"]:
        user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")


@app.route("/users/<int:user_id>/delete")
def show_delete_confirmation(user_id):
    """request confirmation to delete user"""
    user = User.query.get_or_404(user_id)

    return render_template("delete.html", user=user)


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/")


@app.route("/users/<int:user_id>/edit")
def show_edit_user_form(user_id):
    """Show a form to edit a user's details"""

    user = User.query.get_or_404(user_id)
    return render_template("edit-user.html", user=user)


@app.route("/users/<int:user_id>/new-post")
def show_new_post_form(user_id):
    """Show a form to create a new post"""

    user = User.query.get_or_404(user_id)
    return render_template("new-post.html", user=user)


@app.route("/users/<int:user_id>/new-post", methods=["POST"])
def create_new_post(user_id):
    """Create a new post and link to a user's page"""

    title = request.form["title"]
    content = request.form["content"]
    posted_by = user_id

    new_post = Post(title=title, content=content, posted_by=posted_by)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/posts/{new_post.id}")


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """Show post via post id"""

    post = Post.query.get_or_404(post_id)
    return render_template("post-details.html", post=post)


@app.route("/posts/<int:post_id>/edit")
def edit_post_form(post_id):
    """show form to edit post"""

    post = Post.query.get_or_404(post_id)
    return render_template("edit-post.html", post=post)


@app.route("/posts/<int:post_id>", methods=["POST"])
def edit_post_submit(post_id):
    """Submit an edited post"""

    post = Post.query.get_or_404(post_id)

    if request.form["title"]:
        post.title = request.form["title"]
    if request.form["content"]:
        post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()

    return redirect(f"/posts/{post.id}")


@app.route("/posts/<int:post_id>/delete")
def show_delete_post_confirmation(post_id):
    """request confirmation to delete post"""
    post = Post.query.get_or_404(post_id)

    return render_template("post-delete.html", post=post)


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{post.posted_by}")
