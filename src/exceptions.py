class RemoteServiceException(Exception):
    """
    Remote service exception
    """

    pass


class RemoteValidationException(Exception):
    """
    Remote validation exception
    """

    pass


def raise_remote_service_exception():
    """
    Raise remote service exception
    """
    raise RemoteServiceException("This is remote server exception")


def raise_remote_validation_exception():
    """
    Raise remote validation exception
    """
    raise RemoteValidationException("This is remote validation exception")
