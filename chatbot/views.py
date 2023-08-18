from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
import openai


def chatbot(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        # print(f'user_input：{input_text}')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=1024,
            api_key='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'
        )
        chatbot_response = response.choices[0].text.strip()
        return JsonResponse({'response': chatbot_response})

    return render(request, 'chatbot.html')

