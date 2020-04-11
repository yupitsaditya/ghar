from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from application.models import Property


class AddPropertyForm(FlaskForm):
    email               =   StringField("Email",validators=[DataRequired(),Email()])
    mapsLocation        =   StringField("Google Maps Location",validators=[DataRequired()])
    startDate           =   StringField("Start Date",validators=[DataRequired()])
    endDate             =   StringField("End Date",validators=[DataRequired()])
    foodPreference      =   StringField("Food Preference",validators=[DataRequired()])
    genderPreference    =   StringField("Gender Preference",validators=[DataRequired()])
    bedsAvailable       =   IntegerField("Beds Available",validators=[DataRequired()])
    roommateCount       =   IntegerField("Number of Roommates ",validators=[DataRequired()])
    additionalFeatures  =   StringField("Additional Features",validators=[DataRequired()])
    pricePerBed         =   IntegerField("Price/Bed",validators=[DataRequired()])
    submit              =   SubmitField("Submit")

    def validate_email(self,email):
        pEmail=Property.objects(email=email.data).first()
        if pEmail:
            raise ValidationError("Email is already in use. Pick another one")

