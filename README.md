Running a Flask application:

1. Navigate to your project directory (the folder where your app.py is located):

```cd /path/to/your/project```

2. Set the FLASK_APP environment variable (if necessary):

- On Linux/macOS:  ```export FLASK_APP=app.py```

- On Windows (Command Prompt): ```set FLASK_APP=app.py```

- On Windows (PowerShell): ```$env:FLASK_APP = "app.py"```

3. Run Flask:
```flask run```

4. Access your app in a browser:

Go to: http://127.0.0.1:5000/ or http://localhost:5000/ in your browser.

If you're running the app in debug mode, you can add this command before running:
```export FLASK_ENV=development```
Or for Windows Command Prompt:
```set FLASK_ENV=development```
In PowerShell:
```$env:FLASK_ENV = "development"```

