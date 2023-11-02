import requests

if __name__ == '__main__':
    base_url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
    response = requests.get (base_url)
    print (response)

    if response.status_code == 200:              
        content = response.content # almacenar el contenido          
        print (response.content)

        content = response.content
        file = open ('dataset.csv', 'wb') # generar nuevo archivo 
        file.write (content)
        file.close ()
        

       
       
        