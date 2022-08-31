import pytest

from src.exceptions import (
    RemoteServiceException,
    raise_remote_service_exception,
    RemoteValidationException,
    raise_remote_validation_exception,
)


def test_remote_service_exception():
    with pytest.raises(RemoteServiceException):
        raise_remote_service_exception()


def test_remote_validation_exception():
    with pytest.raises(RemoteValidationException):
        raise_remote_validation_exception()
