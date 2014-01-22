# A Flask JSON API Example

A simple symmetrical API using Flask-Restful which forces the client to send JSON using the correct headers.

## Endpoints

**GET** */api/user/0* - Get the user with ID 0

Example response:

```
Status: 200

Data: {
    'name' : 'Joe',
    'email' : 'jturner@thinkful.com',
    'roles' : ['admin']
}
```

**PUT** */api/user/0* - Add or alter a user with ID 0

Example request:

```
Data: {
    'name' : 'Joe',
    'email' : 'jturner@thinkful.com',
    'roles' : ['admin']
}
```

Example response:

```
Status: 201 Created

Data: {
    'name' : 'Joe',
    'email' : 'jturner@thinkful.com',
    'roles' : ['admin']
}
```

## Some interesting things to note

- The use of location=get_json in the parser arguments
- The decorators ensuring that the Content-Type and Accept headers are both set to deal with JSON
- The way we handle validation errors.  This could potentially be cleaned up by using some form of schema validation.
- The use of Accept headers in our tests
