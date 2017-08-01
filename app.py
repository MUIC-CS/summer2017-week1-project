from flask import Flask, request, render_template

posts = []
app = Flask('wall')


@app.route('/', methods=["GET", "POST"])
def index():
    if "message" in request.form:
        posts.append(request.form["message"])
    return render_template('index.html', posts=reversed(posts))


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
