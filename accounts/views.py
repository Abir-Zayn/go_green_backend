import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    data = {
        "message": f"Hello, {request.user.first_name}! welcome to Go Green Backend"
    }
    return Response(data)

from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_email(request):
    try:
        send_mail(
            'Test Subject',
            'Test Message',
            os.getenv('EMAIL_HOST_USER'),  # from email
            [os.getenv('EMAIL_HOST_USER')],  # to email (sending to yourself for testing)
            fail_silently=False,
        )
        return Response({"message": "Email sent successfully"})
    except Exception as e:
        return Response({
            "error": str(e),
            "email_user": os.getenv('EMAIL_HOST_USER'),  # This will help verify if env vars are loaded
            "email_pass_length": len(os.getenv('EMAIL_HOST_PASSWORD')) if os.getenv('EMAIL_HOST_PASSWORD') else 0
        })
