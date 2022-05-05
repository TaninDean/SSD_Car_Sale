# API DOCUMENT

## CarSale api

    CarSale api is a api that help you to create a process from website to your backend.
    This api can send a request to GET the list of car and can SEND that transaction to
    create a list of buyer.

## BASEURL

```
https://polls.com/
```

## Authentication

```
curl https://api.polls.com/charges \
  -u {password}:
```

## CONNECT TO ACCOUNT

```
curl https://api.polls.com/connect/{{CHARGE_ID}}/\
  -u {{SECRET_KEY}}: \
  -H "Stripe-Account: {{ACCOUNT_ID}}" \
```

<span style="color: green">Endpoint: the specific of api</span>

## STATUS CODE

|        Status Code        |                                                            Meaning                                                            |
| :-----------------------: | :---------------------------------------------------------------------------------------------------------------------------: |
|          200 OK           |                                                      Request successful.                                                      |
|      400 Bad Request      |                                                   Problem with the request.                                                   |
|     401 Unauthorized      |                                         Valid channel access token is not specified.                                          |
|       403 Forbidden       |        Not authorized to access the resource. Confirm that your account or plan is authorized to access the resource.         |
|          200 OK           |                                                      Request successful.                                                      |
|       404 Not Found       |                                              Unable to get profile information.                                               |
| 500 Internal Server Error |                            The server has encountered a situation it does not know how to handle.                             |
|    501 Not Implemented    |                            The request method is not supported by the server and cannot behandled.                            |
|      502 Bad Gateway      |                              This error response means that the server, got an invalid response.                              |
|  503 Service Unavailable  | The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. |

## Error responses

The error will response in body with error occurs.
| Massage | String: Conating infromation about error |
| Status Code | int: the status code of error request |
| details[].message | String: Details of the error |
| details[].property | String: Location of error |

```
{
   "message":"The request body has error",
   "details":[
      {
         "message":"May not be empty",
         "property":"messages[0].text"
      },
      {
         "message":"Somthing wrong",
         "property":"messages[1].type"
      }
   ]
}
```

## Error Massage

|         Error massage          |              meaning              |
| :----------------------------: | :-------------------------------: |
|  The request body has error.   |         body is not valid         |
| The request body is not found. |        body has not found         |
|    Failed to send messages.    | the server can't send the massage |

## HTTP request

### GET

get car by id

```
curl -v -X GET https://api.polls/get/{car_id}/ \
```

get car by name

```
curl -v -X GET https://api.polls/get/car/{name} \
```

get all list of car

```
curl -v -X GET https://api.polls/get/car/ \
```

### POST

buy car

```
curl -v -X POST https://api.polls/api/buy/ \
-H 'Content-Type: application/json' \
-d '{
    "car_id": "1",
    "Frist_name": jimmy
    "Last_name" : john
}'
```

create

```
curl -v -X POST https://api.polls/api/create/ \
-H 'Content-Type: application/json' \
-d '{
    "band": BENZ,
    "model": "C43"
    "price": 20000
}'
```

update trans

```
curl -v -X POST https://api.polls/api/update/ \
-H 'Content-Type: application/json' \
-d '{
    "car_id": 1
    "band": "BMW"
    "Model": "X1"
    "Price": 10000
}'
```
