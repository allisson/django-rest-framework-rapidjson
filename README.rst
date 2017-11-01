djangorestframework-rapidjson
=============================

Provides rapidjson support with parser and renderer.

.. image:: https://travis-ci.org/allisson/django-rest-framework-rapidjson.svg?branch=master
    :target: https://travis-ci.org/allisson/django-rest-framework-rapidjson


How to install
--------------

.. code:: shell

    pip install djangorestframework-rapidjson


How to use
----------

Update django rest framework config

.. code:: python

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework_rapidjson.renderers.RapidJSONRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework_rapidjson.parsers.RapidJSONParser',
        )
    }
