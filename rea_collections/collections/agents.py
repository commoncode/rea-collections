from rea.models.agents import Agent

from cqrs.mongo import mongodb, DRFDocumentCollection


class AgentDocumentCollection(DRFDocumentCollection):
    '''
    A denormalized collection of `Agent`
    '''
    serializer_class = 'rea_serializers.serializers.AgentSerializer'
    model = Agent
    name = 'agent'


mongodb.register(AgentDocumentCollection())
