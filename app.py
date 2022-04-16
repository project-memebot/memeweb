from sanic import Sanic, response, request
from sanic.response import json, text, html, redirect
from sanic.exceptions import (
    InvalidUsage,
    Unauthorized,
    Forbidden,
    NotFound,
    ServerError,
    URLBuildError,
)
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

app = Sanic(__name__)

app.static("/static", "./static")
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html", "xml", "tpl"]),
)

def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))

@app.route("/")
async def index(request):
    return template("index.html", title="메인")


@app.route("/login")
async def login(request):
    return template("login.html", title="로그인", oauth_link="https://meme.orora.studio/")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=6000)
