"""
Serializers for the Recipe API.
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serialzer for Recpies."""
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes',
                  'price', 'link', 'description')
        read_only_fields = ('id',)
