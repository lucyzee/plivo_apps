import plivo, plivoxml

auth_id = "MAODU4MTK1MDC0NTBMMM"
auth_token = "MWVkNWNlZWFlYjRmYmViNDBiZDAwNjA0NjA5OTQz"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'to': '14153163136', # The phone numer to which the all has to be placed
    'from' : '1111111111', # The phone number to be used as the caller id
    'answer_url' : "http://morning-ocean-4669.herokuapp.com/speak/", # The URL invoked by Plivo when the outbound call is answered
    'answer_method' : "GET", # The method used to call the answer_url
    # Example for Asynchrnous request
    #'callback_url' : "http://morning-ocean-4669.herokuapp.com/callback/", # The URL notified by the API response is available and to which the response is sent.
    #'callback_method' : "GET" # The method used to notify the callback_url.
}

# Make an outbound call
response = p.make_call(params)
print str(response)