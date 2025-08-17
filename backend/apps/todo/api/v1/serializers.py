from rest_framework import serializers
from apps.todo.models import Todo  # Assuming Todo is the model for todo items

class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for Todo model.
    """
    class Meta:
        model = Todo
        fields = '__all__'  # Adjust fields as necessary
        read_only_fields = ['id', 'created_at', 'updated_at','user']  # Example of read-only fields