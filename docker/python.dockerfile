FROM python:3.6

# Create user, mapped to local user
ARG userid
RUN useradd -m -r -u $userid python
USER python
