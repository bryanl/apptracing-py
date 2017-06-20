# Functions

## Scenario

Pass tracing information to a child function.

A starter project is in `exercise` with a solution in `solution`.

## Extra credit

* Add additional tags
* Add additional logs
* Add an error


```
docker run -it --network apptracingpy_velocity --rm -v $(pwd)/assets:/assets postgres:9.6 bash
```

```
createdb -h apptracingpy_db_1 -U postgres velocity2017
psql -h apptracingpy_db_1  -U postgres -f /assets/import_people.sql
```

