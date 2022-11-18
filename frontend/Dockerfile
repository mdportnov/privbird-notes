FROM node:19-alpine as builder

WORKDIR /app/

COPY . .

RUN npm install

FROM node:19-alpine

COPY --from=builder /app/ /app/

WORKDIR /app/

RUN npm run build::prod
