FROM node:16.0
WORKDIR /my-react-app
COPY package.json yarn.lock ./
RUN yarn
COPY ./public ./public
COPY ./src ./src
RUN yarn build

FROM nginx:1.19.10-alpine
COPY --from=0 /my-react-app/build /usr/share/nginx/app
RUN chmod -R 655 /usr/share/nginx/app
COPY ./conf.d /etc/nginx/conf.d
