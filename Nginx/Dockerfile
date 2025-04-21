# Use official nginx 1.19 image based on Alpine
FROM nginx:1.19-alpine

# Add a non-root user and group
RUN addgroup -S nginxuser && adduser -S nginxuser -G nginxuser

# Create directories with correct permissions
RUN mkdir -p /var/nginx /var/run \
    && chown -R nginxuser:nginxuser /var/nginx /var/run /var/log/nginx /etc/nginx

# Remove default server config if not needed
RUN rm /etc/nginx/conf.d/default.conf

# Replace the default nginx config and add a secure one if needed
COPY nginx.conf /etc/nginx/nginx.conf

# Use non-root user to run nginx
USER nginxuser

# Expose only the necessary port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
