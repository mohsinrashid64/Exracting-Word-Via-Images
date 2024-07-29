product_purchase =  [
    {
        "role": "system",
        "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
    },
    {
        "role": "user",
        "content": [{
                        "type": "text", 
                        "text": '''
                                Please help me extract the textual pieces of information from the image provided. Your job is to extract all of the aforementioned from the image.The desired output I want to receive is in JSON format and just this nothing else. If you are unable to find any of the details in the image please add ‘N/A’ in the json with the respective key. Please observe the image carefully and extract the words as they are in the image, regardless whether they make sense or not.

                                I am a professional Mobile application developer in Flutter. I am making an application for my client. The app is an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image. This data will be used to fill in the input fields.

                                This app is intended for businesses that wish to maintain and store their records efficiently, enabling them to store data simply by capturing a photo of their documents.

                                The data that I want you extract from the image are the following:
                                1. Delivery Cost
                                2. Payment Mode 
                                3. Vendor (this could have the following details):
                                    1. Name
                                    2. Street Address
                                    3. City 
                                    4. State
                                    5. Zipcode
                                    6. Phone Number
                                    7. Email Address
                                4. Purchase Date (Please Convert the date in the following formate when storing it in the JSON “DD/MM/YYYY”)
                                5. Reference Number
                                6. Purchase Description
                                7. Products List (this could have the following details):
                                    1. Product Name
                                    2. Amount 
                                    3. Product Quantity
                                    4. Tax
                                8. Currency Symbol (this could be any currency symbol that exists and what you find)
                                9. Tax Status (this is a boolean, such that it is true if there is tax and false if there is no tax)

                                Please note that, all of the aforementioned fields may not have the same wording as given, rather you should extract the relevant data according to meaning and context.

                                Finally I want the response to be in a JSON format and just that, nothing else, do not even add ```json or anything else like punctuations or any other thing, this is of the utmost importance when it comes to the response. The JSON response needs to have the following structure:
                                {
                                    'delivery_cost': '<value>', (Please do not add currency symbol)
                                    'payment_mode': '<value>',
                                    'vendor': [
                                        {
                                            'name': '<value>',
                                            'street_address': '<value>',
                                            'city': '<value>', 
                                            'state': '<value>',
                                            'zipcode': '<value>',
                                            'phone_number': '<value>',
                                            'email_address': '<value>'
                                        }.
                                …
                                    ],
                                    'purchase_date': '<value>',
                                    'reference_number':  '<value>',
                                    'purchase_description': '<value>',
                                    'products_list': [
                                        {
                                            'product_name': '<value>,'
                                            'amount': '<value>,' (Please do not add currency symbol and also do not multiply with product quantity, keep the amount of an individual product)
                                            'product_quantity': '<value>',
                                            'tax': '<value>'

                                        },
                                        …,
                                    ],
                                    'currency_symbol': '<value>',
                                    'tax_status': '<value>'
                                    
                                }

                                Replace the “<value>” with the appropriate data you extract from the image. The “...” in the JSON structure denotes that there could be multiple entries.
                                '''
                    }
        ]
    }
]



invoice_list =  [
    {
        "role": "system",
        "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
    },
    {
        "role": "user",
        "content": [{
                        "type": "text", 
                        "text": '''
                                Please help me extract the textual pieces of information from the image provided. Your job is to extract all of the aforementioned from the image.The desired output I want to receive is in JSON format and just this nothing else. If you are unable to find any of the details in the image please add ‘N/A’ in the json with the respective key. Please observe the image carefully and extract the words as they are in the image, regardless whether they make sense or not.

                                I am a professional Mobile application developer in Flutter. 

                                I am making an application for my client. The app is an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image. This data will be used to fill in the input fields.
                                This app is intended for businesses that wish to maintain and store their records efficiently, enabling them to store data simply by capturing a photo of their documents.

                                The data that I want you extract from the image are the following:
                                1. Income Account
                                2. Amount 
                                3. Payment Mode
                                4. Customers (this could have the following details):
                                    1. Name
                                    2. Street Address
                                    3. City 
                                    4. State
                                    5. Zipcode
                                    6. Phone Number
                                    7. Email Address
                                    8. Credit Terms
                                5. Invoice Date (Please Convert the date in the following formate when storing it in the JSON “DD/MM/YYYY”)
                                6. Reference Number
                                7. Income Description
                                8. Products List (this could have the following details):
                                    1. Product Name
                                    2. Amount 
                                    3. Product Quantity
                                    4. Tax
                                9. Currency Symbol (this could be any currency symbol that exists and what you find)
                                10. Tax Status (this is a boolean, such that it is true if there is tax and false if there is no tax)



                                Please note that, all of the aforementioned fields may not have the same wording as given, rather you should extract the relevant data according to meaning and context.

                                Finally I want the response to be in a JSON format and just that, nothing else, do not even add ```json or anything else like punctuations or any other thing, this is of the utmost importance when it comes to the response. The JSON response needs to have the following structure:
                                {
                                    "income_account": '<value>',
                                    "amount": '<value>', (Please do not add currency symbol)
                                    "payment_mode": '<value>',
                                    "customers": [
                                        {
                                            "name": '<value>',
                                            "street_address": '<value>',
                                            "city": '<value>', 
                                            "state": '<value>',
                                            "zipcode": '<value>',
                                            "phone_number": '<value>',
                                            "email_address": '<value>',
                                            "credit_terms": '<value>'
                                        },
                                        …
                                    ],
                                    "invoice_date": '<value>',
                                    "reference_number": '<value>',
                                    "income_description": '<value>'
                                    "products_list": [
                                        {
                                            "product_name": '<value>',
                                            "amount": '<value>', (Please do not add currency symbol and also do not multiply with product quantity, keep the amount of an individual product)
                                            "product_quantity": '<value>'
                                            "tax": '<value>' 
                                        },
                                        …
                                    ],
                                    'currency_symbol': '<value>'
                                    'tax_status': '<value>'
                                }
                                Replace the “<value>” with the appropriate data you extract from the image. The “...” in the JSON structure denotes that there could be multiple entries.
                                '''
                    }
        ]
    }
]



