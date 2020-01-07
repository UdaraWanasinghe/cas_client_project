from django.contrib.auth.models import User


def callback_function(tree):
    print(tree)
    username = tree[0][0].text
    User.objects.update_or_create(username=username)
