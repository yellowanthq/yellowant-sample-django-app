import os

DJANGO_ENV= os.environ.get("DJANGO_ENV", "heroku")


if DJANGO_ENV == "heroku":
    # fetch environment variables
    YA_DEVELOPER_TOKEN = os.environ.get("YA_DEVELOPER_TOKEN")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

    # set website
    website = "https://{}.herokuapp.com/".format(HEROKU_APP_NAME)


    os.system("yellowant auth --token {} --host https://www.yellowant.com ".format(YA_DEVELOPER_TOKEN))
    os.system('yellowant sync -q --api_url {}yellowantauthurl/yellowantauthurl/ --website {} --install_page_url {} --privacy_policy_url {}privacy --redirect_uris {}redirecturl/yellowantredirecturl/'.format(website,website,website,website,website))
    os.system("ls -al")
    