GET options:

* by resource id: http://server:port/resource/id
```
requests.get('http://localhost:3000/analysis/1')
```

* apply sorting: http://server:port/resource?_sort=property
```
requests.get('http://localhost:3000/analysis?_sort=price')
```

* apply order (asc, desc): http://server:port/resource?_sort=property&_order=desc
```
requests.get('http://localhost:3000/analysis?_sort=price&_order=asc')
```
