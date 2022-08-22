FROM node:lts-alpine

WORKDIR /app

COPY package*.json ./

RUN yarn global add http-server

COPY . .

RUN yarn
RUN yarn build

EXPOSE 5173

CMD [ "http-server", "dist"]