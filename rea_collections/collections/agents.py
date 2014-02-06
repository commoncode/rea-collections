from rea.models.agents import Agent

from cqrs.mongo import mongodb, DRFDocumentCollection


class AgentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Agent`
    """
    serializer_class = "rea_serializers.agents.AgentSerializer"
    model = Agent
    name = "agent"


mongodb.register(AgentDocumentCollection())
