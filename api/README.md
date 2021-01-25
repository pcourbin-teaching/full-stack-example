# Generation of the API server with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator)

## Main structure generation
From the API description file [openapi-spot.yaml](openapi-spot.yaml) containing in particular:
- Details of data formats
- Details of possible returns
- Details of API entry points

it is possible to generate a complete API structure using the different languages / frameworks available for the servers.
For this you can use the script [openapi_codegen.sh](openapi_codegen.sh) by modifying the parameters as needed.

| Name | Default | Possibles values | Description |
| --- | --- | --- |--- |
| `openapi_file` | `openapi-spot.yaml`| * | Name of YAML file to use for generation. |
| `out_framework` | `python-flask`| See [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) | Name of the language / framework desired as output of the generation. |
| `package_name` | `SPOTAPI`| * | Name of the project that will be used for the generation. |

Then run:
```console
./openapi_codegen.sh
```

## Add your logic, the connection to the Database, etc.
For the following, we consider the generated folder [SPOTAPI](SPOTAPI/) from the description file [openapi-spot.yaml](openapi-spot.yaml).

### Main controllers
In this file we have defined 4 tags to merge different entry points, each one generated a file in the folder [SPOTAPI/controllers](SPOTAPI/controllers/)
| Tag | File |
| --- | --- |
| `Quote` | [SPOTAPI/controllers/quote_controller.py](SPOTAPI/controllers/quote_controller.py) |
| `Reference` | [SPOTAPI/controllers/reference_controller.py](SPOTAPI/controllers/reference_controller.py) |
| `Theme` | [SPOTAPI/controllers/theme_controller.py](SPOTAPI/controllers/theme_controller.py) |
| `Protagonist` | [SPOTAPI/controllers/protagonist_controller.py](SPOTAPI/controllers/protagonist_controller.py) |

For example, in [SPOTAPI/controllers/quote_controller.py](SPOTAPI/controllers/quote_controller.py), we have function `quote_get` which is called when entrypoint `/quote` is called with a `get` method.
At the beginning, the function is empty and simply returns `'do some magic!'`

```python
def quote_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Quote objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'
```

You can now modify these files to add your logic and in particular the connection to your database.
To keep things separate, in this example you will find a [SPOTAPI/controllers/database_controller.py](SPOTAPI/controllers/database_controller.py) file **which is not generated** but contains all the logic and the connection to the database.

Going back to the previous example, we just have to add the import to our file `from SPOTAPI.controllers.database_controller import Database` and then modify the return of the function `quote_get`:

```python
from SPOTAPI.controllers.database_controller import Database

def quote_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Quote objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return Database.getListWithDetailsFromOtherClassParameters(Quote)
```

### Security controller
A specific file [SPOTAPI/controllers/security_controller_.py](SPOTAPI/controllers/security_controller_.py) is generated linked with the `securitySchemes` defined in our [openapi-spot.yaml](openapi-spot.yaml) file.

```
  ####################
  # Security
  ####################
  securitySchemes:
    ApiKeyAuth:        # arbitrary name for the security scheme
      type: apiKey
      in: header       # can be "header", "query" or "cookie"
      name: API-KEY  # name of the header, query parameter or cookie
```

For this example, we decided to use a simple API key, but [many other choices are possible](https://swagger.io/docs/specification/authentication/).

The [SPOTAPI/controllers/security_controller_.py](SPOTAPI/controllers/security_controller_.py) file contains one function `info_from_ApiKeyAuth` which will be called each time **before** the desired entry point. It has to check if the user has the right to access this API.

The key passed by the user is available in the `api_key` variable, you can for example check your database to which user it corresponds. For the example, we are simply using a local dictionary.

### Add your requirements
You have to edit the file [SPOTAPI/requirements.txt](SPOTAPI/requirements.txt) with your needed packages.
For example, we added `mysql-connector-python` used in [SPOTAPI/controllers/database_controller.py](SPOTAPI/controllers/database_controller.py)

### Regenerate without losing all your work
Each time you run the OpenAPI generator ([openapi_codegen.sh](openapi_codegen.sh)), all files will be regenerated.
If you just add an entry point on a specific tag, you can ask the generator to ignore others files.
For that you can edit file [SPOTAPI/.openapi-generator-ignore](SPOTAPI/.openapi-generator-ignore).

For example, do not forget to add `requirements.txt` if you do not want to re-add your requirements.txt each time you regenerate your API.


# Run a Docker with your API
Your API is ready, you want to test it using Docker.
**Here we consider you already follow the steps to deploy the database**. 

We have defined a [docker-compose.yml](docker-compose.yml) file to generate the container using [SPOTAPI/Dockerfile](SPOTAPI/Dockerfile). 
Note that:
- We edited the generated file [SPOTAPI/__main__.py](SPOTAPI/__main__.py) to be able to use an environment variable to change the `PORT` used by the application. We also add [CORS](https://swagger.io/docs/open-source-tools/swagger-ui/usage/cors/) to be able to use the API with our front. 
- We use environment variable in [SPOTAPI/controllers/database_controller.py](SPOTAPI/controllers/database_controller.py) to be able to change the database link.

```
version: '3'
services:
  api:
    image: pcourbin/spot_api:0.1.0
    build: ./SPOTAPI
    environment:
        DATABASE_URL: "mysql://user:password@db:3306/spot"
        PORT: "3000"
    ports:
      - 3000:3000
    networks:
      - spot-network
    restart: always

networks:
  spot-network:
    external: true
```

Then, you can:

| Command | Function |
| --- | --- |
| `docker-compose build` | (re)build the docker image using current files |
| `docker-compose up -d --force-recreate` | (re)create the container using the current docker image |
| `docker-compose logs -f api` | continuously display the logs of the container |

Finally, go to [http://localhost:4000/ui](http://localhost:3000/ui) to test your API.
Do not forget to use `API_KEY` defined in [SPOTAPI/controllers/security_controller_.py](SPOTAPI/controllers/security_controller_.py)

## Note
Each time you changed your code, you can simply use the script [gen_run_docker.sh](gen_run_docker.sh) which will recreate the docker image, then the container and finally display the logs of the container.

You can also use the [docker-compose-dev.yml](docker-compose-dev.yml) during development. It will mount the folder `SPOTAPI` instead of using the code copied in the container, so each time you change your code, you API will be restarted with the changes. 