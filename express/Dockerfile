FROM node:16.0
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential
COPY package.json .
RUN npm install
# Using a .dockerignore file, which will remove unwanted files!
COPY . .
EXPOSE 3000
CMD ["npm", "start"]