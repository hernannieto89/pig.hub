import json
import requests

from flask import render_template, request, redirect, url_for

from app import app

RULES_URL = "http://localhost:5000/rules/"

RULES_INFO_URL = "http://localhost:5000/rules/{}"

HT_INFO_URL = "http://localhost:5000/sensors/{}/{}"

@app.route('/')
@app.route('/index')
def index():
    # TODO: PERFORM GET ALL RULES
    rules = requests.get(RULES_URL)
    print(rules)
    return render_template('index.html', rules=rules.json(), th_message=ht())


@app.route('/')
@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    rule = requests.get(RULES_INFO_URL.format(id)).json()

    if request.method == 'POST':
        update_form = {}
        name = request.form.get('name')
        conditions = request.form.get('conditions')
        rule_type = request.form.get('rule_type')
        frecuency = request.form.get('frecuency')
        relays_used = request.form.get('relays_used')
        true_action = request.form.get('true_action')
        false_action = request.form.get('false_action')
        work_time = request.form.get('work_time')
        sleep_time = request.form.get('sleep_time')
        teardown_action = request.form.get('teardown_action')
        if name != "" :
            update_form["name"] = name
        if conditions != "":
            update_form["conditions"] = conditions
        if rule_type != "":
            update_form["rule_type"] = rule_type
        if frecuency != "":
            update_form["frecuency"] = frecuency
        if relays_used != "":
            update_form["relays_used"] = relays_used
        if work_time != "":
            update_form["work_time"] = work_time
        if sleep_time != "":
            update_form["sleep_time"] = sleep_time
        if true_action != "" and false_action != "":
            update_form["actions_dict"] = json.dumps({"True": true_action, "False": false_action})
        if teardown_action != "":
            update_form["teardown_action"] = teardown_action
        requests.put(RULES_INFO_URL.format(id), data=update_form)
        return redirect(url_for('index'))
    return render_template('edit.html', rule=rule, id=id)


@app.route('/')
@app.route('/toggle/<int:id>')
def toggle(id):
    requests.post(RULES_INFO_URL.format(id))
    return redirect(url_for('index'))


def ht():
    response = requests.get(HT_INFO_URL.format("DHT11", "1")).json()
    msg = "Temperature: {} - Humidity: {}".format(response["T"], response["H"])
    return msg
