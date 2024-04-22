product_list =  [
    {
        "role": "system",
        "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
    },
    {
        "role": "user",
        "content": [{
                        "type": "text", 
                        "text": "What: Please help me extract the textual pieces of information from the image provided.\n\nWho: I am a professional Mobile application developer in Flutter.\n\nWhy: This question originates from a company that makes mobile applications. They are making an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image.\n\nWhich: The data you are supposed to extract from the image is 'Balance Date'(Date should be in this format: 'DD/MM/YYYY'), 'Cash On Hand(this could have different name for instance 'Cash', 'Cash Available' or any other synanoms or phrases with the same meaning, Please do not confuse this with Bank Balance)', 'Bank Name',’Bank Balance’, 'Product List'(this could be more than one and have the following attributes, also correct the spelling mistake if you are familiar with the product otherwise do not do it): “Product Name”, “Quantity”, “Delivery Charges” and “Cost”. The wording of the aforementioned fields may differ so extract according to the meaning.Please ignore anything else. If you are unable to find any field for those put “N/A”. Furthermore the this is the format you are supposed to return the content:\n\n\n{\n\t\"last_balance_sheet_date\" : \"<RELEVANT_DATA>\",\n\t\"cash_on_hand\":\"<RELEVANT_DATA>\",\n\t\"bank_name\":\"<RELEVANT_DATA>\",\n\t\"bank_balance\":\"<RELEVANT_DATA>\",\n\t\"list_of_products\":[\n\t\t{\n\t\t\t\"product_name\":\"<RELEVANT_DATA>\",\n\t\t\t\"product_cost\":\"<RELEVANT_DATA>\",\n\t\t\t\"quantity\":\"<RELEVANT_DATA>\",\n\t\t\t\"delivery_charges\":\"<RELEVANT_DATA>\"\n\t\t}\n\t]\nHow: Finally, return the data as a JSON response and only JSON nothing else."
                    }
        ]
    }
]
