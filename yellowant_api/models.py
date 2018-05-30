"""Models for saving YellowAnt user details and application user details"""
from django.db import models
from django.contrib.auth.models import User


class UserIntegration(models.Model):
    """User YellowAnt Integration model

    Holds the information which identifies your user with an integration on YA.

    Since a single YA user is allowed to have multiple integrations with your application on YA, you
    need to store a one-to-many relationship for a user to many YA user integrations.

    For example, if this is a mail application, users might want to connect their personal mail and
    work mail with YA. In this case, a single user will have two YA integrations, one which connects
    the personal mail, and the other which connects the work mail.

    Fields:
        user (User): Your application user
        yellowant_user_id (int): YA user id
        yellowant_team_subdomain (str): YA user's team subdomain # each user on YA belongs to a
        team, irrespective of the team size
        yellowant_integration_id (int): Unique YA user integration id
        yellowant_integration_invoke_name (str): YA integration invoke name # each integration of
            your application is controlled by the user with the help of your application's default
            invoke name. Since a YA user is allowed to have multiple integrations with your
            application, YA will suffix the default invoke name for users who want to integrate more
            than once with your application, so that they can control the different integrations
            with their respective invoke names.
        yellowant_integration_token (str): Unique token per integration # This token allows your
            application to perform actions on the YA platform for the YA user integration.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yellowant_user_id = models.IntegerField(null=False)
    yellowant_team_subdomain = models.CharField(max_length=256, null=False)
    yellowant_integration_id = models.IntegerField(unique=True, null=False)
    yellowant_integration_invoke_name = models.CharField(
        max_length=256, null=False)
    yellowant_integration_token = models.CharField(max_length=2048, null=False)


class YellowAntRedirectState(models.Model):
    """Model to store YA oauth requests with users

    Create a new entry between the user and the oauth state

    Fields:
        user (User): Your application user
        state (str): A unique ID which helps in matching an oauth2 code from YA to a user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=512, null=False)