cash_sale =  [
    {
        "role": "system",
        "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
    },
    {
        "role": "user",
        "content": [{
                        "type": "text", 
                        "text": '''
                                Please help me extract the textual pieces of information from the image provided. Your job is to extract all of the aforementioned from the image.The desired output I want to receive is in JSON format and just this nothing else. If you are unable to find any of the details in the image please add ‘N/A’ in the json with the respective key. Please observe the image carefully and extract the words as they are in the image, regardless whether they make sense or not.

                                I am a professional Mobile application developer in Flutter. 

                                I am making an application for my client. The app is an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image. This data will be used to fill in the input fields.

                                This app is intended for businesses that wish to maintain and store their records efficiently, enabling them to store data simply by capturing a photo of their documents.
                                The data that I want you extract from the image are the following:
                                1. Income Account
                                2. Payment Mode
                                3. Customers (this could have the following details):
                                    1. Name
                                    2. Street Address
                                    3. City 
                                    4. State
                                    5. Zipcode
                                    6. Phone Number
                                    7. Email Address
                                    8. Credit Terms
                                4. Date (Please Convert the date in the following formate when storing it in the JSON “DD/MM/YYYY”)
                                5. Reference Number
                                6. Income Description
                                7. Products List (this could have the following details):
                                    1. Product Name
                                    2. Amount 
                                    3. Product Quantity
                                    4. Tax
                                8. Currency Symbol (this could be any currency symbol that exists and what you find)
                                9. Tax Status (this is a boolean, such that it is true if there is tax and false if there is no tax)



                                Please note that, all of the aforementioned fields may not have the same wording as given, rather you should extract the relevant data according to meaning and context.

                                Finally I want the response to be in a JSON format and just that, nothing else, do not even add ```json or anything else like punctuations or any other thing, this is of the utmost importance when it comes to the response. The JSON response needs to have the following structure:
                                {
                                    "income_account": <value>,
                                    "payment_mode": <value>,
                                    "customers": [
                                        {
                                            "name": <value>,
                                            "street_address": <value>,
                                            "city": <value>, 
                                            "state": <value>,
                                            "zipcode": <value>,
                                            "phone_number": <value>,
                                            "email_address": <value>
                                            "credit_terms": <value>
                                            },
                                            …
                                        ],
                                        date:  <value>,
                                        reference_number:  <value>,
                                        income_description: <value>
                                    
                                        products_list: [
                                            {
                                                "product_name": <value>,
                                                "amount": <value>, (Please do not add currency symbol and also do not multiply with product quantity, keep the amount of an individual product)
                                                "product_quantity": <value>
                                                "tax": <value>
                                            },
                                                …
                                        ],
                                        'currency_symbol': '<value>',
                                        'tax_status': '<value>'
                                    }
                                    Replace the “<value>” with the appropriate data you extract from the image. The “...” in the JSON structure denotes that there could be multiple entries.
                                    '''
            }
        ]
    }
]


