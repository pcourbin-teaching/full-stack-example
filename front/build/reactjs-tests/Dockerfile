FROM node:13-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN npx @api-platform/client-generator

COPY ./api-platform-generate_react.sh ./api-platform-generate_react.sh
RUN chmod +x ./api-platform-generate_react.sh

ENTRYPOINT ["./api-platform-generate_react.sh"]
