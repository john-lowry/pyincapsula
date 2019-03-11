# PyPI Incapsula Wraper

This is a python module for interacting with the [Incapsula](https://my.incapsula.com/api/docs/v1) API.

## Requirements

Python modules:

- requests

## Setup & Authentication

The module uses environment variables APP_ID and APP_KEY for authentication. Export those or set them for the process running the utility.

## Errors

If there is a non-Incapsula error (i.e. HTTP/404, missing required information, etc...) a JSON formated error will be returned by the function. This error will have a code to help identify what the error is, a discription of the error, and the raw traceback or error message from BaseException.

A listing of codes can be found in [Error_Definitions.md](/Error_Definitions.md)
