FROM node:8.10.0

RUN mkdir /app
COPY ./webpack.dev.js /app/webpack.dev.js
COPY ./tsconfig.json /app/tsconfig.json
COPY ./package.json /app/package.json
COPY ./package-lock.json /app/package-lock.json
COPY ./build /app/build
COPY ./src /app/src

WORKDIR /app
RUN npm install
