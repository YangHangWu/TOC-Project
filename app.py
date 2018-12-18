from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "123"
machine = TocMachine(
    states=['final','user','state0','state1','state2','state3','state4','state5','state6','state7','state8','state9'],
    transitions=[
        {
            'trigger': 'go_to',
            'source': 'user',
            'dest': 'state0',
        },
        {
            'trigger': 'advance',
            'source': 'state0',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state0',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
	{
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
	{
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },

        {
            'trigger': 'go_back',
            'source': [ 'state3','state4','state5','state6'],
            'dest': 'final'
        },
        {
            'trigger': 'again',
            'source': 'final',
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if machine.state=='user':
           machine.go_to(event)
        else:
           machine.advance(event)
    return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    machine.get_graph().draw('show-fsm.png', prog='dot')
    run(host="localhost", port=5000, debug=True, reloader=True)
