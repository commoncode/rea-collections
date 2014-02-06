from rea.models.events import Event, DecrementLine, IncrementLine

from cqrs.mongo import mongodb, DRFDocumentCollection


class EventDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Event`
    """
    name = "event"
    model = Event
    serializer_class = "rea_serializers.events.EventSerializer"


class IncrementLineDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `IncrementLine`
    """
    name = "increment_line"
    model = IncrementLine
    serializer_class = "rea_serializers.events.IncrementLineSerializer"


class DecrementLineDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DecrementLine`
    """
    name = "decrement_line"
    model = DecrementLine
    serializer_class = "rea_serializers.events.DecrementLineSerializer"


mongodb.register(EventDocumentCollection())
mongodb.register(IncrementLineDocumentCollection())
mongodb.register(DecrementLineDocumentCollection())

