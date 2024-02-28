step 1                       
clone the project                          
git clone https://github.com/athultch/DRFCRED.git                 
open the DRFCRED file                               
step 2                                         
Create Virtual Environment                      
           
Windows:                           
python -m venv myenv                              
Activate Virtual Environment: myenv\Scripts\activate
                                 
macOS and Linux:                                  
python3 -m venv myenv Activate Virtual Environment: source myenv/bin/activate
                                 
step 3                                       
Install Dependencies from requirements.txt                                                                         

pip install -r requirements.txt                                    
                               
step 4                                         
python manage.py makemigrations                                
python manage.py migrate                                   
                                           
step 5                                                                          
python manage.py runserver

step 6                                         
check with endpoint in API tester or in web


