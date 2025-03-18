from django.shortcuts import render

import os
import subprocess
from django.http import HttpResponse
from datetime import datetime
import pytz

def htop_view(request):
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')
    system_username = os.getenv("USER") or os.getenv("USERNAME")
    top_output = subprocess.getoutput("top -b -n 1 | head -n 10")

    response = f"""
    <html>
    <body>
        <h1>Name: Nikitha Duvvurime</h1>
        <h2>Username: {system_username}</h2>
        <h3>Server Time: {server_time}</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response)
