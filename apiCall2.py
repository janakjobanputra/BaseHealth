import httplib2, json
httpsObj = httplib2.Http()
headers = {	"user_key": "INSERT_API_KEY_HERE",			#<-- INSERT YOUR API KEY HERE
			"Content-Type": "application/json"	}
body = """{
    "gender": "female",
    "yearOfBirth": "1932",
    "ethnicity": "caucasian",
    "genotypes":
    {
        "rs4951039": "AA",
        "rs11118883": "AG",
        "rs10936599": "CC",
        "rs8752": "CT",
        "rs16892766":"AA",
        "rs6983267":"TG",
        "rs10795668":"TG"
    },
    "hasBeenDiagnosedWith":
    {
        "type2Diabetes": "yes"
    }
}"""
response, content = httpsObj.request(
	uri = "https://api.basehealth.com/Genophen/api/v1/assessment/diseases/type2Diabetes",
	method = 'POST',
	headers = headers,
	body = body
)
#print response
#print content
if response['status'] == "200":
	data = json.loads(content)
	print json.dumps(data, indent=4, separators=(',', ': '))
elif response['status'] == "400":
	print "Invalid Json document in POST body."
elif response['status'] == "403":
	print "Authentication parameters missing."
elif response['status'] == "405":
	print "Faulty request method, use POST."
else:
	print "Unknown Error."