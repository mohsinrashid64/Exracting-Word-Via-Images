PROMPT =  [
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
