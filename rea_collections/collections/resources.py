from rea.models.resources import Resource

from cqrs.mongo import mongodb, DRFDocumentCollection


class ResourceDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Resource`
    """
    serializer_class = "rea_serializers.serializers.resources.ResourceSerializer"
    model = Resource
    name = "resource"


mongodb.register(ResourceDocumentCollection())
