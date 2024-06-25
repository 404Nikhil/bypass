generate a `requirements.txt` file:

Navigate to the directory containing your Python project.
```
pip freeze > requirements.txt
```

use this `requirements.txt` file to install the required packages:
```
pip install -r requirements.txt
```

use 
```
streamlit run app.py
```

launcher scripts are attached for windows(.bat) and linux(.sh)