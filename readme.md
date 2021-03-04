# API_Automation_Test
```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

## need to install some libraries:
```
pip3 install pytest allure-pytest requests requests-toolbelt
```

## how to run auto api testcase:
```
python run.py
```

## exit python venv
```
deactivate
```

## not needed
```
pip install PyYaml faker
```

### how to run pytest cases with marks
e.g.
```
pytest -m http  # run cases that marked as [http]
```