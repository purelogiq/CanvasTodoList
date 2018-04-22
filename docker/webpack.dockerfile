FROM node:8.10.0

# Create user, mapped to local user
RUN userdel node
ARG userid
RUN useradd -m -r -u $userid webpack
USER webpack

COPY ./webpack.dev.js /home/webpack/webpack.dev.js
COPY ./tsconfig.json /home/webpack/tsconfig.json
COPY ./package.json /home/webpack/package.json
COPY ./package-lock.json /home/webpack/package-lock.json
COPY ./src /home/webpack/src

WORKDIR /home/webpack
RUN npm install
