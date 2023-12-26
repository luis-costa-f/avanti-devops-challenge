FROM rabbitmq:3-management

# define os user e o password
ENV RABBITMQ_DEFAULT_USER=user
ENV RABBITMQ_DEFAULT_PASS=password

# expor portas
EXPOSE 5672 15672

# Comando de inicialização do RabbitMQ
CMD ["rabbitmq-server"]