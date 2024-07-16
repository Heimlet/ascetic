FROM node:16-alpine as build-frontend

WORKDIR /app/frontend

COPY .env .env

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend ./
RUN npm run build

FROM python:3.10-slim as build-backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend

COPY .env .env

COPY backend/requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY backend ./

RUN python manage.py collectstatic --noinput

FROM nginx:alpine

COPY --from=build-frontend /app/frontend/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build-backend /app/backend /app/backend

COPY --from=build-backend /app/backend/staticfiles /app/backend/staticfiles

RUN apk add --no-cache python3 py3-pip postgresql-client
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

COPY backend/entrypoint.sh /app/backend/entrypoint.sh
RUN chmod +x /app/backend/entrypoint.sh

WORKDIR /app/backend

EXPOSE 80

ENTRYPOINT ["/app/backend/entrypoint.sh"]
