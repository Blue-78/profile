from flask import Flask, render_template, send_from_directory,request,redirect,url_for
import csv

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thankyou')
def thankyou4():
    return render_template('thankyou.html')

@app.route('/<string:page>')
def custom_page(page):

        return render_template(page)

def writetocsv(data):
 with open("db.csv","a",newline='') as database:
    email=data["email"]
    subject=data["subject"]
    message=data["message"]
    db=csv.writer(database,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)

    db.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST','GET'])
def sendmessage():

    if request.method == 'POST':
        data=request.form.to_dict()
        writetocsv(data)
        with open("database.txt","a") as w:

               w.write(str(data))
               w.write("\n") #move the cursor to new line after writing data to the file

        return redirect(url_for('thankyou4')) #used method thankyou4
    else:
         return "something went wrong"


# @app.route('/works')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/components')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/work')
# def work():
#     return render_template('work.html')
# @app.route('/<username>/<int:id>')
# def hello_w1(username= None,id=None):
#     return render_template('index.html', name=username,id=id)


# def outer(x):
#     def inner(y):
#         return x + y
#
#     return inner
#
#
# x = outer('o')
# j = x('h')  # return func of outer i.e inner()
# print(j)
#
#
# def deco(f):
#     def wrap():
#         print("before")
#         f()
#         print("after")
#
#     return wrap
#
#
# def r():
#     return "me"
#
#
#
# print(r())
app.run(debug=True)
