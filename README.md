# Blog_Api
This repository contains an Api for a Blog site created using FastApi framework of python.

## Getting Setup

#### Clone Repository
```git clone https://github.com/savageclown007/Blog_Api.git```

#### Enter the directory
```cd Blog_Api```

#### Install all the requirements
```pip instal -r requirements.txt```

#### Run the server
```uvicorn main:app --reload```

##### The command ```uvicorn main:app``` refers to:

* ```main```: the file main.py (the Python "module").
* ```app```: the object created inside of main.py with the line app = FastAPI().
* ```--reload```: make the server restart after code changes. Only use for development.

#### In the output, there's a line with something like:


```INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)```
##### You can find the Documentation of the Api at ```http://127.0.0.1:8000/docs``` or  ```http://127.0.0.1:8000/re-doc```
