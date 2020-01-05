from django.contrib.auth.models import User


def callback_function(tree):
    username = tree[0][0].text
    print(tree)
