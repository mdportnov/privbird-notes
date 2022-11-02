from rest_framework import serializers

from .models import *


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'main',
            'fake',
            'email',
        )


class FakeNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeNote
        fields = (
            'content',
            'password',
        )


class OptionSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer(many = False)
    fake_note = FakeNoteSerializer(many = False)
    
    class Meta:
        model = Option
        fields = (
            'type',
            'auto_destruction',
            'password',
            'notification',
            'fake_note',
        )
    
    def create_notification(self, validated_data):
        notification_data = validated_data.pop('notification')
        notification_serializer = NotificationSerializer(data = notification_data)
        notification_serializer.is_valid(raise_exception = True)
        return notification_serializer.save()
    
    def create_fake_note(self, validated_data):
        fake_note_data = validated_data.pop('fake_note')
        fake_note_serializer = FakeNoteSerializer(data = fake_note_data)
        fake_note_serializer.is_valid(raise_exception = True)
        return fake_note_serializer.save()
    
    def create(self, validated_data):
        validated_data['notification'] = self.create_notification(validated_data)
        validated_data['fake_note'] = self.create_fake_note(validated_data)
        return super(OptionSerializer, self).create(validated_data)


class NoteSerializer(serializers.ModelSerializer):
    option = OptionSerializer(many = False)
    
    class Meta:
        model = Note
        fields = (
            'content',
            'option',
        )
    
    def create(self, validated_data):
        option_data = validated_data.pop('option')
        option_serializer = OptionSerializer(data = option_data)
        option_serializer.is_valid(raise_exception = True)
        validated_data['option'] = option_serializer.save()
        return super(NoteSerializer, self).create(validated_data).prepare_content()


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = (
            'problem',
            'email',
        )