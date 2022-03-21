from flask import Flask, render_template
from echarts_bigscreen.index_enc import get_index_data
import utils

app = Flask(__name__)


# 定义函数，网页打开输出index.html大屏的内容


@app.route('/')
def Ren_echarts():
    dict_return = get_index_data()
    return render_template('index.html', dict_return=dict_return)


@app.route('/time')
def get_time():
    return utils.get_time()


if __name__ == '__main__':
    app.run()
