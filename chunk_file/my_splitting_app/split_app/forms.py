"""Sign-up & log-in forms."""
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class SignupForm(FlaskForm):
    """User Sign-up Form."""

    name = StringField("Name", validators=[DataRequired()])
    email = StringField(
        "Email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    confirm = PasswordField(
        "Confirm Your Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    # website = StringField(
    #     'Website',
    #     validators=[Optional()]
    # )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """User Log-in Form."""

    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Enter a valid email.")]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


class UpdateDetailsForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=5, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    new_password = PasswordField(
        "New Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    btn = SubmitField("Update Profile")


# class User(UserMixin, BaseModel):
#     username = CharField(unique=True, null=False)
#     email = CharField(unique=True, null=False)
#     password = CharField(unique=False, null=False)


# <div class="drag flex_c">
#                 <h3>Drag & Drop to Upload File; or</h3>
#                 <button>Browse</button>
#                 <input type="file" name="file" />
#                 <input type="number" name="amount" />
#                 <input type="submit" />
#               </div>
#               <small>Supports only CSV and JSON files only</small>
#             </div>
