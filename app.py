from flask import Flask, render_template, send_from_directory, redirect
import os
app = Flask(__name__)

@app.route("/")
async def index():
    return render_template("index.html", title="메인")

@app.route("/login")
async def login():
    return render_template("login.html", title="로그인", oauth_link="https://meme.orora.studio/")

@app.route("/discord")
async def discord():
    return render_template("redirect.html", title="공식 디스코드", redirect_url="https://discord.gg/RSUqQBzP9B")

@app.route("/invite")
async def bot_invite():
    return render_template("redirect.html", title="봇 초대하기", redirect_url="https://discord.com/oauth2/authorize?client_id=875908453548326922&permissions=412317240384&scope=bot%20applications.commands")

@app.route("/about")
async def about():
    return render_template("about.html", title="소개")

@app.route("/favicon.ico")
async def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "images/favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )

@app.route("/koreanbots")
async def koreanbots():
    return redirect("https://koreanbots.dev/bots/875908453548326922")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=6000)
