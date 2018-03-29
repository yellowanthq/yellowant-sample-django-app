import uuid
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings

from .models import YellowAntRedirectState


def request_yellowant_oauth_code(request, response):
    """Initiate the creation of a new user integration on YA
    
    YA uses oauth2 as its authorization framework. This method requests for an oauth2 code from YA to start creating a 
    new user integration for this application on YA.
    """
    # get the user requesting to create a new YA integration 
    user = User.objects.get(id=request.user.id)

    # generate a unique ID to identify the user when YA returns an oauth2 code
    state = str(uuid.uuid4())

    # save the relation between user and state so that we can identify the user when YA returns the oauth2 code
    YellowAntRedirectState.objects.create(user=user, state=state)

    # Redirect the application user to the YA authentication page. Note that we are passing state, this app's client id,
    # oauth response type as code, and the url to return the oauth2 code at.
    return HttpResponseRedirect("{}?state={}&client_id={}&response_type=code&redirect_url={}".format(
        settings.YA_OAUTH_URL, state, settings.YA_CLIENT_ID, settings.YA_REDIRECT_URL))

def yellowant_oauth_redirect(request, response):
    pass

def yellowant_api(request, response):
    pass
