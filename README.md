django-mysite-sample
====================

This is the Django's tutorial mysite sample project with a couple of test cases and an installed app [django-sample-app](https://github.com/danirus/django-sample-app). Both are part of the example of Continuous Integration with Buildbot: [buildbot-sample-conf](https://github.com/danirus/buildbot-sample-conf).

    python manage.py syncdb --noinput
    python manage.py test polls --settings mysite.test_settings --verbosity=2 # only polls app
    python manage.py test --settings mysite.test_settings --verbosity=2       # test django too
    python manage.py runserver # (user: admin, passwd: admin)
