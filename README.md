
# Python-API-Cache-Demo

Example of using Redis to do caching with FastAPI and PostgreSQL database.


## Tech Stack

**Server:** Python, FastAPI 

**DATABASE:** PostgreSQL, Redis 


## API Reference

#### Get member all

```http
  GET /member
```

#### Get member all with caching

```http
  GET /member/cache
```

#### Create member

```http
  POST /member
```

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | **Required** |
| `firstname`      | `string` | **Required** |
| `lastname`      | `string` | **Required** |

#### Delete member by ID

```http
  DELETE /member/{id}
```
## Installation

Install Library

```bash
  pip install -r requirements.txt
```
    
