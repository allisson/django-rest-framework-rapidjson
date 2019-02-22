djangorestframework-rapidjson
=============================

Provides `rapidjson <https://github.com/python-rapidjson/python-rapidjson>`_
support with parser and renderer.

.. image:: https://travis-ci.org/allisson/django-rest-framework-rapidjson.svg?branch=master
    :target: https://travis-ci.org/allisson/django-rest-framework-rapidjson

.. image:: https://img.shields.io/pypi/v/djangorestframework-rapidjson.svg
        :target: https://pypi.python.org/pypi/djangorestframework-rapidjson
        :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/djangorestframework-rapidjson.svg
        :target: https://pypi.python.org/pypi/djangorestframework-rapidjson
        :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/djversions/djangorestframework-rapidjson.svg
        :target: https://pypi.python.org/pypi/djangorestframework-rapidjson
        :alt: Supported Django versions

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
