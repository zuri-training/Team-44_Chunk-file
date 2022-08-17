"""Logged-in page routes."""
from ast import Try
import base64
from pathlib import Path
from tkinter import N
from unicodedata import name
from flask import (
    Blueprint,
    render_template,
    redirect,
    send_file,
    url_for,
    request,
    flash,
    Flask,
    send_from_directory,
)
from .zips import zipper
from .forms import UpdateDetailsForm
from flask_login import current_user, login_required, logout_user
from werkzeug.utils import secure_filename
from zipfile import ZipFile
import os
from .models import db, User
from . import splitter

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

ALLOWED_EXTENSIONS = {"csv", "json"}
ALLOWED_IMAGE_EXTENSIONS = {"gif", "jpg", "png", "jpeg"}


@main_bp.route("/")
@main_bp.route("/index")
def index():
    """Logged-in User Dashboard."""
    return render_template(
        "index.html",
        title="Index Page",
        template="dashboard-template",
        current_user=current_user,
    )


@main_bp.route("/contactUS")
def contactUs():
    """Logged-in User Dashboard."""
    return render_template(
        "contactUs.html",
        title="Contact-Us Page",
        template="dashboard-template",
        current_user=current_user,
    )


@main_bp.route("/documentation")
def documentation():
    """Logged-in User Dashboard."""
    return render_template(
        "documentation.html",
        title="Contact-Us Page",
        template="dashboard-template",
        current_user=current_user,
    )


@main_bp.route("/tools")
def tools():
    """Logged-in User Dashboard."""
    return render_template(
        "tools.html",
        title="Contact-Us Page",
        template="dashboard-template",
        current_user=current_user,
    )


@main_bp.route("/gettingStarted")
def gettingStarted():
    """Logged-in User Dashboard."""
    return render_template(
        "gettingStarted.html",
        title="Contact-Us Page",
        template="dashboard-template",
        current_user=current_user,
    )


@main_bp.route("/faq")
def faq():
    """Logged-in User Dashboard."""
    return render_template(
        "faq.html",
        title="FAQ Page",
        template="dashboard-template",
        current_user=current_user,
    )

@main_bp.route("/privacy")
def policy():
    """Logged-in User Dashboard."""
    return render_template(
        "policy.html",
        title="FAQ Page",
        template="dashboard-template",
        current_user=current_user,
    )    

@main_bp.route("/terms&conditions")
def terms():
    """Logged-in User Dashboard."""
    return render_template(
        "terms.html",
        title="FAQ Page",
        template="dashboard-template",
        current_user=current_user,
    )

@main_bp.route("/aboutUs")
def aboutUs():
    """Logged-in User Dashboard."""
    return render_template(
        "aboutUs.html",
        title="About-Us",
        template="dashboard-template",
        current_user=current_user,
    )


@main_bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        "newUserDashboard.html",
        title="User Dashboard",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )


@main_bp.route("/settings/<name>", methods=["GET"])
@login_required
def settings(name):
    """Logged-in User Dashboard."""

    # Return 404 if path doesn't exist

    # Show directory contents

    return render_template(
        "settings.html",
        title="Settings Dashboard",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )


@main_bp.route("/storage/<name>", methods=["GET"])
@login_required
def storage(name):
    """Logged-in User Dashboard."""
    BASE_DIR = Path.cwd()/"static"/"uploads"

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return os.abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    xfiles = []
    for file in files:
        newfile = file.split("_")
        if newfile[0] == name:
            xfiles.append(file)

    return render_template(
        "storage.html",
        title="User Dashboard",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
        files=xfiles,
    )


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_image_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS
    )


@main_bp.route("/settings/<name>", methods=["GET", "POST"])
@login_required
def upload_image_file(name):
    print(request.method, "ududu")
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(url_for("main_bp.dashboard"))
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(url_for("main_bp.dashboard"))
        if file and allowed_image_file(file.filename):
            filename = secure_filename(file.filename)
            filename = filename.split(".")
            file.save(
                os.path.join(
                    Path.cwd()/"static"/"uploads"/"pictures",
                    f"{name}.{filename[-1]}",
                )
            )
            return redirect(f"/settings")
    return "Wrong request method"


