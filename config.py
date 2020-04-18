import os



# mongodb+srv://easylease:<password>@cluster0-yjeck.mongodb.net/test?retryWrites=true&w=majority
class Config(object):
    SECRET_KEY =os.environ.get('SECRET_KEY') or "secret_string"


    MONGODB_SETTINGS ={
        'db':'EASYLEASE',
        'host':"mongodb+srv://easylease:easyleasePassword@cluster0-yjeck.mongodb.net/test?retryWrites=true&w=majority"
        }