import flask
from application import db
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class Property(db.Document):
    email               =   db.StringField(max_length=50,validators=[DataRequired(),Email()])
    mapsLocation        =   db.StringField(validators=[DataRequired()])
    startDate           =   db.DateTimeField(max_length=50,validators=[DataRequired()])
    endDate             =   db.DateTimeField(max_length=50,validators=[DataRequired()])
    foodPreference      =   db.StringField(max_length=50,validators=[DataRequired()])
    genderPreference    =   db.StringField(max_length=50,validators=[DataRequired()])
    bedsAvailable       =   db.IntField(validators=[DataRequired()])
    roommateCount       =   db.IntField(validators=[DataRequired()])
    additionalFeatures  =   db.StringField(max_length=50,validators=[DataRequired()])
    pricePerBed         =   db.IntField(validators=[DataRequired()])


class HotelProperty(db.Document):
    email               =   db.StringField(max_length=50,validators=[DataRequired(),Email()])
    mapsLocation        =   db.StringField(validators=[DataRequired()])
    # startDate           =   db.DateTimeField(max_length=50,validators=[DataRequired()])
    # endDate             =   db.DateTimeField(max_length=50,validators=[DataRequired()])
    # foodPreference      =   db.StringField(max_length=50,validators=[DataRequired()])
    # genderPreference    =   db.StringField(max_length=50,validators=[DataRequired()])
    roomsAvailable       =   db.IntField(validators=[DataRequired()])
    # roommateCount       =   db.IntField(validators=[DataRequired()])
    additionalFeatures  =   db.StringField(max_length=50,validators=[DataRequired()])
    pricePerRoom         =   db.IntField(validators=[DataRequired()])

class covidResources(db.Document):
    email               =   db.StringField(max_length=50,validators=[DataRequired(),Email()])
    resourceType        =   db.StringField(validators=[DataRequired()])
    dateAvailableFrom   =   db.DateTimeField(max_length=50,validators=[DataRequired()])   

class covidLogin(db.Document):
    email               =   db.StringField(max_length=50,validators=[DataRequired(),Email()])
    name                =   db.StringField(max_length=50,validators=[DataRequired()])
    age                 =   db.IntField(validators=[DataRequired()])
    languageSpoken      =   db.IntField(validators=[DataRequired()])
    locationZipCode     =   db.IntField(validators=[DataRequired()])
    idNumber            =   db.IntField(validators=[DataRequired()])

