from rest_framework import viewsets
from rest_framework import mixins


class WithoutDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Вьюсет с отключенным методом destroy."""

    pass
