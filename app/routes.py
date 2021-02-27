import json

from flask import render_template, request, redirect, url_for

from app import app

@app.route('/')
@app.route('/index')
def index():
    # TODO: PERFORM GET ALL RULES
    rules = [{"name": "nombre1", "conditions": "[True]", "rule_type":"interval", "relays_used":"[1]", "active": False, "job_id": "someID"}]
    return render_template('index.html', rules=rules, th_message="SomeMessage")


@app.route('/')
@app.route('/edit', methods=["GET", "POST"])
def edit(id=None):
    if request.method == 'POST':
        name = request.form['name']
        conditions = request.form['conditions']
        rule_type = request.form['rule_type']
        frecuency = request.form['frecuency']
        relays_used = request.form['relays_used']
        true_action = request.form['true_action']
        false_action = request.form['false_action']
        work_time = request.form['work_time']
        sleep_time = request.form['sleep_time']
        teardown_action = request.form['teardown_action']
        actions_dict = json.dumps({"True": true_action, "False": false_action})
        # TODO: PERFORM EDIT REQUEST
        return redirect(url_for('index'))
    rule = {"activated": False, "name": "nombre1"}
    return render_template('edit.html', rule=rule, id=id)


@app.route('/')
@app.route('/toggle')
def toggle(id=None):
    # TODO: PERFORM toggle job!
    print("toggled!")
    return redirect(url_for('index'))
