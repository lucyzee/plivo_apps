#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plivo
# Your PLIVO_AUTH_ID and PLIVO_AUTH_TOKEN can be found on your Plivo Dashboard https://manage.plivo.com/dashboard
PLIVO_AUTH_ID = "Enter your Plivo AUTH ID here"
PLIVO_AUTH_TOKEN = "Enter your Plivo AUTH TOKEN here"
# Enter your Plivo phone number. This will show up on your caller ID
plivo_number = "14153337777"
# Enter the phone number that you would like to receive your SMS
destination_number = "14153338888"
# Enter the SMS that you want to send
text = "Welcome to Plivo!"
message_params = {
      'src':plivo_number,
      'dst':destination_number,
      'text':text,
    }
p = plivo.RestAPI(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)
print p.send_message(message_params)