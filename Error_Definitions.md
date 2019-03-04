# Errors Returned

All errors from the wrappers will be returned as a josn formated string

## Error Codes

All errors will return additional information in the details when available

| Code | Description |
|:----:| ----------- |
| 0    | Required information missing |
| 1    | Connection error sending API request |
| 2    | Connection timed out sending request |
| 3    | An HTTP error was returnd by the reqest |
| 4    | A I/O Error occured, see spesific description for more details |
| 99   | Unknown error, These shouldn't be possible. |
