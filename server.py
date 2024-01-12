#This page is now dynamic and we donot need to add code everytime we add a new file.

from flask import Flask, render_template, request, redirect
import csv
import os
print('current dir:', os.getcwd())

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

#Disabling Favicon Request.
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

'''-----------------------------------------------------------------------------------------------------'''

#writing into the 'database.csv' file.
def write_to_csv(data):
    print('current dir:', os.getcwd())
    try:
        with open('./database/database.csv', mode='a', newline='') as database:
            email = data['email']
            subject = data['subject']
            message = data['message']

            csv_writer = csv.writer(database, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])
    except Exception as e:
            print(f"Error while saving to database: {str(e)}")

'''-----------------------------------------------------------------------------------------------------'''

#Giving the User Some reply and also opening a new html page to give the response.
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()         #{'email': 'sachin1712003@gmail.com', 'subject': 'abc', 'message': 'hi'}
            print(f"Received data: {data}")     #Remove the {data} when deploying the server. As it shows the data in logs. It useful for testing.
            write_to_csv(data)
            print("Data written to database.csv successfully")
            return redirect('thankyou.html')
        except:
            return 'Saving to Database Failed !'
    else:
        return 'Something went wrong. Try again!'


# #test code.
# data = {'email': 'sachin1712003@gmail.com', 'subject': 'abc', 'message': 'hi'}
# write_to_csv(data)

