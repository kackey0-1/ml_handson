# [Understanding Software Architecture Spec] Layered Architecture

## Layered Architecture Topology

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2022-05-31T07:45:11.712Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36\&quot; etag=\&quot;0_VRANSJ-GI5pfWUn3zg\&quot; version=\&quot;18.1.1\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;m9_Bpx2jhqHkKHG2KxBJ\&quot; name=\&quot;Page-1\&quot;&gt;7Zndb5swEMD/mkjbwyYDgcLjmvRjajdV66Stjy444M7YyJgm7K+fHcyn0y6tmkKlvjS5s8/1/XzcHc7MWaSbMw6z5BuLEJnZINrMnOXMti3LA/JDacpK43lBpYg5jvSkVnGN/yKt1HZxgSOU9yYKxojAWV8ZMkpRKHo6yDlb96etGOn/1wzGyFBch5CY2l84Ekml9e2jVn+OcJyIxmHtXwrrydqTPIERW3dUzsnMWXDGRPUt3SwQUfBqLpXd6QOjzcY4omIfg7vzs9L9Xob++gL++FrAU0q8Txbwq3XuISm0y3q7oqwZcFbQCKllrJlzvE6wQNcZDNXoWp661CUiJXpYL4e4QJsHd2o1/svAQSxFgpdySm0A3MpEx4ylxXV7AG6gqSYd+HathPrQ42bplov8otE8AVNgQkGRjBMtMi4SFjMKyUmrPW6xASm1cy4ZyzSsOyREqYMeFoL1UaINFr+V+WdXSzedkeVGr7wVylqg0t+OkRJvumOt2Vaq7Sr/lFOPH5pkwAoeokdg+fVzCnmMxGMTg91hwBGBAt/3d/LiZ1pvc7/IB68T+XWy0JHvAyPym4zajfzG7uUpzQ1KVxzl0h95RIzKkUtYIj5+zpj3yQVmzmggdck5BwPnGeCOixxTlOeThWbZo1M7MsMN8RznAlHJYbLg3NHBBdPPZvZ8z3Q2P1gdBwalJRTwFubTjS17PnZsBY4B5b37eRCWLpj/7X4Cf3cYvE73E5h1ffR84djDcrRnvvAPFvlvoIg7w1rk7KD2uvnibRRxA5w3OrgnvYyP81BOoIibrc7kivgwtsYv4hZ4v8PYv4pbAOxbxudjlvFmn1NOGaNnDAuYdz2TvMUYpo0JZA1nevHlPveWzDscpjdyTeYOex4wds/TXPZPucc2sI3eY1vAfDWZYpNtkBu9ybaA+Xoyuf7RwBaMj81suy8wjdRDylbyz1VS5jiEciEPpooIvc3Vx0+WMcJi5dyHJcoIK1MJ4aOBWMISfY654OwPWkhrLjWUUdWRrjAhAxUkOKZSJGilVlDg1Ua+aHWKo2jbzO46tn7teoGTG156OpZ5cvauXy+fcXJSbH8/3o51foV3Tv4B&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>

- Presentation Layer 
  - Presentation Layer is responsible for User Interface(UI) and Backend Interface
- Business Layer
  - Business Logic Layer for each requests like fetch data from persistence layer
- Persistence Layer
  - Fetch/Create/Update data from database layer
- Database Layer

## Specification

The most important part of Layered Architecture is **Separation of Domains**.
This architecture helps you to build effective role and responsibility models.

- Layer Separation
    - Closed Layer
        - When a request moves from top to bottom in a layer, it must go through the layer directly below without skipping any of the layers 
        - Closed layers facilitate separation of layers and help isolate changes within the architecture 
    - Open Layer
        - opposite of Closed Layer

## Why we choose Layered Architecture

- Suitable for Small and Simple application
  - Layered Architecture is really easy to understand and start

## Architecture Evaluation
| Architecture Spec | Score |
|-------------------|-------|
| Separate Type     | Tech  |
| Quantum Number    | 1     |
| Deployment Ease   | 1     |
| Elasticity        | 1     |
| Evolvability      | 1     |
| Resiliency        | 1     |
| Modularity        | 1     |
| Overall Cost      | 5     |
| Performance       | 2     |
| Reliability       | 3     |
| Scalability       | 1     |
| Simplicity        | 5     |
| Testability       | 2     |
