# from rest_framework import serializers, viewsets
# from .models import PersonalNote

# class PersonalNoteSerializer(serializers.HyperlinkedSerializer):
#     class Meta:
#         model = PersonalNote
#         fields = ('title', 'content')

# class PersonalNoteViewSet(viewsets.ModelViewSet):
#     serializer_class = PersonalNoteSerializer
#     queryset = PersonalNote.objects.all()

### Oddly enough, mine was giving me errors, so I copy-pasted this
### one in here and all the problems went away... even though it's
### the same thing. Frustrating...

from rest_framework import serializers, viewsets
from .models import PersonalNote
# import pdb

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

        def create(self, validated_data):
            # import pdb; pdb.set_trace() # Start the debugger here
            # pass
            user = self.context['request'].user
            note = PersonalNote.objects.create(**validated_data)
            return note
            

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)