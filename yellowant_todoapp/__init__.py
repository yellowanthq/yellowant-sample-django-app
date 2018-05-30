"""Initialize YellowAnt Sample Todo Application"""
import os

DJANGO_ENV = os.environ.get("DJANGO_ENV", "heroku")


if DJANGO_ENV == "heroku":
    # fetch environment variables
    YA_DEVELOPER_TOKEN = os.environ.get("YA_DEVELOPER_TOKEN")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

    # set website
    WEBSITE = "https://{}.herokuapp.com/".format(HEROKU_APP_NAME)

    os.system("yellowant auth --token {} --host https://www.yellowant.com "
              .format(YA_DEVELOPER_TOKEN))
    os.system('yellowant sync -q --api_url {}yellowant-api/ --website {} --install_page_url {} \
        --privacy_policy_url {}privacy --redirect_uris {}yellowant-oauth-redirect/'
              .format(WEBSITE, WEBSITE, WEBSITE, WEBSITE, WEBSITE))
    os.system("ls -al")
