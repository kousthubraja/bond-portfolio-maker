from rest_framework import serializers
from bondportfolio.models import Bond

class BondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = ('isin', 'name', 'tenor', 'ytm')