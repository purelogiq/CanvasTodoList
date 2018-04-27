FROM python:3.6

# Create user, mapped to local user
ARG userid
RUN mkdir /app
RUN useradd --user-group --home-dir /app --uid $userid python
RUN chown python:python /app
USER python

WORKDIR /app
