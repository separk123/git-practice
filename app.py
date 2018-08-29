# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random
import csv

# names = []     이제 얘 말고 csv 통해서 저장할 것임.
# names = {}


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/result")
def result():
    # 한글 주석 써도 에러 안 난다. 이제.
    # 1. "/"에서 날아온 이름 두 개를 가져온다
    name1 = request.args.get('name1')
    name2 =request.args.get('name2')
    
    # 2. 궁합은 뻥 친다. (50~100개 사이에서 랜덤으로 뽑기)
    match = random.randrange(50, 101)
    
    # 같은 이름 여러 번 검색해도 궁합율은 같은 값만 나오게 하기
    # names.append(name1)
    # names.append(name2)
    
    # 'names.csv' 파일을 만들어서 저장한다.
    f = open('names.csv', 'a+')
    a = csv.writer(f)
    a.writerow([name1, name2])
    f.close
    a = csv.writer(f)
    
   #  names[name1] = name2     {}로 할 경우에~
    return render_template('result.html', name1 = name1, name2 = name2, match=match)
    
@app.route("/admin")
def admin():
    #names에 들어가 있는 모든 이름을 출력한다
    # return render_template('admin.html', names=names)
    f = open('names.csv', 'r')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html', names=names)
    
    
    

#app.run(host='0.0.0.0', port='8080', debug=True)