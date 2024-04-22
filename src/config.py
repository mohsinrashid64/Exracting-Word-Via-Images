product_list =  [
    {
        "role": "system",
        "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
    },
    {
        "role": "user",
        "content": [{
                        "type": "text", 
                        "text": '''
                                What:
                                Please help me Extract the textual pieces of information from the image provided.
                                Who:
                                I am a professional Mobile application developer in flutter. Please answer my queries as an experienced mobile developer and as a web scraper and someone who is an expert in image processing and generative AI.

                                Why:
                                This question originates from a company that makes mobile applications and they are making an ecommerce app and they are intending  to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image. The image could be a screenshot of doc or pdf, in short it contains text. The image could also contain handwritten text.

                                Which:
                                The data you are supposed to extract from the image is “Balance Date”, “Cash”, “Bank”, “Product List”(this could be more than one and have the following attributes): “Product Name”, Unit(this is the weight and could be either in kilograms or pounds, also convert them to the approperiate abbreviation), “Quantity”, “Delivery Charges” and “Cost”. The wording of the aforementioned fields may differ so extract according to the meaning.Please ignore anything else. If you are unable to find any field for those put “N/A”. Furthermore the this is the format you are supposed to return the content:
                                {
                                    "last_balance_sheet_date" : "<RELEVANT_DATA>",
                                    "cash_on_hand":"<RELEVANT_DATA>",
                                    "bank_name":"<RELEVANT_DATA>",
                                    "bank_balance":"<RELEVANT_DATA>",
                                    "list_of_products":[
                                        {        
                                            "product_name":"<RELEVANT_DATA>",
                                            "unit": "<RELEVANT_DATA>",
                                            "product_cost":"<RELEVANT_DATA>",
                                            "quantity":"<RELEVANT_DATA>",
                                            "delivery_charges":"<RELEVANT_DATA>"
                                        }
                                    ]
                                }



                                How:
                                Finally return the data as a JSON response and only a json response nothing else this is of the utmost importance.

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
                               What: 
                                Please help me extract the textual pieces of information from the image provided. The image you will receive is that of and invoice, it can and will have the following as its content:
                                Title of Invoice (this could be ‘Cash Sale’, ‘Product Purchase’ or ‘Invoice’)
                                Date (Convert it to “DD/MM/YYYY” format) 	
                                Reference Number (Ref No)	
                                Customer Details (this will contain the following details. I.e, name, address, phone number, email, credit terms)
                                Business Details (this will contain the following details. I.e, name, address, phone number, email)
                                Data in tabular format which will have the following:
                                Item
                                Price(USD)
                                Quantity or Qty
                                Add Tax
                                Total (USD)

                                Your job is to extract all of the aforementioned from the image.The desired output I want to receive is in JSON format and just this nothing else. If you are unable to find any of the aforementioned details in the image please add ‘N/A’ in the json with the respective key.

                                Who:
                                I am a professional Mobile application developer in Flutter.

                                Why:
                                This question originates from a company that makes mobile applications. They are making an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image.
                                Which:
                                You have to extract everything specified as before.As for the tabular part please observe the column names of the table as they are supposed to be key names in the JSON also populate each key with data provided with respect to each column.The data you are supposed to extract from the image is 'Item', 'Price(USD), 'Quantity', 'Add Tax', 'Total (USD)', Further more in the table there is also a part which contains sections named ‘Sub Total’, ‘Tax’, ‘Total’, please also retrieve these. Please note that the wording of the column names may differ, please  extract them according to the context.Following is the template on how you should create the JSON:
                                {
                                "title_of_invoice": "<value>",
                                "date": "<value>",
                                "ref_no": "<value>",
                                "customer_details": {
                                    "name": "<value>",
                                    "address": "<value>",
                                    "phone_number": "<value>",
                                    "email": "<value>",
                                    "credit_terms": "<value>"
                                },
                                "business_details": {
                                    "name": "<value>",
                                    "address": "<value>",
                                    "phone_number": "<value>",
                                    "email": "<value>"
                                },
                                "item_list": [
                                    {
                                    "item": "<value>",
                                    "price_usd": "<value>",
                                    "quantity": "<value>",
                                    "add_tax": "<value>",
                                    "total_usd": "<value>"
                                    }
                                ],
                                "total_prices": {
                                    "sub_total": "<value>",
                                    "tax": "<value>",
                                    "total": "<value>"
                                }
                                }
                                How: 
                                Finally, return the data as a JSON response and only JSON and nothing else.
                                '''
                    }
        ]
    }
]