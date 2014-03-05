from rea.models.contracts import Contract, Clause, ClauseRuleAspect, ContractClause

from cqrs.mongo import mongodb, DRFDocumentCollection


class ContractDocumentCollection(DRFDocumentCollection):
    '''
    A denormalized collection of `Contract`
    '''
    name = 'contract'
    model = Contract
    serializer_class = 'rea_serializers.serializers.ContractSerializer'


class ClauseDocumentCollection(DRFDocumentCollection):
    '''
    A denormalized collection of `Clause`
    '''
    name = 'clause'
    model = Clause
    serializer_class = 'rea_serializers.serializers.ClauseSerializer'


class ClauseRuleDocumentCollection(DRFDocumentCollection):
    '''
    A denormalized collection of `ClauseRuleAspect`
    '''
    name = 'clause_rule'
    model = ClauseRuleAspect
    serializer_class = 'rea_serializers.serializers.ClauseRuleAspectSerializer'


class ContractClauseDocumentCollection(DRFDocumentCollection):
    '''
    A denormalized collection of `ContractClause`
    '''
    name = 'contract_clause'
    model = ContractClause
    serializer_class = 'rea_serializers.serializers.ContractClauseSerializer'


mongodb.register(ContractDocumentCollection())
mongodb.register(ClauseDocumentCollection())
mongodb.register(ClauseRuleDocumentCollection())
mongodb.register(ContractClauseDocumentCollection())
