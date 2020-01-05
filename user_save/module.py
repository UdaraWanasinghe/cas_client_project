from django.contrib.auth.models import User


def callback_function(tree):
    username = tree[0][0].text
    email = tree[0][1].text
    User.objects.get_or_create(username=username, email=email)
