# app.py
from flask import Flask, render_template, request, flash, redirect
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_list = [
        {
            'name': 'E-commerce Site',
            'description': 'A web application built with php and Laravel',
            'technologies': ['HTML', 'Bootstrap', 'PHP', 'CSS'],
            'github': 'https://github.com/Rupeshsanjel/Online-Bidding-System'
        },
        {
            'name': 'Vidmate',
            'description': 'Youtube Clone',
            'technologies': ['HTML', 'CSS', 'JavaScript'],
            'github': 'https://github.com/Rupeshsanjel/Vidtube'
        },
        {
            'name': 'Ecommerce',
            'description': 'Ecommerce  Website',
            'technologies': ['HTML', 'CSS', 'JavaScript', 'php', 'Laravel'],
            'github': 'https://github.com/Rupeshsanjel/ecomm'
        },
        {
            'name': 'Online Job Portal',
            'description': 'Job Site where employee can add job and jobseeker apply for the available job',
            'technologies': ['HTML', 'CSS', 'JavaScript', 'python', 'Flask', 'SQLite'],
            'github': 'https://github.com/RupeshSanzel/Online-Jobs-portal'
        },

    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/skills')
def skills():
    skills_list = {
        'Programming Languages': ['Python', 'JavaScript', 'Java', 'C++','C#'],
        'Web Technologies': ['HTML5', 'CSS3', 'React', 'Flask', 'Django'],
        'Databases': ['MySQL', 'PostgreSQL', 'MongoDB'],
        'Tools': ['Git', 'Docker', 'AWS', 'Linux','AIX']
    }
    return render_template('skills.html', skills=skills_list)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you would typically handle the form submission (e.g., send email)
        flash('Thanks for your message! I\'ll get back to you soon.', 'success')
        return redirect('/contact')
    return render_template('contact.html')

