from application import app, db
from flask import render_template, redirect, flash, url_for
from application.models import Property, covidResources, covidLogin
from application.forms import AddPropertyForm, CovidResourcesForm, CovidLoginForm
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True )

@app.route("/login")
def login():
    return render_template("login.html", login=True )
@app.route("/addCovidResources",methods=['GET','POST'])
def addCovidResources():
    form= CovidResourcesForm()
    if form.validate_on_submit():
        email                       =   form.email.data
        resourceType                =   form.resourceType.data
        dateAvailableFrom           =   form.dateAvailableFrom.data
        covidResources(email=email,resourceType=resourceType,dateAvailableFrom=dateAvailableFrom).save()
        flash("You have successfully added resource. Thank you for your support")
        return redirect(url_for("index"))
    return render_template("addCovidResources.html", form=form, addCovidResources=True)

@app.route("/addCovidLogin",methods=['GET','POST'])
def adddCovidLogin():
    form= CovidLoginForm()
    if form.validate_on_submit():
        email               =   form.email.data
        name                =   form.name.data
        age                 =   form.age.data
        locationZipCode     =   form.locationZipCode.data
        idNumber            =   form.idNumber.data
        covidLogin(email=email,name=name,age=age,locationZipCode=locationZipCode, idNumber=idNumber).save()
        flash("You have been successfully added to the database. We will find you help.")
        return redirect(url_for("index"))
    return render_template("addCovidLogin.html", form=form, addCovidLogin=True)

@app.route("/listProperty", methods=['GET'])
def listProperty():
    properties = Property.objects.all()
    return render_template("listProperty.html", properties=properties, listProperty=True)


@app.route("/listCovidResources", methods=['GET'])
def listCovidResources():
    covid_resources = covidResources.objects.all()
    print(covid_resources);
    return render_template("listCovidResources.html", covid_resources=covid_resources, listCovidResources=True)

@app.route("/addProperty",methods=['GET','POST'])
def addProperty():
    form= AddPropertyForm()
    if form.validate_on_submit():
        email               =   form.email.data
        mapsLocation        =   form.mapsLocation.data
        startDate           =   form.startDate.data
        endDate             =   form.endDate.data
        foodPreference      =   form.foodPreference.data
        genderPreference    =   form.genderPreference.data
        bedsAvailable       =   form.bedsAvailable.data
        roommateCount       =   form.roommateCount.data
        additionalFeatures  =   form.additionalFeatures.data
        pricePerBed         =   form.pricePerBed.data
        Property(email=email,mapsLocation=mapsLocation,startDate=startDate,
        endDate=endDate,foodPreference=foodPreference,
        genderPreference=genderPreference,bedsAvailable=int(bedsAvailable),
        roommateCount=int(roommateCount),additionalFeatures=additionalFeatures,
        pricePerBed=int(pricePerBed)).save()
        print("hello")
        flash("You have successfully added the property")
        return redirect(url_for("index"))
    return render_template("addProperty.html", form=form, addProperty=True)





@app.route("/addFakeLocation")
def addFakeLocation():
    Property(email="something@something.com",mapsLocation="myHouse",startDate="1/1/2001",endDate="2/2/2002",foodPreference="veg",
    genderPreference="male",bedsAvailable=2,roommateCount=2,additionalFeatures="laundary room",pricePerBed=600).save()
    return render_template("addFakeLocation.html")