from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    name1 = request.form['name1']
    name2 = request.form['name2']
    love_prob = love_probability(name1, name2)
    return render_template('result.html', name1=name1, name2=name2, love_prob=love_prob)


def love_probability(name1,name2):
    # Định dạng lại tên
    name1 = name1.title()
    name2 = name2.title()
    # Tính tổng mã ASCII của các ký tự trong hai tên
    name1_ascii_sum = sum(ord(c) for c in name1)
    name2_ascii_sum = sum(ord(c) for c in name2)
    total_ascii_sum = name1_ascii_sum + name2_ascii_sum
    # Tính giá trị từ 1 đến 10
    compatibility_value = ((total_ascii_sum % 100) / 10) + 1

    # Tính xác suất
    love_probability = compatibility_value * 10

    return love_probability

if __name__ == '__main__':
    app.run(debug=True)
