from django.shortcuts import render
from django.http import HttpResponse
from restframework import status
from restframework.response import Response
from restframework.decorators import api_view
from slackdetails.models import SlackDetails
from slackdetails.serializers import SlackDetailsSerializer

# Create your views here.

@api_view['GET', 'POST']
def slackdetails(request):
    if request.method == 'GET':
        slack = SlackDetails.objects.all()
        serializer = SlackDetailsSerializer(slack)
        return Response(serializer.data)
    elif request.method == 'POST':
        slack_details = SlackDetailsSerializer(data=request.data)
        if slack_details.isvalid():
            slack_details.save()
            return Response(slack_details.data, status=status.HTTP_201_CREATED)
        else:
            return Response(slack_details.error, status=status.HTTP_400_BAD_REQUEST)


