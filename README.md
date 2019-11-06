SQL test
===

### Usage

- Run up Postgresql server

```bash
$ docker-compose up db
```

- Stop Postgresql server

```bash
$ docker-compose down
```

- Connect to test database on Postgresql server using psql

```bash
$ docker-compose exec db psql -U postgres test
```

- Execute SQL file

```bash
$ docker-compose exec db psql -v ON_ERROR_STOP=1 -U postgres test -a -f "sql/schema.sql"
```
