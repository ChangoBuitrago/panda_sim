# Panda sim test
> Gridsingularity interview tasks

## Setup
1. Clone repo:
  `git clone https://github.com/ChangoBuitrago/panda_sim.git`
2. Change folder:
  `cd panda_sim`
3. Build docker image:
  `docker-compose build`
4. Launch service:
  `docker-compose up -d`

## Endpoints

#### POST request that launches the simulation using the aforementioned Python module. The response should include the active and reactive power of the load in JSON format

- [http://localhost:8000/tasks/init-sim](http://localhost:8000/tasks/init-sim)

#### GET request that reads the active power of the previously executed simulation

- [http://localhost:8000/reads/active-power](http://localhost:8000/reads/active-power)

#### GET request that reads the reactive power of the previously executed simulation

- [http://localhost:8000/reads/reactive-power](http://localhost:8000/reads/reactive-power)


## Removal
1. Stops and removes docker image:
  `docker-compose down -v`

## Docker-compose debug
1. Tale logs:
  `docker-compose logs -f`