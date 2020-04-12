from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField,RadioField
from wtforms.validators import DataRequired, Email, ValidationError, URL
from application.models import Property

# (value, string shown in the dropdown)
choices = {
    "foodPreference" :[
        ('VEGAN','VEGAN'),
        ('VEG','VEG'),
        ('NON VEG','NON VEG'),
        ('ANY','ANY'),
    ],
    "genderPreference":[
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('BOTH','BOTH'),
    ],
    "bedsAvailable" : [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ],
    "roomateCount":[
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]

}


class AddPropertyForm(FlaskForm):
    email               =   StringField("Email",validators=[DataRequired(),Email()])
    mapsLocation        =   StringField("Google Maps Location",validators=[URL()])
    startDate           =   DateField("Start Date")
    endDate             =   DateField("End Date")
    foodPreference      =   RadioField("Food Preference",choices=choices["foodPreference"])
    genderPreference    =   RadioField("Gender Preference",choices=choices["genderPreference"])
    bedsAvailable       =   SelectField("Beds Available", choices=choices["bedsAvailable"])
    roommateCount       =   SelectField("Number of Roommates", choices=choices["roomateCount"])
    additionalFeatures  =   StringField("Additional Features",validators=[DataRequired()])
    pricePerBed         =   IntegerField("Price/Bed")
    submit              =   SubmitField("Submit")

    def validate_email(self,email):
        pEmail=Property.objects(email=email.data).first()
        if pEmail:
            raise ValidationError("Email is already in use. Pick another one")


    def validate_endDate(self, endDate):
        print(self.startDate.data, endDate.data)
        if self.startDate.data is not None and endDate.data is not None:
            if self.startDate.data >= endDate.data:
                raise ValidationError("End date cant be before or same as start date")

    
