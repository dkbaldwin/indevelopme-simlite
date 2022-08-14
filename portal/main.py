from flask import Flask
from pathlib import Path
from flask import render_template

#create application
app = Flask(__name__)

# load the views
@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/admin')
def admin_landing_page():
    return render_template('administration.html')

# renders the manual login page
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def user_logout():
    return render_template('logout.html')

def get_extra_files():
    for bp in (app.blueprints or {}).values():
        macros_dir = Path(bp.root_path)
        for filepath in macros_dir.rglob('*.html'):
            yield str(filepath)

# run flask application
if __name__ == '__main__':
    app.run(extra_files=list(get_extra_files()))
