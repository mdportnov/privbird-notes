from typing import Any, Type

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer


def get_validated_data(serializer: Type[Serializer], data: Type) -> Any:
    """
    Get validated request data or throw validation exception
    """
    serializer = serializer(data=data)
    if not serializer.is_valid():
        raise ValidationError(serializer.errors)
    return serializer.validated_data
