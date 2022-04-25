from flask import Flask, request, jsonify
import json
from cn.dz import utils

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Hello World!"


@app.route("/a")
def a():
    import synonyms
    keywords = synonyms.keywords(
        "9月15日以来，台积电、高通、三星等华为的重要合作伙伴，只要没有美国的相关许可证，都无法供应芯片给华为，而中芯国际等国产芯片企业，也因采用美国技术，而无法供货给华为。目前华为部分型号的手机产品出现货少的现象，若该形势持续下去，华为手机业务将遭受重创。")
    return str(keywords)


# 解析 POST 请求参数
@app.route("/wyc", methods=["POST"])
def wyc():
    text = request.form.get('text')
    print("获取到内容 [ {} ]".format(text))
    return utils.words_change(text)


if __name__ == "__main__":
    app.run(debug=True)
