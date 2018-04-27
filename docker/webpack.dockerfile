FROM node:8.10.0

# Create user, mapped to local user
ARG userid
RUN mkdir /app
RUN userdel node
RUN useradd --user-group --home-dir /app --uid $userid webpack
RUN chown webpack:webpack /app
USER webpack

COPY ./webpack.dev.js /app/webpack.dev.js
COPY ./tsconfig.json /app/tsconfig.json
COPY ./package.json /app/package.json
COPY ./package-lock.json /app/package-lock.json
COPY ./src /app/src

WORKDIR /app
RUN npm install
