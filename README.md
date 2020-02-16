## Description

AWS serverless project for notifying by email about the survey results.


### Quick Start
Run locally using:  
```bash
chalice local
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
    
}
```
#### Test POST body
```json5
{
    'payload': 'Test payload'
}
```