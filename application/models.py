import flask
from application import db
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class Property(db.Document):
    email               =   db.StringField(max_length=50,validators=[DataRequired(),Email()])
    mapsLocation        =   db.StringField(validators=[DataRequired()])
    startDate           =   db.StringField(max_length=50,validators=[DataRequired()])
    endDate             =   db.StringField(max_length=50,validators=[DataRequired()])
    foodPreference      =   db.StringField(max_length=50,validators=[DataRequired()])
    genderPreference    =   db.StringField(max_length=50,validators=[DataRequired()])
    bedsAvailable       =   db.IntField(validators=[DataRequired()])
    roommateCount       =   db.IntField(validators=[DataRequired()])
    additionalFeatures  =   db.StringField(max_length=50,validators=[DataRequired()])
    pricePerBed         =   db.IntField(validators=[DataRequired()])


    