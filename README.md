## Description

AWS serverless project for notifying by email about the survey results.


### Quick Start
Run locally using:  
```bash
chalice local
```

### Deployment
Deploy  using:  
```bash
chalice deploy
chalice deploy --state prod
```

#### Environment variables
```text
SMTP_USERNAME= <Data provided by Amazon Simple Email Service> 
SMTP_PASSWORD= <Data provided by Amazon Simple Email Service>
ORIGIN_EMAIL= <Verified email in SES>
DESTINATION_EMAIL= <Verified email in SES>
```

#### Routes and methods
| Method | URI Path        | Description                           |
|---     |---              |---                                    |
| GET    | /               | Gets the service data                 |
| POST   | /notify         | Sends an email with survey data       |
| POST   | /test           | Sends a test email                    |

#### Notify POST body
```json5
{
   "step":21,
   "profile":{
      "survey_date":"1995-02-08",
      "location":"Guatemala",
      "age":"25",
      "gender":"man",
      "sex":"male",
      "orientation":"bisexual",
      "indigenous":false,
      "disability":false
   },
   "results":{
      "q_01":5,
      "q_02":4,
      "q_03":3,
      "q_04":2,
      "q_05":1,
      "q_06":5,
      "q_07":4,
      "q_08":3
   },
   "feedback":{
      "services_given":[
         {
            "label":"LEGAL",
            "active":true
         },
         {
            "label":"PSICOLÓGICO",
            "active":false
         },
         {
            "label":"ECONÓMICO",
            "active":true
         },
         {
            "label":"MÉDICO",
            "active":false
         },
         {
            "label":"ALBERGUE",
            "active":true
         }
      ],
      "needs_met":{
         "on":"Si",
         "off":"No",
         "active":true
      },
      "needs_feedback":"",
      "referred_to_partner":{
         "on":"Si",
         "off":"No",
         "active":true
      },
      "partner_service":3,
      "had_problems":{
         "on":"Si",
         "off":"No",
         "active": true
      },
      "problems_encountered":"asdfsa ",
      "seen_on":[
         {
            "label":"INTERNET",
            "active":true
         },
         {
            "label":"REDES SOCIALES",
            "active":true
         },
         {
            "label":"FERIAS O KIOSKOS",
            "active":false
         },
         {
            "label":"FOLLETOS",
            "active":false
         },
         {
            "label":"REFERIDO",
            "active":false
         }
      ],
      "additional_channels":"",
      "global_valuation":"very_bad",
      "is_confidential":{
         "on":"Si",
         "off":"No",
         "active":true
      },
      "confidential_feedback":"as 2 1 4fsa ",
      "suggestions":"mzxncmvnzmxn mcx"
   },
   "contact":{
      "anonymity":"false",
      "first_name":"aldo",
      "last_name":"gatica",
      "email":"aldogatica123@gmail.com",
      "phone_number":"31264249"
   }
}
```
#### Test POST body
```json5
{
    'payload': 'Test payload'
}
```