@main_bp.route("/uploader/<name>", methods=["GET", "POST"])
@login_required
def upload_file(name):
    print(request.method)
    if request.method == "POST":
        print("kk")
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(url_for("main_bp.dashboard"))
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(url_for("main_bp.dashboard"))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(
                os.path.join(
                    Path.cwd()/"static"/"uploads",
                    filename,
                )
            )
            try:
                limit = int(request.form["amount"])
            except:
                limit = 10000

            savename = filename.split(".")
            splitter.split(
                open(
                    os.path.join(
                        Path.cwd()/"static"/"uploads",
                        filename,
                    ),
                    "r",
                ),
                output_path= Path.cwd()/"static"/"uploads",
                output_name_template=f"{name}_{savename[0]}_",
                row_limit=limit,
                filename=filename,
            )

            nFilename = filename.split(".")
            delete_item(filename, name)
            zipper(nFilename[0], name)
            return redirect(f"/storage/{name}")
    return "Wrong request method"


@main_bp.route("/uploads/<name>")
def download_file(name):
    return send_from_directory(
        Path.cwd()/"static"/"uploads", name
    )


def render_picture(data):
    render_pic = base64.b64encode(data).decode("ascii")
    return render_pic


@main_bp.route("/upload/picture/<email>", methods=["GET", "POST"])
@login_required
def uploadPicture(email):
    if request.method == "POST":
        existing_user = User.query.filter_by(email=email).first()
        if "inputFile" not in request.files:
            flash("No file part", "error")
            redirect((f"/settings/{existing_user.name}"))
        file = request.files["inputFile"]
        if file.filename == "":
            flash("No selected file")
            redirect((f"/settings/{existing_user.name}"))
        data = file.read()
        render_file = render_picture(data)
        text = email
        existing_user.data = data
        existing_user.text = text
        existing_user.rendered_data = render_file
        db.session.commit()
        return redirect((f"/settings/{existing_user.name}"))


@main_bp.route("/updateprofile/<email>", methods=["GET", "POST"])
@login_required
def updateProfile(email):
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        newPassword = request.form["newPassword"]
        oldPassword = request.form["oldPassword"]
        confirmPassword = request.form["confirmPassword"]
        existing_user = User.query.filter_by(email=email).first()
        if name.rstrip != "":
            existing_user.name = name
        if email.rstrip != "":
            existing_user.email = email
        if newPassword != "" and existing_user.check_password(oldPassword):
            if newPassword == confirmPassword:
                existing_user.set_password(newPassword)
        db.session.commit()
        flash("Update Successful")
        return redirect((f"/settings/{existing_user.name}"))


@main_bp.route("/delete_item/<filename>/<name>", methods=["GET", "POST"])
@login_required
def delete_item(filename, name):
    try:

        file_path = os.path.join(
            Path.cwd()/"static"/"uploads",
            filename,
        )
        os.remove(file_path)

    except Exception as error:
        print(error("Error removing or closing downloaded file handle", error))

    return redirect(f"/storage/{name}")


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))


@main_bp.route("/profile", methods=["POST"])
@login_required
def edit_profile():
    # check whether both email and username has been taken, if not update the specific profile
    form = UpdateDetailsForm()

    if check_password_hash(current_user.password, form.data["password"]):
        if current_user.username != form.data["username"]:
            updated_user = User.update(username=form.data["username"]).where(
                User == current_user
            )
            updated_user.execute()
        if current_user.email != form.data["email"]:
            updated_user = User.update(email=form.data["email"]).where(
                User == current_user
            )
            updated_user.execute()
        if form.data["password"] != form.data["new_password"]:
            # updated_user = User.update(password=generate_password_hash(new_password)).where(User == current_user)
            updated_user = User.update(
                password=generate_password_hash(form.data["new_password"])
            ).where(User == current_user)
            updated_user.execute()
        flash("Profile successfully updated", "success")
        return redirect(url_for("users.view_profile"))
    else:
        flash("Kindly ensure that the initial password matches", "danger")
        return redirect(url_for("users.view_profile"))
    return redirect(url_for("users.view_profile"))
