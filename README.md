# Example of full-stack project using Database (MySQL) + API (OpenAPI) + Front (Angular)
(README in progress, for teaching purpose)

## Acknowledgements -- SPOT – La place du débat public
This project is based on previous work for the great project "**SPOT – La place du débat public**" led by **Samy Monnier**.
If you are interested to work on this project, do not hesitate to contact him and watch its [videos on Youtube](https://www.youtube.com/channel/UCjssrmULG31Pp6hzRpZgLXQ)

## Details of each part
- Database: See [data/README.md](data/README.md)
Using MySQL docker with script and CSV file to deploy a database with data.
- API: See [api/README.md](api/README.md)
Using OpenAPI generator to define and generate an API.
- Front: See [front/README.md](front/README.md)
Using Angular and OpenAPI to generate a front using the API.

## Quick test
**Create the docker network**:
```terminal
docker network create spot-network
```

**Build all** docker images (API and Front)
```terminal
docker-compose build
```

**Run all** containers
```terminal
docker-compose up -d
```

**Finally, test it**:

| Part | Access | Description |
| --- | --- | --- |
| **API** | [http://localhost:4000/ui](http://localhost:4000/ui) | Do not forget to use `API_KEY` defined in [SPOTAPI/controllers/security_controller_.py](api/SPOTAPI/SPOTAPI/controllers/security_controller_.py) |
| **Front** | [http://localhost:3000](http://localhost:3000)| Wait a bit during the first run, see docker logs if needed: lots of stuff needs to be compiled. |
| **Database** | [http://localhost:5000](http://localhost:5000) | phpmyadmin |