### @todo
[x] Simple implementation of Kafka PubSub with python  
[x] Docker compose file  
[x] Add simple data set  
[...] Add logging  
[ ] Add tests  
[ ] Add multiprocessing


# local mock deployment 
Using docker desktop kubernetes cluster
```shell
kompose convert
mv *yaml k8s
kubectl config use-context docker-desktop
kubectl apply -f k8s/
```


Other commands  
```shell
kubectl config get-contexts
kubectl config use-context docker-desktop
kubectl cluster-info
```