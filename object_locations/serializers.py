from models import Block

from rest_framework import serializers

# Serializers

class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block
        fields = ('device_id','block_id', 'signature', 'x', 'y','color',
                  'width', 'height', 'status', 'timestamp')