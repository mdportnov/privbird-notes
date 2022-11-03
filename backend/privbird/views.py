from privbird.exceptions.handler import common_handler, prepare_response
from privbird.exceptions.shared.ResourceNotFoundException import ResourceNotFoundException
from privbird.exceptions.shared.UnexpectedException import UnexpectedException


def handler404(request, exception):
    return prepare_response(ResourceNotFoundException(), common_handler)


def handler500(request):
    return prepare_response(UnexpectedException(), common_handler)
