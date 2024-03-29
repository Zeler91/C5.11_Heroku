import os
import random
import sayings
from bottle import route, run


def generate_message():
  beginning = sayings.beginnings[random.randrange(7)]
  subject = sayings.subjects[random.randrange(7)]
  verb = sayings.verbs[random.randrange(7)]
  action = sayings.actions[random.randrange(7)]
  end = sayings.ends[random.randrange(7)]
  result = "{} {} {} {} {}".format(beginning, subject, verb, action, end)
  return result


@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
""".format(
        generate_message()
    )
    return html


@route("/api/generate/")
def example_api_response():
  return {"message": generate_message()}

@route("/api/generate/<some_id:int>")
def example_api_response(some_id):
  str_list = []
  for x in range(some_id):
    str_list.append(generate_message())
  return {"messages": str_list}


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
