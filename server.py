import os
from datetime import datetime as dt
import random
import json
from bottle import route, run, static_file, view


# @route("/")
# def index():
#     return "<h1>Success!</h1>"

@route("/api/forecasts")
def api_forecasts():
    times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
    advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
    promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]
    prophecies_list = {}
    prophecies = ''
    generated_prophecies = []
    for i in range(0,6):
        one_prophecie = ""
        for j in range(0,2):
            one_prophecie = one_prophecie + random.choice(times).capitalize()+" "+random.choice(advices).lower()+" "+random.choice(promises).lower()+". "
        generated_prophecies.append(one_prophecie.rstrip(' '))
    prophecies_list["prophecies"] = generated_prophecies
    prophecies = json.dumps(prophecies_list, sort_keys=False, indent=3)
    return prophecies


@route("/api/roll/<some_id:int>")
def example_api_response(some_id):
    return {
        "requested_id": some_id,
        "random_number": randrange(some_id)
    }


@route("/")
@view("home")
def example_template_render():
    return {"now": dt.now().isoformat()}


@route('/css/<filename>')
def send_css(filename):
    return static_file(filename, root='static/css')

@route('/js/<filename>')
def send_js(filename):
    return static_file(filename, root='static/js')

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
