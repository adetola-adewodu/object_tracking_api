from rest_framework import viewsets

from django.utils.timezone import now
from object_locations.models import Block
from object_locations.serializers import BlockSerializer


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db import connection
import socket


# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def block_list(request):
    """
    List all blocks, or create a new block.
    """
    if request.method == 'GET':
        blocks = Block.objects.all()
        serializer = BlockSerializer(blocks, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':

        try:
            data = JSONParser().parse(request)
            block_id = data['block_id']
            signature = data['signature']

            # get block_id and signature
            insert_query = "update object_locations_block " \
                            "SET status = 'old' where block_id ={0}" \
                            "".format(block_id, signature)

            cursor = connection.cursor()
            cursor.execute(insert_query)

            serializer = BlockSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
        except socket.error as msg:
            print "Socket Error: %s" % msg

        return JSONResponse(serializer.errors, status=400)

def latest_block_list(request):
    latest_blocks = Block.objects.filter(status="latest")
    serializer = BlockSerializer(latest_blocks, many=True)
    return JSONResponse(serializer.data)

def get_latest_block(request):
    block_id = request.GET.get('block_id')

    latest_block = Block.objects.filter(block_id=block_id).get(status="latest")
    serializer = BlockSerializer(latest_block)
    return JSONResponse(serializer.data)


def delete_block(request):


    # Send an empty Response
    return HttpResponse()


@csrf_exempt
def delete_all_blocks(request):

    block_id = request.GET.get('block_id')
    signature = request.GET.get('signature')
    if block_id and signature:
        # delete block for block_id and signature
        Block.objects.filter(block_id=block_id).filter(signature=signature).delete()
    elif block_id:
        # Delete that block id
        Block.objects.filter(block_id=block_id).delete()
    elif signature:
        # Delete all the colors
        Block.objects.filter(signature=signature).delete()
    elif not block_id and not signature:
        # Delete blocks
        Block.objects.all().delete()

    # Send an empty Response
    return HttpResponse()
