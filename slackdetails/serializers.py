from restframework import serializers
from slackdetails.models import SlackDetails


class SlackdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackDetails
        fields = ['slackUsername', 'backend', 'age', 'bio']
