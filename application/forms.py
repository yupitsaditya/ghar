from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, ValidationError, URL
from application.models import Property


class AddPropertyForm(FlaskForm):
    email               =   StringField("Email",validators=[DataRequired(),Email()])
    mapsLocation        =   StringField("Google Maps Location",validators=[URL()])
    startDate           =   DateField("Start Date")
    endDate             =   DateField("End Date")
    foodPreference      =   StringField("Food Preference",validators=[DataRequired()])
    genderPreference    =   StringField("Gender Preference",validators=[DataRequired()])
    bedsAvailable       =   IntegerField("Beds Available")
    roommateCount       =   IntegerField("Number of Roommates")
    additionalFeatures  =   StringField("Additional Features",validators=[DataRequired()])
    pricePerBed         =   IntegerField("Price/Bed")
    submit              =   SubmitField("Submit")

    def validate_email(self,email):
        pEmail=Property.objects(email=email.data).first()
        if pEmail:
            raise ValidationError("Email is already in use. Pick another one")
    def validate_startDate(self, startDate):
        if self.startDate.data is None:
            raise ValidationError("")

    def validate_endDate(self, endDate):
        if endDate.data is None:
            raise ValidationError("")

        if self.startDate.data >= endDate.data:
            raise ValidationError("End date cant be before or same as start date")
    # def url_validator(url):
    # try:
    #     result = urlparse(url)
    #     return all([result.scheme, result.netloc, result.path])
    # except:
    #     return False
    # def validate_bedsAvailable(self, bedsAvailable):
    #     if bedsAvailable.data is None:
    #         return ValidationError("Please enter a number")
    #     if not isinstance(bedsAvailable.data, int):
    #         raise ValidationError("Need a number")
    
