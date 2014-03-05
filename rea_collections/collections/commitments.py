from rea.models.commitments import (
    Commitment, IncrementCommitment, DecrementCommitment
)

from cqrs.mongo import mongodb, DRFDocumentCollection


class CommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `Commitment`
    """
    name = "commitment"
    model = Commitment
    serializer_class = "rea_serializers.serializers.CommitmentSerializer"


class IncrementCommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `IncrementCommitment`
    """
    name = "increment_commitment"
    model = IncrementCommitment
    serializer_class = (
        "rea_serializers.serializers.IncrementCommitmentSerializer")


class DecrementCommitmentDocumentCollection(DRFDocumentCollection):
    """
    A denormalized collection of `DecrementCommitment`
    """
    name = "decrement_commitment"
    model = DecrementCommitment
    serializer_class = (
        "rea_serializers.serializers.DecrementCommitmentSerializer")


mongodb.register(CommitmentDocumentCollection())
mongodb.register(IncrementCommitmentDocumentCollection())
mongodb.register(DecrementCommitmentDocumentCollection())
