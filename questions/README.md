To use this the data submitted needs to be in JSON for testing purposes use POSTMAN, raw coding, with JSON/Application Type.

Web Application URL is /questions/addlocation


Android Application URL is /questions/questionsbyuser
#note this is not filtered




Below is example JSON. 


{
	"loc_barcode_num": 56,
		"items":
			[
			{
				"barcode_num":20, "item_type":"A", "user_assigned": "nick", "admin":"ally",
				"questions":
					[
					"Is the fireeqtinguisher pin in place?", "is equipment red?"		
					]
			}
	],
		"loc_questions": ["Is the location clean?", "Is there two pieces of Equipment?"]
}





