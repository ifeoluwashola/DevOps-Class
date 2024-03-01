<<<<<<< HEAD
FROM node:alpine

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .

EXPOSE 3000

=======
FROM node:20-alpine

# Setting the working directory in the container
WORKDIR /app

# Copying package.json and package-lock.json to the working directory
COPY package.json .
COPY package-lock.json .

# Installing dependencies 
RUN npm install

# Copying the rest of the application code
COPY public/ ./public
COPY src/ ./src

# Exposing the port the app runs on (assuming your frontend app runs on port 3000)
EXPOSE 3000

# Command to run the application
>>>>>>> b3af0c27a90eb1209867628a807ce32fd43e287d
CMD ["npm", "start"]