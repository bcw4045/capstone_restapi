from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import TextSerializer
# import pyttsx3


class TextToSpeechView(APIView):
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data['text']
        country = serializer.validated_data['country']

        # 텍스트를 음성으로 변환
        # engine = pyttsx3.init()
        # engine.save_to_file(text, 'output.wav')
        # engine.runAndWait()

        # WAV 파일을 클라이언트에게 반환
        with open('static/output.wav', 'rb') as f:
            response = Response(f.read(), content_type='audio/wav')
            response['Content-Disposition'] = 'attachment; filename="output.wav"'
            return response