# Stage 1: Build the React app
FROM node:18

WORKDIR /app

COPY . .

RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev", "--","--host"]