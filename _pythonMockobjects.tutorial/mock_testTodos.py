# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from services import get_todos


@patch('services.requests.get')
def test_getting_todos(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)


    
    
    
"""Run in terminal with:
        nosetests --verbosity=2 .
    
    ipython shell: 
        !nosetests --verbosity=2 .

More info-
https://realpython.com/testing-third-party-apis-with-mocks/
"""    
