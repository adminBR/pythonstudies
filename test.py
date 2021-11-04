import asyncio
import datetime
import time
import requests
from plyer import notification
import json

msg = str(input('mensagem'))
notification.notify(
        title = ''+msg,
        message = ''+msg,
        app_icon = '',
        timeout = 10
    )