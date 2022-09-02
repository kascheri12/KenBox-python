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
    
    start_recursive = time.time()
    myKenBox = KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox())))))))))))))))))))))))))))))))))))))))))
    children_recur = myKenBox.getNumberOfChildBoxesRecursive()
    end_recursive = time.time()
    
    start_iterative = time.time()
    myOtherKenBox = KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox())))))))))))))))))))))))))))))))))))))))))
    children_iter = myOtherKenBox.getNumberOfChildBoxesIterative()
    end_iterative = time.time()
    
    start_counter = time.time()
    myThirdKenBox = KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox(KenBox())))))))))))))))))))))))))))))))))))))))))
    children_counter = myThirdKenBox.getNumberOfChildBoxesIterative()
    end_counter = time.time()
    
    time_recur = (end_recursive - start_recursive)
    time_iter = (end_iterative - start_iterative)
    time_counter = (end_counter - start_counter)
    perc_faster = (time_recur - time_iter) / time_iter * 100
    
    results = {
        'children_recur': children_recur,
        'time_recur': end_recursive - start_recursive,
        'children_iter': children_iter,
        'time_iter': end_iterative - start_iterative,
        'children_counter': children_counter,
        'time_counter': time_counter,
        'perc_faster': perc_faster
    }
    return render_template('index.html'
                ,children_recur=children_recur
                ,time_recur=time_recur
                ,children_iter=children_iter
                ,time_iter=time_iter
                ,children_counter=children_counter
                ,time_counter=time_counter
                ,perc_faster=perc_faster
                ,results=results)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
