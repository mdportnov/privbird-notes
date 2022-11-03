from privbird.exceptions.handler import response_exception
from privbird.exceptions.shared.ResourceNotFoundException import ResourceNotFoundException
from privbird.exceptions.shared.UnexpectedException import UnexpectedException


def handler404(request, exception):
    return response_exception(ResourceNotFoundException())


def handler500(request):
    return response_exception(UnexpectedException())
