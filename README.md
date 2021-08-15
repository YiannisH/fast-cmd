# yhadji-com

## Run with
**`uvicorn main:app --reload`**

## Notes
Following the tutorial from here https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-same-router-multiple-times-with-different-prefix

## Build and run 
```
export dt=`date +"%d-%m-%Y-%s"`
docker build -t yhadji/fastapi:${dt} .
docker push yhadji/fastapi:${dt}
docker run --network=host -p 18000:8000 --rm -d yhadji/fastapi:v1
docker run --rm -d -p 8000:8000 yhadji/fastapi:v1
```