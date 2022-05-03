from flask import Flask, render_template, session
from dp_test.route.match_route import bp as mr


app = Flask(__name__)  #웹 어플리케이션

app.secret_key = 'asfaf' #세션 사용시 시크릿 키 설정

app.register_blueprint(mr)

@app.route('/')  # 요청 url 등록
def root():
    '''
    로그아웃 처리
    session.pop('flag')
    session.pop('loginid')
    '''
    return render_template('index.html')

# @app.route('/chart')
# def chart():
#     render_template('/match/chart.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__=='__main__':
    # app.run(port=8000)
    app.run()