vendor = [
    {
        "role": "system",
        "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
    },
    {
        "role": "user",
        "content": [{
                        "type": "text", 
                        "text": '''
                                Please help me extract the textual pieces of information from the image provided. Your job is to extract all of the aforementioned from the image.The desired output I want to receive is in JSON format and just this nothing else. If you are unable to find any of the details in the image please add ‘N/A’ in the json with the respective key. Please observe the image carefully and extract the words as they are in the image, regardless whether they make sense or not.

                                I am a professional Mobile application developer in Flutter. 

                                I am making an application for my client. The app is an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image. This data will be used to fill in the input fields.

                                This app is intended for businesses that wish to maintain and store their records efficiently, enabling them to store data simply by capturing a photo of their documents.

                                The data that I want you extract from the image are the following:
                                1. Name
                                2. Street Address
                                3. City
                                4. Sate
                                5. Zipcode
                                6. Phone Number
                                7. Email Address
                                8. Currency Symbol (this could be any currency symbol that exists and what you find)
                                9. Tax Status (this is a boolean, such that it is true if there is tax and false if there is no tax)


                                Please note that, all of the aforementioned fields may not have the same wording as given, rather you should extract the relevant data according to meaning and context.

                                Finally I want the response to be in a JSON format and just that, nothing else, do not even add ```json or anything else like punctuations or any other thing, this is of the utmost importance when it comes to the response. The JSON response needs to have the following structure:
                                {
                                    "name": '<value>',
                                    "street_address": '<value>',
                                    "city": '<value>',
                                    "state": '<value>',
                                    "zipcode": '<value>',
                                    "phone_number": '<value>',
                                    "email_address": '<value>',
                                    "amount_owed": '<value>', (Please do not add currency symbol)
                                    "currency_symbol": '<value>',
                                    "tax_status":'<value>'

                                }

                                Replace the “<value>” with the appropriate data you extract from the image. The “...” in the JSON structure denotes that there could be multiple entries.
                                '''
            }
        ]
    }
]



customer = [
    {
        "role": "system",
        "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
    },
    {
        "role": "user",
        "content": [{
                        "type": "text", 
                        "text": '''
                               Please help me extract the textual pieces of information from the image provided. Your job is to extract all of the aforementioned from the image.The desired output I want to receive is in JSON format and just this nothing else. If you are unable to find any of the details in the image please add ‘N/A’ in the json with the respective key. Please observe the image carefully and extract the words as they are in the image, regardless whether they make sense or not.

                                I am a professional Mobile application developer in Flutter. 
                                I am making an application for my client. The app is an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image. This data will be used to fill in the input fields.

                                This app is intended for businesses that wish to maintain and store their records efficiently, enabling them to store data simply by capturing a photo of their documents.

                                The data that I want you extract from the image are the following:
                                1. Name
                                2. Street Address
                                3. City
                                4. Sate
                                5. Zipcode
                                6. Phone Number
                                7. Email Address
                                8. Credit Terms
                                9. Currency Symbol (this could be any currency symbol that exists and what you find)
                                10. Tax Status (this is a boolean, such that it is true if there is tax and false if there is no tax)



                                Please note that, all of the aforementioned fields may not have the same wording as given, rather you should extract the relevant data according to meaning and context.

                                Finally I want the response to be in a JSON format and just that, nothing else, do not even add ```json or anything else like punctuations or any other thing, this is of the utmost importance when it comes to the response. The JSON response needs to have the following structure:
                                {
                                    'name': '<value>',
                                    'street_address': '<value>',
                                    'city': '<value>',
                                    'state': '<value>',
                                    'zipcode': '<value>',
                                    'phone_number': '<value>',
                                    'email_address': '<value>',
                                    'credit_terms': '<value>'
                                    'currency_symbol': '<value>'
                                    'tax_status':'<value>'

                                }

                                Replace the “<value>” with the appropriate data you extract from the image. The “...” in the JSON structure denotes that there could be multiple entries.
                                '''
            }
        ]
    }
]



customer_details = [
    {
        "role": "system",
        "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
    },
    {
        "role": "user",
        "content": [{
                        "type": "text", 
                        "text": '''
                                Please help me extract the textual pieces of information from the image provided. Your job is to extract all of the aforementioned from the image.The desired output I want to receive is in JSON format and just this nothing else. If you are unable to find any of the details in the image please add ‘N/A’ in the json with the respective key. Please observe the image carefully and extract the words as they are in the image, regardless whether they make sense or not.

                                I am a professional Mobile application developer in Flutter. 

                                I am making an application for my client. The app is an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image. This data will be used to fill in the input fields.

                                This app is intended for businesses that wish to maintain and store their records efficiently, enabling them to store data simply by capturing a photo of their documents.

                                The data that I want you extract from the image are the following:
                                1. Name
                                2. Amount Owed
                                3. Credit Terms (this could be 30, 60 or 90. Note if there as another number besides the ones mentioned before igore it and put N/A in json response)
                                4. Currency Symbol (this could be any currency symbol that exists and what you find)
                                5. Tax Status (this is a boolean, such that it is true if there is tax and false if there is no tax)


                                Please note that, all of the aforementioned fields may not have the same wording as given, rather you should extract the relevant data according to meaning and context.

                                Finally I want the response to be in a JSON format and just that, nothing else, do not even add ```json or anything else like punctuations or any other thing, this is of the utmost importance when it comes to the response. The JSON response needs to have the following structure:
                                {
                                    [
                                        {
                                            "name": "<value>",
                                            "amount_owed": "<value>", (Please do not add currency symbol)
                                            "credit_terms": "<value>"
                                        }
                                        ...
                                    ],
                                    "currency_symbol": "<value>"
                                    "tax_status":"<value>"

                                }

                                Replace the “<value>” with the appropriate data you extract from the image. The “...” in the JSON structure denotes that there could be multiple entries.
                                '''
            }
        ]
    }
]
