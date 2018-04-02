import uuid
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings

from django.urls import reverse
from yellowant import YellowAnt

from .models import YellowAntRedirectState, UserIntegration


def request_yellowant_oauth_code(request):
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


def yellowant_oauth_redirect(request):
    """Receive the oauth2 code from YA to generate a new user integration
    
    This method calls utilizes the YA Python SDK to create a new user integration on YA.
    This method only provides the code for creating a new user integration on YA. Beyond that, you might need to 
    authenticate the user on the actual application (whose APIs this application will be calling) and store a relation
    between these user auth details and the YA user integration.
    """
    # oauth2 code from YA, passed as GET params in the url
    code = request.GET.get("code")

    # the unique string to identify the user for which we will create an integration
    state = request.GET.get("state")

    # fetch user with the help of state
    yellowant_redirect_state = YellowAntRedirectState.objects.get(state=state)
    user = yellowant_redirect_state.user

    # initialize the YA SDK client with your application credentials
    ya_client = YellowAnt(app_key=settings.YA_CLIENT_ID, app_secret=settings.YA_CLIENT_SECRET, access_token=None,
        redirect_uri=settings.YA_REDIRECT_URL)


    # get the access token for a user integration from YA against the code
    access_token_dict = ya_client.get_access_token(code)
    print(access_token_dict)
    access_token = access_token_dict["access_token"]

    # reinitialize the YA SDK client with the user integration access token
    ya_client = YellowAnt(access_token=access_token)

    # get YA user details
    ya_user = ya_client.get_user_profile()

    # create a new user integration for your application
    user_integration = ya_client.create_user_integration()

    # save the YA user integration details in your database
    UserIntegration.objects.create(user=user, yellowant_user_id=ya_user["id"],
        yellowant_team_subdomain=ya_user["team"]["domain_name"],
        yellowant_integration_id=user_integration["user_application"],
        yellowant_integration_invoke_name=user_integration["user_invoke_name"],
        yellowant_integration_token=access_token)
    
    # A new YA user integration has been created and the details have been successfully saved in your application's 
    # database. However, we have only created an integration on YA. As a developer, you need to begin an authentication 
    # process for the actual application, whose API this application is connecting to. Once, the authentication process 
    # for the actual application is completed with the user, you need to create a db entry which relates the YA user
    # integration, we just created, with the actual application authentication details of the user. This application
    # will then be able to identify the actual application accounts corresponding to each YA user integration.

    # return HttpResponseRedirect("to the actual application authentication URL")

    return HttpResponseRedirect(reverse("home"))


def yellowant_api(request):
    pass
