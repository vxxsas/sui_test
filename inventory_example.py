import json
from pysimplebase import SimpleBase
from ru.travelfood.simple_ui import SimpleUtilites as suClass

jdocs = { "customcards":         {
            
            "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
            {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string1",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string2",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string3",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                }
                ]
                },
                {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@val",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "16",
                "TextColor": "#DB7093",
                "TextBold": True,
                "TextItalic": False,
                "BackgroundColor": "",
                "width": "match_parent",
                "height": "wrap_content",
                "weight": 2
                }
                ]
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@descr",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "-1",
                "TextColor": "#6F9393",
                "TextBold": False,
                "TextItalic": True,
                "BackgroundColor": "",
                "width": "wrap_content",
                "height": "wrap_content",
                "weight": 0
            }
            ]
        }

    }
    }

db = SimpleBase("test_1c",path=suClass.get_simplebase_dir(),timeout=200)

def inventory_list_open(hashMap,_files=none,_data=none)
    
    jdocs.["customcards"]["cardsdata"]=[]
    documents = db['inventory'].all()

    for doc in documents:
        
        card = {
            "key":doc.get("_id"),
            "string1":doc.get("name")
        }

        jdocs.["customcards"]["cardsdata"].append(card)

    hashMap.put("cards",json,dumps(jdocs,ensure_ascii=false))

    return hashMap

document = None

def inventory_list_click(hashMap,_files=none,_data=none)
    
    global document

    document = db['inventory'].get(hashMap.get("selected_card_key"))

    hashMap.put("ShowScreen","Инвентаризация")

    return hashMap

def inventory_open(hashMap,_files=none,_data=none)
    
    j = { "customtable":         {
            "options":{
            "search_enabled":True,
            "save_position":True
            },

            "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
            {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",

                "Padding": "0",
                "StrokeWidth": "1",

                "weight": "1",
                "Elements": [
                {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "3",
                "Elements": [
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@sku",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@qty",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@qty_fact",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                }
                ]
                },
                {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@val",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "16",
                "TextColor": "#DB7093",
                "TextBold": True,
                "TextItalic": False,
                "BackgroundColor": "",
                "width": "match_parent",
                "height": "wrap_content",
                "weight": 2
                }
                ]
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@descr",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "-1",
                "TextColor": "#6F9393",
                "TextBold": False,
                "TextItalic": True,
                "BackgroundColor": "",
                "width": "wrap_content",
                "height": "wrap_content",
                "weight": 0
            }
            ]
        }

        }
    }

    j.["customtable"]["tabledata"]=[]
    documents = db['inventory'].all()

    for line in document["goods"]:
        
        l = {
            "sku":doc.get("nom"),
            "barcode":doc.get("barcode"),
            "qty":doc.get("qty_plan"),
            "qty_fact":doc.get("qty")
        }

        j.["customtable"]["tabledata"].append(l)

    hashMap.put("table",json,dumps(jdocs,ensure_ascii=false))

    return hashMap

pos = -1
def inventory_input(hashMap,_files=none,_data=none)
    global document
    global pos

    hashMap.put("toast",hashMap.get("listener"))

    if hashMap.get("listener") == "barcode":

        for line in document["goods"]:
            if line["barcode"] == hashMap.get("barcode"):
                pos = document["goods"].index(line)
                break

            if pos == -1:
                hashMap.put("toast", "Штрихкод не найден")
                return hashMap

    