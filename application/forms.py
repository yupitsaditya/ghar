from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField,RadioField
from wtforms.validators import DataRequired, Email, ValidationError, URL
from application.models import Property

from wtforms.fields.html5 import DateField
import re

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
    ],
    "resourceType":[
        ('Medicine','Medicine'),
        ('Food','Food')
    ]

}


class AddPropertyForm(FlaskForm):
    # dt = DateField('DatePicker', format='%Y-%m-%d')



    email               =   StringField("Email",validators=[DataRequired(),Email()])
    mapsLocation        =   StringField("Google Maps Location",validators=[DataRequired()])
    startDate           =   DateField("Start Date",validators=[DataRequired()])
    endDate             =   DateField("End Date",validators=[DataRequired()])
    foodPreference      =   RadioField("Food Preference",choices=choices["foodPreference"],validators=[DataRequired()])
    genderPreference    =   RadioField("Gender Preference",choices=choices["genderPreference"],validators=[DataRequired()])
    bedsAvailable       =   SelectField("Beds Available", choices=choices["bedsAvailable"],validators=[DataRequired()])
    roommateCount       =   SelectField("Number of Roommates", choices=choices["roomateCount"],validators=[DataRequired()])
    additionalFeatures  =   StringField("Additional Features",validators=[DataRequired()])
    pricePerBed         =   IntegerField("Price/Bed",validators=[DataRequired()])
    submit              =   SubmitField("Submit",validators=[DataRequired()])

    def validate_email(self,email):
        pEmail=Property.objects(email=email.data).first()
        if pEmail:
            raise ValidationError("Email is already in use. Pick another one")


    def validate_endDate(self, endDate):
        # print(self.startDate.data, endDate.data)
        if self.startDate.data is not None and endDate.data is not None and self.startDate.data >= endDate.data:
            raise ValidationError("End date cannot be before or same as start date")

    def validate_mapsLocation(self,mapsLocation):
        # mapsRegex = "/^https?\:\/\/(www\.|maps\.)?google\.[a-z]+\/maps\/?\?([^&]+&)*(ll=-?[0-9]{1,2}\.[0-9]+,-?[0-9]{1,2}\.[0-9]+|q=[^&]+)+($|&)/";
        # mapsRegex = re.compile(r'/^https?\:\/\/(www\.|maps\.)?google\.[a-z]+\/maps\/?\?([^&]+&)*(ll=-?[0-9]{1,2}\.[0-9]+,-?[0-9]{1,2}\.[0-9]+|q=[^&]+)+($|&)/') 
        # mapsRegex=re.compile(r'^(http(s?)://)?maps\.google(\.|/).*/maps/.*$')
        # mapsRegex1=re.compile(r'/google.com\/maps/')
        # if not mapsRegex1.match(str(mapsLocation)):
        #     raise ValidationError("Not a google maps location")
        check1="google.com/maps"
        check2="maps.google"
        if check1 not in str(mapsLocation) and check2 not in str(mapsLocation):
            raise ValidationError("Not a google maps location")

    def validate_pricePerBed(self,pricePerBed):
        if pricePerBed.data>20000 or pricePerBed.data<1:
            raise ValidationError("Enter valid amount")

class CovidResourcesForm(FlaskForm):
    email                       =   StringField("Email",validators=[DataRequired(),Email()])
    resourceType                =   SelectField("Selecte Resource Type", choices=choices["resourceType"],validators=[DataRequired()])
    dateAvailableFrom           =   DateField("Date Available From",validators=[DataRequired()])
    submit                      =   SubmitField("Submit",validators=[DataRequired()])


class CovidLoginForm(FlaskForm):
    email               =   StringField("Email",validators=[DataRequired(),Email()])
    name                =   StringField("Name",validators=[DataRequired()])
    age                 =   IntegerField("Age",validators=[DataRequired()])
    languageSpoken                 =   IntegerField("Language Spoken",validators=[DataRequired()])
    locationZipCode     =   IntegerField("Zip Code of your Work Location",validators=[DataRequired()])
    idNumber            =   IntegerField("ID Number",validators=[DataRequired()])
    submit              =   SubmitField("Submit",validators=[DataRequired()])

class AddHotelPropertyForm(FlaskForm):
    # dt = DateField('DatePicker', format='%Y-%m-%d')



    email               =   StringField("Email",validators=[DataRequired(),Email()])
    mapsLocation        =   StringField("Google Maps Location",validators=[DataRequired()])
    # startDate           =   DateField("Start Date",validators=[DataRequired()])
    # endDate             =   DateField("End Date",validators=[DataRequired()])
    # foodPreference      =   RadioField("Food Preference",choices=choices["foodPreference"],validators=[DataRequired()])
    # genderPreference    =   RadioField("Gender Preference",choices=choices["genderPreference"],validators=[DataRequired()])
    roomsAvailable       =   IntegerField("Rooms Available",validators=[DataRequired()])
    # roommateCount       =   SelectField("Number of Roommates", choices=choices["roomateCount"],validators=[DataRequired()])
    additionalFeatures  =   StringField("Additional Features",validators=[DataRequired()])
    pricePerRoom         =   IntegerField("Price/Bed",validators=[DataRequired()])
    submit              =   SubmitField("Submit",validators=[DataRequired()])