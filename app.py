from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello"


@app.route('/api/user')
def user():
    data = {
        'name': '张三',
        'age': 18,
        'city': '北京',
        'hobby': ['篮球', '足球', '游泳']
    }
    return jsonify(data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 在这里进行用户名和密码的验证逻辑
        if username == 'admin' and password == '123456':
            return '登录成功'
        else:
            return '登录失败'
    else:
        return render_template('login.html')  # 这里假设你已经创建了名为 login.html 的模板


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
