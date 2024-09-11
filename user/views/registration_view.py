from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.serializers.serializer import UserSerializer
# from user.shared_tasks.registration_email import send_registration_email
from user.shared_tasks.kafka_producer import KafkaProducer
class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            # send_registration_email.delay('email',serializer.data)
            # publish user data to kafka topic
            kafka = KafkaProducer()
            kafka.publish_message('user-registration', serializer.data)
            return Response(
                {
                    'user': serializer.data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request):
        id = request.query_params.get('id')
        user = User.objects.get(id=id)
        serializer = self.serializer_class(user)
        kafka = KafkaProducer()
        kafka.publish_message('registration', serializer.data)
        # send_registration_email.delay('email', {'data':serializer.data})
        return Response(serializer.data)
