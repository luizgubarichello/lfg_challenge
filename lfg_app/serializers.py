from rest_framework import serializers
from .models import ProposalField, ProposalFieldValue, Proposal


class ProposalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalField
        fields = ('id', 'name', 'label', 'type', 'required')


class ProposalFieldValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalFieldValue
        fields = ('id', 'field', 'value')


class ProposalSerializer(serializers.ModelSerializer):
    fields = ProposalFieldValueSerializer(many=True)

    class Meta:
        model = Proposal
        fields = ('id', 'status', 'fields', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        proposal = Proposal.objects.create(**validated_data)
        fields = []
        for field_data in fields_data:
            field_obj = ProposalFieldValue.objects.create(proposal=proposal, **field_data)
            fields.append(field_obj)
        proposal.fields.set(fields)
        return proposal
