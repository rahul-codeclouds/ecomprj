# ecomprj_fullstack

 ## Project Description-

This is an Ecommerce website project using Django. 
The name of the website is Hmart which consists of-
   #### front-end side
  - a homepage
  - a products page
  - a product modal
  - a cart detail page
  - checkout page
  - placeorder page
  - thank you page

### Let's start-
1. Open the terminal and install the following requirements-
   -django
   -Pillow
   -django-shopping-cart
   -django-ckeditor
2. start a project-
   ```
   django-admin startproject ecomprj
   ```
3. start an app-
   ```
   django-admin startapp ecomapp
   ```
4. change the current working directory to ecomprj
   ```
   cd ecomprj
   ```
5. Go to \ecomprj\settings.py and add the following in the Installed Apps
   ```
   INSTALLED_APPS = [
    'ecomapp',
    'ckeditor',
    'cart',
   ...
   ]
   ```
6. Create a template and static file directory in ecomprj\ or just create a new folder by these two names
  ```
  mkdir templates
  ```
  ```
  mkdir static
  ```
7. In the settings.py import os and add paths to the templates and static folders
   ```
   import os
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...
                
            ],
        },
    },
   ]
   ```
   STATIC_URL = 'static/'
   STATICFILES_DIRS = [
     BASE_DIR / "static",
     os.path.join(BASE_DIR, "static") 
    
   ]

   STATIC_ROOT = os.path.join(BASE_DIR,'/static/')
   ```

### Project results-

**1. Homepage-**
   ![1](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/f1138d5f-f5a8-4880-afac-d782d2336bc9)
   
**2. products page-**
   ![2](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/2b29e576-f76a-4718-95ec-c22c921bfea0)
   
**3. product modal-**
   ![3](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/058d70ca-454f-46ba-988d-ea07d5add87e)
   
**4. Add to Cart-**
   ![5](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/c51f944a-e6a2-41e3-9eea-2b4e516bce10)
   
**5. Cart details-**
   ![6](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/7436502f-62b1-4d12-b722-2a3b0b3d9de7)
   
**6. checkout page-**
   ![7](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/f3b0137d-b6c1-44ac-b6ed-680c3161362a)
   
**7. place order-**
   ![17](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/911eccee-cf73-4091-b7ef-df61f041c09a)
   
**8. Thank you-**
   ![9](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/8af8690a-c5a2-475a-b4da-5004eeb2ef99)
   
**9. Login/Register-**
    ![18](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/7fa3dcc8-81de-4a10-bfbe-09d61e21df3b)
    ![11](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/8c3bf974-4616-4f8c-8804-814c837f1fe1)
    
**10. Contact Us-**
    ![4](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/e8b30695-658b-415d-95db-98a9f303acd6)
    
**11. admin side(Products Model)-**
    ![12](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/59423db1-e7a9-4699-958a-f808cbd1b932)
    ![13](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/6428676f-161e-4fd5-9643-b9b7db82db51)
    ![14](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/5f765902-4bd6-425f-a0eb-f3e6d54204cf)
    ![15](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/5db6c901-2fb9-4d47-8d6e-c6a9740f951a)
    ![16](https://github.com/rahul-codeclouds/ecomprj/assets/158029174/98bdfbc5-9729-4cde-b599-ad10d9117e3c)

















  
   

