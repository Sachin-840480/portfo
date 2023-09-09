#This page is now dynamic and we donot need to add code everytime we add a new file.

#We wrap the 'submit_form' block in a 'try-except' block to catch 'error' more effectively.

from flask import Flask, render_template, request, redirect
import csv 


app = Flask(__name__)
print(__name__)

#Home Page
@app.route('/')
def my_home():
    return render_template('index.html')

'''-----------------------------------------------------------------------------------------------------'''

#making it dynamic.
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

'''-----------------------------------------------------------------------------------------------------'''

#writing into the 'database.csv' file.
def write_to_csv(data):
    with open('./database/database.csv', mode = 'a', newline = '') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

'''-----------------------------------------------------------------------------------------------------'''

#Giving the User Some reply and also opening a new html page to give the response.
@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST': 
        try:    
            data = request.form.to_dict() #{'email': 'sachin1712003@gmail.com', 'subject': 'abc', 'message': 'hi'}
            write_to_csv(data)              
            return redirect('thankyou.html') 
        except:
            return 'Saving to Database Failed !'
    else:
        return 'Something went wrong. Try again!'