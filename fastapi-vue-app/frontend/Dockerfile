FROM node:20-alpine

WORKDIR /app

COPY . .
RUN rm -rf node_modules

RUN npm install --force


EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host"]