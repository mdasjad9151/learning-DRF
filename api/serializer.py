from rest_framework import serializers
from  .models import  Todo

class TodoSerializer(serializers.Serializer):
    title =  serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=500)
    createDate = serializers.DateField()
    updateDate  = serializers.DateField()

    def create(self,validated_data):
        return Todo.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title  = validated_data.get('title' , instance.title)
        instance.body  = validated_data.get('body' , instance.body)
        instance.createDate  = validated_data.get('createDate' , instance.createDate)
        instance.updateDate  = validated_data.get('updateDate' , instance.updateDate)
        instance.save()
        return instance