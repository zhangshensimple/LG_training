# encoding=utf-8

from flask import Flask, request, jsonify

app = Flask(__name__)

# 定义color接口，参数para 值为0 返回red，值为1 返回green 值为1 返回yello
@app.route('/color', methods=["GET"])
def color():
    try:
        para = int(request.args.get("para"))
    except ValueError:
        return jsonify(code = -2, msg="参数类型错误")
    # except TypeError:
    #     return jsonify(code = -3, msg="参数类型错误")
    if para == 0:
        return jsonify(code=0, msg="red")
    elif para == 1:
        return jsonify(code=1, msg="green")
    elif para == 2:
        return jsonify(code=2, msg="yellow")
    else:
        return jsonify(code=-1, msg="illegal，非法整型")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
