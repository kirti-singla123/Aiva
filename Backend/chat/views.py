from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
import requests
import os

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # ✅ Get Real IST Time
        current_time = timezone.localtime().strftime("%A, %d %B %Y, %I:%M %p")

        # ✅ If user explicitly asks for time/date
        if any(word in user_message.lower() for word in ["time", "date", "today", "day"]):
            return JsonResponse({
                "response": f"The current time is {current_time} IST."
            })

        # ✅ Normal clean assistant behavior
        prompt = f"""
You are AIVA, a smart and friendly AI assistant.
Reply naturally and conversationally.
Do NOT mention current date or time unless the user asks.

User: {user_message}
Assistant:
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()
        ai_reply = result.get("response", "").strip()

        return JsonResponse({"response": ai_reply})

    return JsonResponse({"error": "Only POST allowed"})
def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>AIVA Backend</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: #ffffff;
                padding: 40px 60px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 500px;
            }
            h1 {
                color: #0f4c75;
                margin-bottom: 20px;
            }
            p {
                color: #333333;
                margin: 10px 0;
            }
            .highlight {
                color: #3282b8;
                font-weight: bold;
            }
            ul {
                text-align: left;
                padding-left: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AIVA Backend</h1>
            <p>Welcome to the <span class="highlight">AIVA AI Assistant</span> backend.</p>
            <p>This backend currently handles:</p>
            <ul>
                <li>Chat handling</li>
                <li>API endpoints for connected frontend apps</li>
            </ul>
            <p><span class="highlight">frontend Connected:</span> React App</p>
            <p><span class="highlight">Developed by:</span> Kirti Singla</p>
            <p><span class="highlight">Status:</span> Active & Running</p>
        </div>
    </body>
    </html>
    """)
