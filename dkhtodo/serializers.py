from rest_framework_json_api import serializers
from dkhtodo.models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': False},
            'completed': {'required': False},
            'due_date': {'required': False},
        }

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    def validate(self, attrs):
        if 'due_date' in attrs:
            current_date = timezone.now().date()
            if attrs['due_date'] < current_date:
                raise serializers.ValidationError("Due date cannot be in the past.")
        return attrs

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task

    def update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance

    def list(self):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return serializer.data

    def retrieve(self, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise serializers.ValidationError("Task not found.")
        serializer = TaskSerializer(task)
        return serializer.data

    def partial_update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return instance
