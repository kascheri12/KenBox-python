#
# KenBox WebApp
#
from KenBox import KenBox
from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    children = None
    
    myKenBox = KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox())))))))))))))))))))))))))))))))))))))))))
    start_recursive = time.time()
    children_recur = myKenBox.getNumberOfChildBoxesRecursive()
    end_recursive = time.time()
    
    start_iterative = time.time()
    children_iter = myKenBox.getNumberOfChildBoxesIterative()
    end_iterative = time.time()
    
    time_recur = (end_recursive - start_recursive)
    time_iter = (end_iterative - start_iterative)
    perc_faster = (time_recur - time_iter) / time_iter * 100
    
    results = {
        'children_recur': children_recur,
        'time_recur': end_recursive - start_recursive,
        'children_iter': children_iter,
        'time_iter': end_iterative - start_iterative,
        'perc_faster': perc_faster
    }
    return render_template('index.html'
                ,children_recur=children_recur
                ,time_recur=time_recur
                ,children_iter=children_iter
                ,time_iter=time_iter
                ,perc_faster=perc_faster
                ,results=results)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
