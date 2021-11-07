The first time I heard about [Backstage](https://backstage.io), I reacted with a resounding "huh, that's neat I guess."
However, over the past few weeks it's come up in conversation with engineers whose opinions I respect,
and so I thought it might be time to investigate it properly.
After watching some of the demos, I had an "a-ha" moment, and at this point I'm pretty excited about Backstage and the idea of developer portals cutting down on the number of touch points an engineer needs to interact with to get things done.

I've tried to describe Backstage to people before, and the response is usually something along the lines of "so... like a wiki?"
While Backstage does share some characteristics with a wiki, saying that it's "like a wiki" doesn't really do the idea justice. 
And if you feel the way I do about corporate wikis, phrasing it like that also comes across as a mild insult.
In essence, Backstage tries to solve the problem of discoverability for developer resources.
Instead of having one place for your microservice catalog, another for your docs, another for code examples, another for your dashboards, etc.
Backstage collects all of those (and more) into a single UI.
Backstage has a plugin architecture, which means that the UI for different resources (components in Backstage lingo) can be owned by separate teams;
If I'm on a team that owns observability tooling, I can write a plugin to surface that information in Backstage instead of waiting on another team to do it for me.

While exciting, Backstage is still very new technology, so the docs aren't quite stable yet for onboarding new users.
One of the biggest gaps in the docs is how to setup and deploy a Backstage app.
When you deploy Backstage, you have two options: you can either fork the main Backstage repo, or you can create a Backstage app.
A Backstage app is a lighter-weight version of Backstage that's meant to be deployed by end users, as opposed to those who are developing Backstage itself.
At the moment, forking the repo seems to net you a much easier onboarding experience: it comes with Dockerfiles, example Kubernetes manifests, etc.
But ultimately, most users are probably going to want to run a Backstage app, for the same reason that most users don't compile Kubernetes to deploy Kubernetes clusters.
Unfortunately, at the moment there aren't any guides on getting a Backstage app deployed anywhere besides your laptop in the official documentation. 
So, in the spirit of too much free time on a Saturday, I decided to try to deploy a Backstage app to Kubernetes, 
and to write about the experience in order to give others a head start.

# A caveat

This post marks a very specific point in time of a nascent technology.
Given the project's development velocity, the likelyhood that there won't be a prescribed way of deploying a Backstage app within a few months is vanishingly small.
More likely than not, the end user docs are going to recommend something different than what's in this post.
If you're reading this a year from now, first, congrats on making it out of 2020, and second, _go with what the docs say_.
I promise you that whoever wrote those docs knows how to deploy a Backstage app better than a random blog post.

# What's not included

The Backstage app in this post is by no means meant for production use.
Among other things, I've not made any attempt to secure the app, and the database runs on Kubernetes, which is what you do to databases when you hate the data they contain.
A production deployment would also require a stable URL and SSL certificate, which I didn't attempt to set up for this post.

# Requirements

In order to follow along with this post, you'll need these tools installed:

* [npm](https://www.npmjs.com/)
* [python](https://www.python.org/)
* [yarn](https://yarnpkg.com/)
* [docker](https://www.docker.com/)
* [kind](https://kind.sigs.k8s.io/)

# Create the Backstage app

The first task is to create a new Backstage app.
You can do this using the `npx` script from the Backstage package:

```sh
npx @backstage/create-app
```

A prompt will first ask you to pick a name for the app, and then a database to use.
I was feeling inspired, so I went with "example-app" for the name.
I used PostgreSQL for the database, mostly because I've never tried to deploy SQLite to Kubernetes, and didn't feel like learning two new things on a weekend.

# Set up Postgres locally

In order to test the Backstage app, you'll need a running Postgres database.
Installing Postgres on your laptop is a completely fine option, but for development I like running databases in containers:

```sh
docker run -d -e POSTGRES_HOST_AUTH_METHOD=trust --net=host postgres
```

The `--net=host` flag uses the host process' networking namespace instead of creating a new one, so I don't have to worry about binding ports.
Note that I'm using Fedora, and networking might work different on, say, Docker for Mac.
An alternate option would be to use `-p 5432:5432` to bind port 5432 from the container to your machine.
The security-minded will notice that I set `POSTGRES_HOST_AUTH_METHOD` to `trust`.
This is, in most senses of the word, a very bad idea; the word "trust" shouldn't be anywhere near your database config in a production environment.
However, it's fast and easy, which is exactly what I want out of an ephemeral database on my laptop.

# Testing the Backstage installation

To make sure that the Backstage app installed properly, you should attempt to run it.
The `npx` script should have created a new directory named after your app; for my app the directory is called `example-app`.
This directory should contain a `packages` directory, which has an `app` and `backend` directory.
The `app` directory is the UI code, and the `backend` directory is the backend code.
Switch to the newly-created `example-app` directory, and start the backend server:

```sh
# The backend app logs are pretty verbose, so we log them to a backend.log file instead of getting our terminal commands interrupted
THIS_IS_HILARIOUSLY_UNSAFE=1 POSTGRES_USER=postgres yarn workspace backend start > backend.log 2>&1 &
```

Then start the frontend app

```sh
yarn workspace app start
```

This should open a browser to `localhost:3000`, where you'll see the Backstage UI.

# Setup the app-backend plugin

By default, Backstage's frontend and backend are served separately.
This is a good choice if you're looking to be able to scale the two independently, but for simple deployments it's more complexity than one needs.
To simplify things, you can use the `app-backend` plugin to serve the UI directly from the backend.

## Installing the app-backend plugin

Start by installing the plugin:

```sh
yarn workspace backend add @backstage/plugin-app-backend
```

And then add your frontend as a dependency to your backend

```sh
yarn workspace backend link app
```

You'll then need to build the app

```sh
yarn workspace app build
```

## Adding the plugin code to the backend

In order to use the plugin, you'll need to add a bit of extra code to packages/backend/src/index.ts

```typescript
// FIXME: this code was copied from the internet, double check it

// Put this with your imports
import { createRouter } from '@backstage/plugin-app-backend'

// ...there's a bunch of lines of code here..

async function main() {
    // put this with the other calls to useHotMemoize
    const appBackend = useHotMemoize(module, () => createEnv('appbackend'));

    // put this after the apiRouter configuration
    const staticRouter = await createRouter({logger: appBackend.logger, appPackageName: 'app'});

    // Add this line to the call to createServiceBuilder
    const service = createServiceBuilder(module)
      .loadConfig(configReader)
      .addRouter('/api', apiRouter)
      .addRouter('', staticRouter) // <- this one
}
```

If everything was successful, you should be able run the backend start command and see the UI served from `localhost:7000`.

# Create a kind cluster

Before we can deploy to Kubernetes, we need a Kubernetes cluster to deploy to.
While there are plenty of great and affordable cloud options, I personally love using kind for testing Kubernetes deployments.
If you already have a Kubernetes cluster, you probably already know that you can skip this step.
If you don't already have a cluster, create one on your laptop by installing kind and running:

```sh
kind create cluster
```

# Create a Backstage app container image

While the generated app contains a Dockerfile, it only containerizes the backend, and doesn't work with the app-backend plugin.
If you want to deploy them together, you'll need to add a new Dockerfile to the root of the app directory:

```dockerfile
# FIXME: this creates a gigantic Docker image
FROM node:12-buster

WORKDIR /usr/src/app

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --production

COPY . ./
RUN yarn workspace app link
RUN yarn workspace backend link app
RUN yarn workspace backend install

CMD ["node", "packages/backend"]
```

Note that this Dockerfile is _extremely_ unoptimized.
On my laptop it clocked in at around a 1.3G, which is... frankly terrible.
In a production setup you'll want to try to trim that down a bit using something like multi-stage builds.
You'll also want to write at least a minimal .dockerignore file:

```
node_modules/
Dockerfile
```

Now you can build the Docker image 

```sh
docker build . -t localhost/backstage-example:local
```

I avoid using the `latest` tag because it doesn't play well with side loading containers onto kind.
Instead, I use a tag that hopefully makes it _extremely_ clear that this is for use on my laptop.

Instead of pushing to a container registry, I side-loaded the container image onto my kind node:

```sh
kind load docker-image localhost/backstage-example:local
```

If this were a production deployment, you'd want to use a sensible tagging scheme, and push to a real container image registry.

# Deploying Backstage to Kube

Finally, we can deploy Backstage to Kubernetes.
The first thing that we'll want to do is create a new namespace for Backstage

```sh
kubectl create namespace backstage
```

And we'll also need a password for our Postgres:

```sh
# This is literally the only attempt at security in this post
export POSTGRES_PASSWORD=yourpasswordhere
```

From there, we can go ahead and deploy our database.
I used a pretty straightforward PG on Kube setup:

```sh
cat <<EOM | kubectl apply -f -
kind: PersistentVolume
apiVersion: v1
metadata:
  name: postgres-pv-volume
  namespace: backstage
  annotations:
    breaking.computer/copied-from-internet: "yes"
    breaking.computer/original-source: https://severalnines.com/database-blog/using-kubernetes-deploy-postgresql
  labels:
    type: local
    app: postgres
spec:
  storageClassName: manual
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteMany
  hostPath:
    path: "/mnt/data"
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: postgres-pv-claim
  namespace: backstage
  annotations:
    breaking.computer/copied-from-internet: "yes"
    breaking.computer/original-source: https://severalnines.com/database-blog/using-kubernetes-deploy-postgresql
  labels:
    app: postgres
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: postgres-config
  namespace: backstage
  annotations:
    breaking.computer/copied-from-internet: "yes"
    breaking.computer/original-source: https://severalnines.com/database-blog/using-kubernetes-deploy-postgresql
    breaking.computer/bad-idea: "yes use a secret instead"
  labels:
    app: postgres
data:
  POSTGRES_USER: postgres
  POSTGRES_PASSWORD: $POSTGRES_PASSWORD
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
  namespace: backstage
  annotations:
    breaking.computer/copied-from-internet: "yes"
    breaking.computer/original-source: https://severalnines.com/database-blog/using-kubernetes-deploy-postgresql
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:10.4
          imagePullPolicy: "IfNotPresent"
          ports:
            - containerPort: 5432
          envFrom:
            - configMapRef:
                name: postgres-config
          volumeMounts:
            - mountPath: /var/lib/postgresql/data
              name: postgredb
      volumes:
        - name: postgredb
          persistentVolumeClaim:
            claimName: postgres-pv-claim
---
apiVersion: v1
kind: Service
metadata:
  name: postgres
  namespace: backstage
  annotations:
    breaking.computer/copied-from-internet: "yes"
    breaking.computer/original-source: https://severalnines.com/database-blog/using-kubernetes-deploy-postgresql
  labels:
    app: postgres
spec:
  type: ClusterIP
  ports:
   - port: 5432
  selector:
   app: postgres

EOM
```

Note that if you write the manifest and apply it separately instead of using a heredoc, you'll want to find a way to interpolate the `$POSTGRES_PASSWORD` variable.

If any security-conscious engineers are still reading this, they'll notice that I put the Postgres password in a ConfigMap instead of a Secret.
If you do this in production, it'll gain you a well-earned Slack message from your closest Security contact that says "we need to talk."
But in this case, it's a lot easier to examine the ConfigMap to check for typos, since it keeps me from having to base64 decode the string.

After Postgres is deployed, we can deploy our Backstage image:

```sh
cat <<EOM | kubectl apply -f -
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backstage-backend
  namespace: backstage
  annotations:
    breaking.computer/copied-from-internet: "yes"
    breaking.computer/adapted-from: https://github.com/spotify/backstage/blob/master/contrib/kubernetes/plain_single_backend_deplyoment/deployment.yaml
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backstage
      component: backend
  template:
    metadata:
      labels:
        app: backstage
        component: backend
    spec:
      containers:
        - name: backend
          image: localhost/backstage-example:local
          env:
            # We set this to development to make the backend start with incomplete configuration. In a production
            # deployment you will want to make sure that you have a full configuration, and remove any plugins that
            # you are not using.
            - name: NODE_ENV
              value: development
            - name: APP_ENV
              value: development
            - name: POSTGRES_USER
              valueFrom:
                configMapKeyRef:
                  name: postgres-config
                  key: POSTGRES_USER
            - name: POSTGRES_PORT
              value: "5432"
            - name: POSTGRES_HOST
              value: postgres.backstage.svc
            - name: POSTGRES_PASSWORD
              valueFrom:
                configMapKeyRef:
                  name: postgres-config
                  key: POSTGRES_PASSWORD
          ports:
            - name: http
              containerPort: 7000
          resources:
            limits:
              cpu: 1
              memory: 0.5Gi
          readinessProbe:
            httpGet:
              port: 7000
              path: /healthcheck
          livenessProbe:
            httpGet:
              port: 7000
              path: /healthcheck
---
apiVersion: v1
kind: Service
metadata:
  name: backstage-backend
  namespace: backstage
  annotations:
    breaking.computer/copied-from-internet: "yes"
    breaking.computer/adapted-from: https://github.com/spotify/backstage/blob/master/contrib/kubernetes/plain_single_backend_deplyoment/deployment.yaml
spec:
  type: NodePort
  selector:
    app: backstage
    component: backend
  ports:
    - name: http
      port: 80
      targetPort: http
EOM
```

Now we should be able to run `kubectl port-forward svc backstage-backend 7000:80` and see Backstage in our browser at `localhost:7000`.

---

Again, this is not a production-grade deployment.
However, if you want to take this deployment and make it production grade, here are some gaps to fill in:

- You probably want to use a database outside of Kubernetes.
  Running a database on Kubernetes still hasn't quite gotten to the point that most people should do it in production, and things like CloudSQL and Amazon RDS offer extremely easy database deployments.
- You'll want to create a separate database user for Backstage.
  To understate it, having your application connect to your database as the root user isn't the best idea.
- You'll need a DNS entry and an SSL certificate.
  Backstage requires you to configure a `baseUrl`, which will need to be a real DNS entry with an SSL certificate in a production deployment.
- You'll probably want to trim down the Docker image.
  Because again, a 1.3 gig Docker image is going to cause headaches when your
  Kubernetes node is spending 5 minutes pulling the image and you're trying to
  autoscale a deployment.
- You'll want observability into the system, alerting, etc.
  Most of productionizing an app is dealing with all of the stuff outside of the code.
