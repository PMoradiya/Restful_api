## Requirement
- Create a REST service to allow other systems to query the information. 
- The API should expose:
    - Return the 10 most risky vulnerabilities for a specific host;
    - Return the vulnerabilities in alphabetical order for a specific host. This API must support pagination.

## Built With

- Python 3.8.x - Programming Language
- Flask - The framework used
- Pip - Dependency Management


## Project Setup 
1. Install the packages 
    
        python -m pip install -r requirements.txt
    
2. Run the server
        
        python src/app.py
   
3. In the browser, open the below URL
   
        http://127.0.0.1:5000/top10vulnerabilities?hostip=10.128.35.79

        [Take any hostip from csv and replace with hostip on URL]

4. To check pagination
        
        http://127.0.0.1:5000/top10vulnerabilities/?hostip=10.128.35.79&page=1

        [change page number]




        