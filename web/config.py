import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="prj3db.postgres.database.azure.com"  #TODO: Update value
    # POSTGRES_URL="localhost"  #TODO: Update value

    POSTGRES_USER="prj3admin@prj3db" #TODO: Update value
    # POSTGRES_USER="postgres" #TODO: Update value

    POSTGRES_PW="@1995N89y12345"   #TODO: Update value
    # POSTGRES_PW=""   #TODO: Update value

    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_NAMESPACE ='prj3servicebus.servicebus.windows.net'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://prj3servicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=HtNP8GaqCFAhu7HarIJyDow44AD4KhPRr+ASbPcztaE=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False