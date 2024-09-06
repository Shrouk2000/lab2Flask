from app.models import Posts, db
from flask import render_template, request, redirect, url_for, Blueprint
from app.posts import posts_blueprint


@posts_blueprint.route("/", endpoint="list")
def posts_list():
    posts = Posts.query.all()
    return render_template("posts/list.html", posts=posts)




@posts_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def posts_create():
    
    if request.method == "POST":
        post = Posts(
            name=request.form["name"],
            description=request.form["description"],
            image=request.form["image"],
        )
        db.session.add(post)
        db.session.commit()
        return redirect(post.show_url)

    return render_template("posts/create.html")


@posts_blueprint.route("<int:id>/update", endpoint="update", methods=["GET", "POST"])
def posts_update(id):
    post = db.get_or_404(Posts, id)
    if request.method == "POST":
        
        postobj = post
        postobj.name = request.form["name"]
        postobj.description = request.form["description"]
        postobj.image = request.form["image"]
        db.session.add(postobj)
        db.session.commit()
        return redirect(url_for("posts.list"))

    return render_template("posts/update.html", post=post)


@posts_blueprint.route("<int:id>", endpoint="show")
def post_show(id):
    post= db.get_or_404(Posts, id)
    return render_template("posts/show.html", post=post)


@posts_blueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
def posts_delete(id):
    post = db.get_or_404(Posts, id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("posts.list"))



